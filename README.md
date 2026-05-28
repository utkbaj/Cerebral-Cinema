# English to Hindi Translation using PyTorch Transformer

This version fixes the earlier `<unk> <unk>` problem by using SentencePiece subword tokenization instead of simple word splitting.

## Why the old model failed

The old version used `.split()` tokenization and a small word vocabulary. Many words were outside the vocabulary, so the model produced `<unk>`.

This version uses BPE subwords. Rare words are broken into smaller known pieces, so unknown output is much less common.

## Folder structure

```text
project/
├── data/
│   ├── opus.en-hi-train.en
│   ├── opus.en-hi-train.hi
│   ├── opus.en-hi-dev.en
│   ├── opus.en-hi-dev.hi
│   ├── opus.en-hi-test.en
│   └── opus.en-hi-test.hi
├── config.py
├── check_data_leakage.py
├── train_tokenizers.py
├── dataset.py
├── transformer_model.py
├── train_transformer.py
├── translate.py
├── evaluate.py
└── requirements.txt
```

## Data leakage control

1. Tokenizers are trained only on train files.
2. Model is trained only on train pairs.
3. Dev set is used only for validation.
4. Test set is used only for final evaluation.
5. `check_data_leakage.py` checks exact duplicate sentence-pairs across train/dev/test.

## Run order

Install:

```bash
pip install -r requirements.txt
```

Check leakage:

```bash
python check_data_leakage.py
```

Train tokenizers:

```bash
python train_tokenizers.py
```

Train model:

```bash
python train_transformer.py
```

Translate:

```bash
python translate.py
```

Evaluate:

```bash
python evaluate.py
```

## Kaggle note

Use GPU and keep paths inside `/kaggle/working/`. Copy this project to Kaggle, put data files in the `data/` folder, then run the same commands.
