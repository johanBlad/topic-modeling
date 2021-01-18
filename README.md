# master-thesis-topic-modelling
Master thesis project by Johan Blad &amp; Karin Svensson, investigating topic models for finding topics in article text data.

The topic can be used for content analysis, for example, ad-hoc analysis as well as serve as a uniform categorization framework across several brands within Bonnier News.

The thesis can be found here: https://www.diva-portal.org/smash/get/diva2:1512130/FULLTEXT01.pdf

## Repository structure

The repository contains three main directories.
- **notebook_examples**
  
  containing example notebooks for topic modeling applications on custom datasets, showcasing example ad-hoc analyses.
- **src**
  
  containing Python utility functions for data preprocessing, data visualization etc.
- **legacy**
  
  containing legacy notebooks for historical purposes

## Setup

Clone the project.

### Python Dependencies

Install the necessary Python dependencies on your machine, or in a virtual environment, with conda or with pip.

`$ conda install --file requirements.txt`

or

`$ pip install -r requirements.txt`


### NLP Preprocessing library

Only compatible with UNIX-like OS.

The topic modeling applications in this repository requires extensive cleaning of the text data for good results. A custom text cleaning implementation for the Swedish language is used, called efselab-wrapper. This is a wrapper of the project [Efselab](https://github.com/robertostling/efselab). It is built in Python with C modules and Cython for efficient sequence labeling including Tokenization, Lemmatization, Part-of-Speech (POS) tagging, and Named Entity Recognition. To build the modules required for efselab-wrapper to work, run the following in the root directory.

`$ bash efselab_setup.sh`

This builds and compiles the library's C modules, trains the tagging binaries (for lemmatization, POS-tagging etc.), and places all built files in the correct directories. The efselab-wrapper module can now be used for text cleaning of Swedish texts, by importing `from src.efselabwrapper.pipeline import run_processing_pipeline` from a Python interpreter in the root directory.

## Notebook usage

The directory notebook_exampels holds three examples of how to perform topic modeling as well as how to visualize the result. We encourage you to use, edit and copy code from these example notebooks.

- **basic_example**

  a basic example of how to perform topic modeling.

- **adhoc_analysis_climate**

  in this example, articles from Dagens Nyheter's (DN) tagged with climate "Klimatet" are chosen, and then a topic modeling algorithm is applied to this data to learn what concepts (topics) DN is writing about in the context of the climate.

- **adhoc_analysis_coronavirus**

  in this example, articles from 3 brands within Bonnier News are chosen (Dagens Nyheter (DN), Dagens Industri (Di), and Expressen). The articles are tagged with the subject Corona virus. Then a topic modeling algorithm is applied to each of the 3 datasets to learn what concepts (topics) the different brands are writing about in the context of the coronavirus.
