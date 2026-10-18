# Project: build and defend a clinical model

Teams of three. One track per team. Handed out at the end of the Day 2 lecture, defended on
Day 3: six minutes of talk, four minutes of questions.

You hand in two things: a notebook that runs top to bottom on a clean kernel, and six slides.

## The five tracks

Every track uses real patient data. Read that dataset's section in `DATASETS.md` before you
write any code, because half the marks come from knowing what is wrong with your data.

| Track | Data | The question | What makes it hard |
|---|---|---|---|
| T1 | `heart_cleveland.csv` | Does this patient have coronary disease? | 302 patients, so your CV spread will be around 0.05. Most apparent differences between models are noise. |
| T2 | `pima_diabetes.csv` | Will this patient develop diabetes within five years? | Zeros used as a missing-value code in five columns. Insulin is missing for half the patients. |
| T3 | `diabetes_progression.csv` | How far will the disease progress in a year? | Regression. The target is in arbitrary units, so you have to say what an error of 45 means. |
| T4 | `ecg_mitbih_208.npy` | Which beats in this recording are abnormal? | No labels at all. Start from `ecg_codealong.ipynb`, not the project starter. |
| T5 | `breast_cancer_wdbc.csv` | Diagnose the tumour using at most five features. | Everything scores above 0.95, so the work is choosing which five and defending the choice. |

Start from `notebooks/project_starter.ipynb`, except T4.

## What every project must contain

1. **Who uses this, and for what decision.** Name the user, the moment in the patient
   pathway, and the decision that changes. If no decision changes, change your framing now.
2. **What each error costs.** A false negative and a false positive in your problem. You do
   not need money, you need a ratio you would defend to a clinician.
3. **Cleaning inside a `Pipeline`.** Imputation, scaling, selection. Nothing fitted outside.
4. **A trivial baseline and two real models**, compared with 5-fold cross-validation, each
   reported as mean and standard deviation.
5. **A primary metric, chosen and justified clinically.** Not accuracy, unless you can argue
   specifically for it.
6. **An operating point.** The threshold chosen on training folds from your cost ratio, then
   applied to the test set once. Confusion matrix on test.
7. **Your headline number in clinical units**, including PPV at a prevalence you name.
8. **Error analysis.** At least three individual misclassified patients, examined by hand,
   with your explanation of why the model got each one wrong.
9. **Limitations.** The population the data came from, the sample size, and what would need
   to be true before anyone used this on a patient.

T3 replaces points 6 and 7 with error in clinical units and an analysis of where the model is
worst. T4 replaces points 4 to 7 with feature construction, clustering, and the evidence that
the cluster you found is real.

## Your six slides

1. Problem and clinical user
2. Data: source, size, class balance, what you cleaned and why
3. Method and cross-validated results, with the baseline next to them
4. Operating point, and the cost reasoning behind it
5. What the model learned, plus your three error cases
6. Limitations and what you would do next

Every number on a slide must be reproducible from the notebook you hand in. We will ask.

## Two ways teams lose marks every year

**Choosing the threshold on the test set.** We will ask to see the cell where it was chosen,
and what data was visible to you at that moment. This caps two criteria at once.

**Reporting a difference that is smaller than the spread.** On the heart data, logistic
regression scores about 0.894 and a random forest about 0.906, with standard deviations near
0.047. A team that announces the forest as the winner has not read its own output.

## One thing worth more than a high score

A model that does not beat the trivial policy at your cost ratio is a real finding, and
saying so in your defence scores better than hiding it. On several of these tracks that is
the honest answer.
