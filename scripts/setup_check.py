"""Check that this machine is ready for the school.

Run from anywhere inside the cloned repository:

    python scripts/setup_check.py

Every line should end in OK. Bring the output to the instructor if one does not.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EXPECTED = {
    "heart_cleveland.csv": (302, 14),
    "pima_diabetes.csv": (768, 9),
    "breast_cancer_wdbc.csv": (569, 31),
    "diabetes_progression.csv": (442, 11),
}

problems = []


def check(label, ok, detail=""):
    print(f"{label:<44} {'OK' if ok else 'PROBLEM'}  {detail}")
    if not ok:
        problems.append(label)


print(f"{'Python ' + sys.version.split()[0]:<44} {'OK' if sys.version_info >= (3, 9) else 'PROBLEM'}")

try:
    import numpy, pandas, sklearn, scipy, matplotlib
except ImportError as e:
    print(f"\nMissing package: {e.name}")
    print("Run: pip install -r requirements.txt")
    raise SystemExit(1)

major, minor = (int(p) for p in sklearn.__version__.split(".")[:2])
check(f"scikit-learn {sklearn.__version__}", (major, minor) >= (1, 4), "needs 1.4 or newer")
check(f"pandas {pandas.__version__}", True)
check(f"numpy {numpy.__version__}", True)
check(f"scipy {scipy.__version__}", True)
check(f"matplotlib {matplotlib.__version__}", True)

print()
for name, (rows, cols) in EXPECTED.items():
    path = DATA / name
    if not path.exists():
        check(name, False, "file is missing")
        continue
    shape = pandas.read_csv(path).shape
    check(name, shape == (rows, cols), f"{shape[0]} rows, {shape[1]} columns")

ecg = DATA / "ecg_mitbih_208.npy"
if ecg.exists():
    signal = numpy.load(ecg)
    check("ecg_mitbih_208.npy", signal.shape == (108000,), f"{len(signal)} samples = {len(signal)/360:.0f} s")
else:
    check("ecg_mitbih_208.npy", False, "file is missing")

print()
if problems:
    print(f"{len(problems)} problem(s): " + ", ".join(problems))
    raise SystemExit(1)
print("Everything is ready. Open notebooks/lab1_breast_cancer.ipynb.")
