# Week 1 — English to Hindi Machine Translation

## Objective

The goal of Week 1 is to implement a **Transformer-based Neural Machine Translation (NMT)** system using **PyTorch** for **English → Hindi translation**.

You will work with a dataset that has already been split into **train** and **test** sets.

---

## Task Requirements

### Primary Task
Implement a **Transformer model** in PyTorch for **English to Hindi translation**.

### Additional Task (Recommended)
If time permits:

- Implement an **RNN/LSTM-based model**
- Compare outputs between:
  - Transformer
  - RNN
  - LSTM
- Analyze performance differences

The goal is not only to achieve good results, but also to understand how different sequence models behave.

---

## Dataset Information

The dataset has already been provided and is **split into train and test sets**.

### File Format
The dataset files:

- `.en` → English sentences
- `.hi` → Hindi sentences

These are **plain text files**, and can be loaded similarly to standard `.txt` files.

Example:

```python
with open("train.en", "r", encoding="utf-8") as f:
    english_sentences = f.readlines()

with open("train.hi", "r", encoding="utf-8") as f:
    hindi_sentences = f.readlines()
```
---
## Expected Deliverables

By the deadline, each group should submit:

### 1. Model Implementation

- Transformer implementation in **PyTorch**
- Proper **training pipeline**
- **Evaluation pipeline**

### 2. GitHub Repository

Push the following to GitHub:

- Source code
- Trained model(s)
- Scripts / notebooks
- Documentation

### 3. Documentation

Include proper documentation covering:

- Model architecture
- Dataset preprocessing
- Training methodology
- Hyperparameters
- Results and observations
- Challenges faced

### 4. Model Comparison *(Optional but Encouraged)*

If implemented:

- Compare **Transformer vs RNN/LSTM**
- Discuss strengths and weaknesses
- Show qualitative translation differences

---

## Resources for Week 1

For those who did NOT attend the meet, watch [this video](https://youtu.be/bCz4OMemCcA?si=CZiTQvqrgQ53ZAhQ) completely.

For those who did attend the meet:
1. Revise transformers: Read [Attention is All You Need](https://arxiv.org/pdf/1706.03762).
2. Introduction to LLMs: Watch the first 2 hours of this [video](https://youtu.be/7xTGNNLPyMI?si=d_Vty2O9JZCszIan).

Spend the rest of your time exploring the task and implementing the model.
