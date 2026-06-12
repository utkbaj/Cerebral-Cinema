# Cerebral Cinema - Week 2
## JEPA & Energy-Based Models

(This is an introduction for those who were absent in the DJAC Meet)

Hey everyone! Hope the Week 1 tasks went well :))

This week we go a level deeper, we're moving from "what is a transformer" to "how does a model actually *learn* a structured understanding of the world." The answer, at least according to Yann LeCun, involves Energy-Based Models and JEPA. This is probably the most theoretically dense week of the project, so take your time with the material.

---

## What We're Covering This Week

### Perception-Action Episodes (Mode 1 & Mode 2)
LeCun's framework distinguishes between two modes of intelligence:
- **Mode 1**: Fast, reactive, perception-action loops — think reflexes or visuomotor responses
- **Mode 2**: Slow, deliberate, model-based planning — the kind of reasoning that uses an internal world model

Understanding this distinction is key to seeing *why* JEPA is designed the way it is. This was discussed in detail in the offline session, but you may refer to Figure 3 & Figure 4 of [this paper](https://openreview.net/pdf?id=BZ5a1r-kVsf) for a visual understanding. Also, you can find the notes in the "Notes" folder on Github.
For your convenience, the paper is also attached as a PDF in the notes folder. 

### Energy-Based Models (EBMs)
An EBM assigns a scalar **energy** to every configuration of variables. Learning is about shaping this energy landscape so that:
- Compatible (x, y) pairs → **low energy**
- Incompatible pairs → **high energy**

This is a much more general framework than your standard supervised classifier. It sidesteps the need to model explicit probability distributions, which is what makes it so flexible. The reading material is availabe in the "Notes folder" on Github. 

### Energy Landscapes & Latent Variable EBMs (LV-EBMs)
Real data is messy and multimodal. A plain EBM struggles to capture multiple valid outputs for a single input (e.g., a video frame could be followed by *many* plausible futures). **Latent Variable EBMs** introduce a latent variable `z` that indexes over this set of plausible outputs, letting the model represent uncertainty and multimodality in a principled way.

The resources are available in the "Notes" folder. 

### JEA & I-JEPA
**Joint Embedding Architectures (JEA)** are the family of models that learn by comparing representations in an embedding space rather than reconstructing pixels. This is the core design philosophy behind JEPA.

**I-JEPA** (Image JEPA) instantiates this for images:
- A **context encoder** processes a masked view of the image
- A **predictor** takes those context representations and tries to predict the representations of *target* blocks
- A **target encoder** (EMA of the context encoder) produces the prediction targets

The paper is uploaded in the notes folder and the PPT for the session will be shared once the session is done. 

---

## This Week's Task

### CIFAR-10 Representation Learning Benchmark

You'll be comparing three families of models on CIFAR-10, probing the quality of their learned representations.

**Models to compare:**
1. **I-JEPA** (pretrained or trained from scratch)
2. **MAE** (Masked Autoencoder)
3. **CNN-based methods** (e.g., ResNet, a simple ConvNet trained with cross-entropy)

**Evaluation protocols:**

For each model, run two evaluations:

| Protocol | Description |
|---|---|
| **Linear Probe** | Freeze the backbone, train only a linear classifier on top |
| **LoRA / QLoRA Fine-tune** | Attach low-rank adapters to the backbone and fine-tune end-to-end (for CNNs this is just finetuning a few layers)|

**Deliverable:** A short write-up (can be a notebook) with your results table, training curves, and a few lines of analysis per comparison.

**Resouces:**
- Article on LoRA (just for basic understanding, don't get too involved with this): https://www.ibm.com/think/topics/lora#1029355617
- Basic idea on peft: https://huggingface.co/blog/peft
  
**DEADLINE: 11th June 2026, EOD**
