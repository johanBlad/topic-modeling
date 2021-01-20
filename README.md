# master-thesis-topic-modelling
Topic modeling implementation for finding topics in text data.

The topic can be used for content analysis, finding concrete overviewable insights from large volumes of text.

This work is based on an academic thesis, which can be found here: https://www.diva-portal.org/smash/get/diva2:1512130/FULLTEXT01.pdf

## Repository structure

The repository contains three main directories.
- **notebook_examples**
  
  containing example notebooks for topic modeling applications
- **src**
  
  containing Python utility functions for data preprocessing, data visualization etc.
- **legacy**
  
  containing legacy notebooks for historical purposes

## Setup

Clone the project.

### Dependencies

Install the necessary Python dependencies on your machine, or in a virtual environment.

`$ pip install -r requirements.txt`

There are two topic modeling algorithms avaialble, NMF and LDA. LDA builds on an external Java package (MALLET) and needs to be set up in order to be used. To do this, make sure you have the following installed:

- JDK
- Ant

Then run

`$ sh setup_mallet.sh`

### NLP Preprocessing library

Only compatible with UNIX-like OS.

The topic modeling applications in this repository requires extensive cleaning of the text data for good results. A custom text cleaning implementation for the Swedish language is used, called efselab-wrapper. This is a wrapper of the project [Efselab](https://github.com/robertostling/efselab). It is built in Python with C modules and Cython for efficient sequence labeling including Tokenization, Lemmatization, Part-of-Speech (POS) tagging, and Named Entity Recognition. To build the modules required for efselab-wrapper to work, run the following in the root directory.

`$ sh setup_efselab.sh`

This builds and compiles the library's C modules, trains the tagging binaries (for lemmatization, POS-tagging etc.), and places all built files in the correct directories. The efselab-wrapper module can now be used for text cleaning of Swedish texts, by importing `from src.efselabwrapper.pipeline import run_processing_pipeline` from a Python interpreter in the root directory.

### Data

The repo comes with some sample text datasets for trying out topic modeling. This includes both raw and preprocessed datasets. To use these, run 

`$ sh setup_data.sh`

which will download and unpack these datasets. Alternatively, copy lines from the script to only download specific datasets.

## Notebook usage

The directory notebook_exampels holds three examples of how to perform topic modeling as well as how to visualize the result.

- **basic_example**

  a basic example of how to perform topic modeling.
