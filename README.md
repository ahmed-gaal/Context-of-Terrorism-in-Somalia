# ML - Capstone
# Introduction

*   This is the Machine Learning Nanodegree Capstone Project repository that
    contains all the code used to successfully complete this project.
************

*   The data that will be used throughout the course of this project was obtained
    from the National Consortium for the Study of Terrorism and Responses to 
    Terrorism of the University of Maryland.

You can find the complete dataset [here](https://drive.google.com/uc?id=182QuypWQDczgbSoObr9FxnVF6BcTrLTD)
You can also find the visualizations of the dataset in the
interactive web application [here](https://somali-warfare.herokuapp.com/)

*********
### How to use the workflow
*   Clone the repository
>   git clone https://github.com/ahmed-gaal/ml-capstone.git
*   Create virtual environment
>   python3 -m venv env
*   Activate virtual environment
>   source env/bin/activate
*   Install project dependencies
>   pip install -r requirements.txt
*   Load data for the workflow to commence
>   export DATA='https://drive.google.com/uc?id=182QuypWQDczgbSoObr9FxnVF6BcTrLTD'
*   Initiate workflow production
>   dvc repro
