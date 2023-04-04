# KennethLM

<!-- [![documentation](https://github.com/kennethenevoldsen/KennethLM/workflows/documentation/badge.svg)][documentation] -->
[![Tests](https://github.com/KennethEnevoldsen/KennethLM/actions/workflows/tests.yml/badge.svg)][tests]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/KennethLM/
[documentation]: https://kennethenevoldsen.github.io/KennethLM/
[tests]: https://github.com/kennethenevoldsen/KennethLM/actions?workflow=Tests
[black]: https://github.com/psf/black

KennethLM is a reimplementation of [NanoGPT] for experimentation with generative language models. It works coincidentally with Danish texts, but might 
just as well be evaluated on English. The goal of the repository in to better understand these types of models and have a repository where changes to
these are easy to examine.

I also have a slight idea to use this in an educational context.

## Intended Plan
- Implement bigram model (the starting point)
  - Add dataset (DAGW, everything should be open source)
  - Add evaluation dataset
    - test set of DAGW (upload it to HF)
      - Domain Perplexity (this will probably be enough to start off with)
    - (any open-source summerization?)
    - Sentiment analysis
    - Scandi Q/A
    - Lexical acceptability
  - Add functionality
- One by one implement the changes off Karpathy to see the effect
  - Add previous token mean
  - ...
- Check the effect of dataset distribution
- check the effect of tokenizers
- check the effect of the fast attention Lasse mentioned
- effect the type of positional embeddings

### Push workflow
The intended PR workflow is intended to have a model training just large enough to be runable on a macbook using the GPU. Preferably also on an
(free?) server GPU? The goal is to train the best obtainable model using ~15 minutes on a macbook GPU. 

For each improvement it should be clear that it is an improvement. 
- Thus is should be run 5 times with a small model
- We will evaluate it on a seq2seq benchmark
- If it is better it will be merged with the scores of the improvement
- If it is not better (or inconclusive) it will be added to a negative results section
- check if an approach can improve upon the previous best model (using a halfway checkpoint can it obtain a better trajectory?)
  - Probably hard to implement, probably easier to just plot the trajectories


## Installation

```bash
git clone https://github.com/kennethenevoldsen/KennethLM
pip install -e .
```

## Usage

[NanoGPT]: https://github.com/karpathy/nanoGPT
