# Machine learning for medicine

MIPT International School, 19 to 21 October 2026.

Five real clinical datasets, four notebooks, and a project you defend on day three.

## Setup

```bash
git clone <this repository>
cd ml-for-medicine
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/setup_check.py
jupyter notebook
```

`setup_check.py` prints one line per dataset and per package. If every line says OK you are
ready. Bring the output to me if any line does not.

Nothing in this repository needs an internet connection after the clone. The data is here.

## What is where

| Path | What it is |
|---|---|
| `data/` | Five real clinical datasets. Provenance and known problems in `DATASETS.md`. |
| `notebooks/lab1_breast_cancer.ipynb` | Day 1 practice. Three models end to end, and choosing an operating point. |
| `notebooks/hw1_pima.ipynb` | Day 1 homework. Missing data, and what prevalence does to PPV. |
| `notebooks/ecg_codealong.ipynb` | Day 2. A raw ECG to abnormal beats, with no labels. |
| `notebooks/lab2_clinical_models.ipynb` | Day 2. Forests, imbalance, importance, calibration, thresholds. |
| `notebooks/project_starter.ipynb` | Your project. Start here unless you are on the ECG track. |
| `project/HANDOUT.md` | The five tracks and what every project must contain. |
| `project/GRADING.md` | The eight criteria you are marked on. Read this before you start, not after. |
| `DATASETS.md` | Where every dataset came from, and what is wrong with it. |

## Three rules for the week

1. Every cleaning step goes inside a scikit-learn `Pipeline`. Anything fitted outside it has
   seen your test data.
2. Report mean and standard deviation, never a single number. A difference smaller than the
   spread is not a difference.
3. The threshold is chosen on training data and applied to test once. Choosing it on the test
   set is the fastest way to lose marks on Wednesday.
