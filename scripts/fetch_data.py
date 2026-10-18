"""Rebuild the datasets that ship inside Python packages, and verify all five.

    python scripts/fetch_data.py

The two UCI files (heart_cleveland.csv, pima_diabetes.csv) are committed to this repository
and are not re-fetched: UCI and OpenML are frequently unreachable from conference networks.
Their provenance is in DATASETS.md. This script checks them against their published shapes
so that a corrupted or truncated copy fails loudly instead of quietly training a bad model.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer, load_diabetes

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

# Breast Cancer Wisconsin Diagnostic, UCI dataset 17, shipped with scikit-learn.
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
wdbc = X.copy()
wdbc["diagnosis"] = np.where(y == 0, "M", "B")
wdbc.to_csv(DATA / "breast_cancer_wdbc.csv", index=False)
print("breast_cancer_wdbc.csv     ", wdbc.shape, dict(wdbc.diagnosis.value_counts()))

# Diabetes progression, Efron et al. 2004. scaled=False keeps the original units.
Xd, yd = load_diabetes(scaled=False, return_X_y=True, as_frame=True)
prog = Xd.copy()
prog["progression"] = yd
prog.to_csv(DATA / "diabetes_progression.csv", index=False)
print("diabetes_progression.csv   ", prog.shape, f"target {yd.min():.0f} to {yd.max():.0f}")

# MIT-BIH record 208, five minutes at 360 Hz, via SciPy. Downloads once, then caches.
try:
    from scipy.datasets import electrocardiogram
    ecg = electrocardiogram().astype("float32")
    np.save(DATA / "ecg_mitbih_208.npy", ecg)
    print("ecg_mitbih_208.npy         ", ecg.shape, f"= {len(ecg)/360:.0f} seconds")
except Exception as e:
    existing = DATA / "ecg_mitbih_208.npy"
    if existing.exists():
        print(f"ecg_mitbih_208.npy          kept the committed copy ({type(e).__name__} on download)")
    else:
        raise SystemExit(f"Could not fetch the ECG and no committed copy exists: {e}")

EXPECTED = {
    "heart_cleveland.csv": (302, 14),
    "pima_diabetes.csv": (768, 9),
    "breast_cancer_wdbc.csv": (569, 31),
    "diabetes_progression.csv": (442, 11),
}
print()
for name, shape in EXPECTED.items():
    actual = pd.read_csv(DATA / name).shape
    if actual != shape:
        raise SystemExit(f"{name}: expected {shape}, found {actual}. See DATASETS.md.")
    print(f"{name:<28} {actual} verified")

ecg = np.load(DATA / "ecg_mitbih_208.npy")
assert ecg.shape == (108000,), f"ECG should be 108000 samples, found {ecg.shape}"
print(f"{'ecg_mitbih_208.npy':<28} {ecg.shape} verified")
