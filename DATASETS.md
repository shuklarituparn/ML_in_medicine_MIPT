# Datasets

Every file in `data/` contains real patient measurements from a published clinical dataset.
Nothing here is simulated. Below: where each one came from, what was done to it to produce
the copy in this repository, and what is wrong with it.

Read the "Known problems" lines before you build anything. Most of the marks on Wednesday
come from knowing them.

---

## heart_cleveland.csv

**302 patients, 13 features, 164 with heart disease (54 percent).**

Patients referred for coronary angiography at the Cleveland Clinic Foundation. The target is
whether angiography found a narrowing of more than 50 percent in any major vessel.

- Primary source: UCI Machine Learning Repository, Heart Disease (Cleveland subset),
  https://archive.ics.uci.edu/dataset/45/heart+disease
- Original publication: Detrano R. et al., *International application of a new probability
  algorithm for the diagnosis of coronary artery disease*, American Journal of Cardiology,
  1989;64:304-310.
- Collected: Cleveland Clinic Foundation, principal investigator Robert Detrano MD PhD.

**What was done to it here.** The widely circulated analysis copy was used: the original
five-level target (0 to 4 by severity) collapsed to 0 and 1, and the six rows with missing
`ca` and `thal` values already filled. One exactly duplicated row was removed, leaving 302
of the original 303.

**Known problems.**
- The patients were all referred for angiography, so they were already suspected of having
  coronary disease. The 54 percent prevalence here is nothing like the prevalence in a
  general population. Your PPV calculation has to account for that.
- `ca` and `thal` arrived with missing values that somebody else imputed before this copy
  existed. You cannot see which rows were affected.
- 302 patients is small. Expect cross-validation standard deviations around 0.05 on AUC, and
  do not report a difference smaller than that as a result.

---

## pima_diabetes.csv

**768 patients, 8 features, 268 with diabetes (34.9 percent).**

All participants are women of at least 21 years of age and of Pima (Akimel O'odham) heritage,
near Phoenix, Arizona. The target is whether the patient was diagnosed with diabetes within
five years of the examination, by World Health Organization criteria.

- Primary source: UCI Machine Learning Repository / OpenML dataset 37,
  https://www.openml.org/d/37
- Original publication: Smith J.W. et al., *Using the ADAP learning algorithm to forecast the
  onset of diabetes mellitus*, Proceedings of the Symposium on Computer Applications in
  Medical Care, 1988:261-265.
- Collected: National Institute of Diabetes and Digestive and Kidney Diseases, from a
  longitudinal study of the Gila River Indian Community.

**What was done to it here.** Column names expanded from the original abbreviations. Nothing
else. The row count, the class balance and the zero counts all match the published dataset.

**Known problems.**
- Zeros are used as a missing-value code in five columns, and they are physiologically
  impossible: glucose 5, blood pressure 35, skin thickness 227, insulin 374, BMI 11. Insulin
  is missing for 49 percent of patients. Treating those zeros as real numbers is the single
  most common mistake made with this dataset.
- One community, one sex, one age range. A model fitted here describes this population.
- The Akimel O'odham community has publicly criticised the long history of research conducted
  on it. If you present this dataset, say whose data it is.

---

## breast_cancer_wdbc.csv

**569 patients, 30 features, 212 malignant and 357 benign.**

Features are computed from a digitised image of a fine needle aspirate of a breast mass:
ten characteristics of each cell nucleus (radius, texture, perimeter, area, smoothness,
compactness, concavity, concave points, symmetry, fractal dimension), each reported as a
mean, a standard error and a worst value.

- Primary source: UCI Machine Learning Repository, Breast Cancer Wisconsin (Diagnostic),
  https://archive.ics.uci.edu/dataset/17
- Original publication: Street W.N., Wolberg W.H., Mangasarian O.L., *Nuclear feature
  extraction for breast tumor diagnosis*, IS&T/SPIE International Symposium on Electronic
  Imaging, 1993;1905:861-870.
- Collected: University of Wisconsin Hospitals, Madison, by Dr William H. Wolberg.

**What was done to it here.** Exported from `sklearn.datasets.load_breast_cancer`, which
ships the UCI file. The label is written as M and B rather than 0 and 1, deliberately, so
that you have to decide which class is positive rather than inheriting somebody's choice.

**Known problems.**
- The features are measurements somebody already extracted from the images. You are not
  working with images, you are working with one radiologist's feature definitions.
- Radius, perimeter and area correlate at about 0.99. Any statement about the importance of
  one of them individually is close to meaningless.
- The classes separate very well, so almost any model scores above 0.95 AUC. That makes it a
  good teaching dataset and a bad dataset for showing that your method is clever.

---

## diabetes_progression.csv

**442 patients, 10 features, continuous target from 25 to 346.**

Age, sex, BMI, mean arterial pressure and six blood serum measurements, taken at baseline.
The target is a quantitative measure of disease progression one year later.

- Primary source: shipped with scikit-learn as `load_diabetes`; originally distributed with
  the paper below.
- Original publication: Efron B., Hastie T., Johnstone I., Tibshirani R., *Least Angle
  Regression*, Annals of Statistics, 2004;32(2):407-499.

**What was done to it here.** Exported with `scaled=False`, so the columns are in their
original units rather than the centred and normalised version scikit-learn returns by
default. Use these raw values: the scaled version was normalised over the whole dataset,
test rows included.

**Known problems.**
- The target is a composite score in arbitrary units. An error of 45 points is not
  interpretable without asking a clinician what magnitude of change would alter treatment.
  Saying so is part of the work.
- The six serum measurements are published only as s1 to s6. Nobody using this dataset can
  tell you what they are, which makes any claim about mechanism impossible.

---

## ecg_mitbih_208.npy

**108,000 samples at 360 Hz, which is five minutes from one patient. About 500 beats.**

A single-channel ECG excerpt from record 208 of the MIT-BIH Arrhythmia Database.

- Primary source: PhysioNet, MIT-BIH Arrhythmia Database, https://physionet.org/content/mitdb/
- Original publications: Moody G.B., Mark R.G., *The impact of the MIT-BIH Arrhythmia
  Database*, IEEE Engineering in Medicine and Biology, 2001;20(3):45-50. And Goldberger A.L.
  et al., *PhysioBank, PhysioToolkit, and PhysioNet*, Circulation, 2000;101(23):e215-e220.
- Collected: Beth Israel Hospital Arrhythmia Laboratory, 1975 to 1979.

**What was done to it here.** Exported from `scipy.datasets.electrocardiogram`, which
distributes this excerpt, and stored as float32 in millivolts.

**Known problems.**
- One patient, five minutes. Nothing you find here generalises to a population.
- The recording contains three stretches where the signal is corrupted and no beat can be
  detected, around 42, 96 and 209 seconds. They produce apparent gaps between beats of 2.3,
  2.6 and 4.8 seconds. Those are artefacts, not pauses, and if you leave them in they inflate
  every heart rate variability measure you compute.
- The beat labels that come with the original PhysioNet record are deliberately not included
  here. This track is unsupervised, and the point is to find the abnormal beats without them.

---

## Rebuilding these files

`scripts/fetch_data.py` rebuilds the three scikit-learn and SciPy files from their packages
and checks the row counts against the numbers above. The two UCI files are committed to this
repository because thirty laptops downloading them over conference wifi at the same moment is
a reliable way to lose twenty minutes.
