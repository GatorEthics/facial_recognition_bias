# Table of contents

* [About](#about)
* [Installation](#installation)
* [info for developers](#info-for-developers)
* [info for users](#info-for-users)
* [testing](#testing)
  + [Automated Testing](#automated-testing)
  + [Code Linting](#code-linting)
* [Run](#run)
* [ethical discussions](#ethical-discussions)
* [future work](#future-work)
* [Contributing](#contributing)
* [Data used](#data-used)

## About

Facial recognition software has become very popular in many industries, including but not limited to law enforcement, airports, healthcare facilities, technology manufacturing companies. These type of technologies let the users track people without their knowledge and gather data about them. As facial recognition software gains popularity some ethical issues are rising regarding the development and use of these tools. According to a report by the [National Institute of Standards and Technology](https://www.nist.gov/news-events/news/2019/12/nist-study-evaluates-effects-race-age-sex-face-recognition-software), comercial facial recognition tools exhibited biases with age, gender and race.This is an important issue because biased facial recognition technology in law enforcment may lead to false accusations and arrests, or in airports it may cause delayed flights.
Therefore the purpose of this project is to highlight ethical issues with face recognition technologies, compare efficiency of different classification algorithms and raise questions about development and use of face recognition tools.

## Installation

- Clone the source code onto your machine

    With HTTPS:

    `https://github.com/Allegheny-Mozilla-Fellows/facial_recognition_bias.git`

    or With SSH:

    `git@github.com:Allegheny-Mozilla-Fellows/facial_recognition_bias.git`

- Install Poetry(Recommended)

    Poetry is a tool for dependency managment and packaging in Python. Please follow the documentation [here](https://python-poetry.org/docs/#installation) on how to install poetry on your machine

## Run

- With Poetry(Recommended)

    After pulling the repo, use `poetry shell` in `facial_recognition_bias/` to enter the virtual environment. Under the virtual environment, use `poetry install` to install dependencies. Please refer to poetry documentation [here](https://python-poetry.org/docs/basic-usage/#installing-dependencies) for more info about dependency installation.

    After entering the virtual environment and installing the dependencies please refer to the following links for the detailed info on how to run each classifier.

    - [Convolution Neural Network(CNN)](src/CNN/README.md)
    - Multi-layer Perception(MLP)
    - Random Forest(RandomForest)
    - Support Vector(SVM)

- Without Poetry

    Alternatively all dependencies required for this project will need to be installed
    locally on your machine. You may use `pip` for that purpose.

    `python3 -m pip install --upgrade pip`
    `pip install package`

    After installing all the dependencies please refer to the following links for the detailed info on how to run each classifier.

    - Convolution Neural Network(CNN)
    - Multi-layer Perception(MLP)
    - Random Forest(RandomForest)
    - Support Vector(SVM)

## Development info

## Testing

## Future work

## Reading Material

## Ethical Discussions

## Data used

The images used used in this project are retrieved from [Kaggle](https://www.kaggle.com/) and are stored in file `data/images` directory. File stores about 10 000 face images. The images are annotated with age, gender and ethnicity. The images are cropped and aligned.

The labels of each face image is embedded in the file name, formatted like
age_gender_race_date&time.jpg

- age is an integer from 0 to 116, indicating the age
- gender is either 0 (male) or 1 (female)
- race is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).

More information on data can be found [here](https://susanqq.github.io/UTKFace/).