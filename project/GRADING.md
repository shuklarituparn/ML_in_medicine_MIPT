# How you are marked

Eight criteria. Each is scored 0, 1, 2 or 3 by two reviewers independently, and the two
scores are averaged. The weights below turn that into a mark out of 100.

The scale is the same for every criterion:

- **0** — not there at all.
- **1** — there in form, but it does not work or it is not justified.
- **2** — done correctly.
- **3** — done correctly, and you can explain why it had to be done that way.

Most teams land on 2. A 3 is for knowing why.

| | Criterion | Weight |
|---|---|---|
| K1 | The clinical decision | 20 |
| K2 | Baseline | 10 |
| K3 | Honest evaluation | 15 |
| K4 | A number in clinical units | 10 |
| K5 | Uncertainty | 10 |
| K6 | Known failures | 10 |
| K7 | Defence | 20 |
| K8 | Audit of the next team | 5 |

## K1. The clinical decision (20)

- **0** — You output a prediction and stop. No decision appears anywhere in the work.
- **1** — There is a threshold, but it came from nowhere. 0.5, or a round number that looked
  reasonable.
- **2** — The threshold is derived from the cost of each error type, and computed correctly.
- **3** — The same, and you show how the answer moves when the cost ratio changes, and you
  name who in the hospital would have to agree to that ratio.

## K2. Baseline (10)

- **0** — No baseline. Nothing to compare your number against.
- **1** — A baseline is mentioned but not computed on the same data.
- **2** — Computed, your model beats it, and you state the size of the gap.
- **3** — More than one baseline, including the trivial clinical policy, such as testing
  everybody, and you say what share of the achievable benefit you actually captured.

## K3. Honest evaluation (15)

- **0** — Scored on training data, or a feature in the model that is only known after the
  outcome.
- **1** — A test set exists but it was used while choosing something. Or a failed experiment
  was quietly removed.
- **2** — The test set was held out from the start and used once. Negative results reported.
- **3** — The same, and you name where your own estimate might still be optimistic.

## K4. A number in clinical units (10)

- **0** — Only AUC, R² or MAE.
- **1** — Clinical units appear, but the number is not tied to your decision.
- **2** — Your headline result is in patients, cases caught, cases missed, or PPV at a
  prevalence you state.
- **3** — The same, and you say under what assumptions that number stops being true.

## K5. Uncertainty (10)

- **0** — Single numbers with no spread anywhere.
- **1** — Spread reported but ignored. A difference smaller than the standard deviation is
  announced as a winner.
- **2** — Mean and standard deviation for every model, and differences read against the
  spread.
- **3** — The same, and the probabilities are shown to be calibrated, or you state plainly
  that they are a ranking and should not be read as risks.

## K6. Known failures (10)

- **0** — No failure modes named.
- **1** — Generic statements: more data would help, the model is not perfect.
- **2** — At least three individual misclassified patients examined by hand, or a named
  subgroup where performance drops, with numbers.
- **3** — The same, plus the reason for the failure and what the clinician should do about it.

## K7. Defence (20)

- **0** — The team cannot answer questions, or answers something else.
- **1** — Only the person who wrote the code can answer. The rest of the team does not know
  how it works.
- **2** — Everyone answers on substance and admits the limits of their work.
- **3** — The team answers a question they did not prepare for, reasoning out loud, correctly.

## K8. Audit of the next team (5)

Each team asks the first question after the next team's talk. This criterion is about the
quality of your question, not your own project.

- **0** — No question asked.
- **1** — A formal question about presentation.
- **2** — A question about the substance of their solution.
- **3** — A question that found a real weakness, or that tested whether their approach would
  survive on your own data.

## What caps your score automatically

These are not judgement calls. If any of these is true, the criterion is capped regardless of
how good the rest is.

| What happened | Effect |
|---|---|
| The threshold or the model was chosen by looking at the test score | K3 no higher than 1 |
| Beats or visits from the same patient appear in both train and test | K3 = 0 |
| A feature in the model is only known after the outcome | K3 no higher than 1 |
| Zeros left as real values in Pima glucose, blood pressure, skin thickness, insulin or BMI | K3 no higher than 1 |
| The headline result is given only as AUC or R² | K4 no higher than 1 |
| PPV reported without stating the prevalence it assumes | K4 no higher than 1 |
| The threshold is 0.5 with no reason given | K1 no higher than 1 |
| A single cross-validation number with no spread | K5 no higher than 1 |

A reviewer who gives a 0 or a 1 on any criterion must write a comment. You will see the
comments after the defence.
