
# Traffic Sign Image Classification

This is a streamlit app which helps you to classify images of different traffic signs. In total we have 58 classes in the Data Set.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Download and install [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

### Installation

1. First check python version in terminal, if it's 3.10.0 then go ahead.
   ```sh
   python --version 
   ```

2. Go to folder where you want to clone this repository and use below command to clone this repo to your local machine.
   ```sh
   git clone https://github.com/ipiyushvaghela/TrafficSignClassification.git
   ```
3. Create virtual Environment 
   ```sh
   python -m venv venvForTrafficSign --system-site-packages
   ```

   To Activate our virtual environment we use 
   ```sh
   venvForTrafficSign/Script/Activate.bat
   ```
4. Install packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
4. Now check if streamlit is installed properly or not.
   ```sh
   streamlit version
   ```

## Usage

1. Run below command in terminal to run streamlit application. 
   ```sh
   streamlit run app.py
   ```
Now we are all set to go. just upload the image of any given class and it will classify that image and also it gives other 5 possible classes from which image could belong to.

![App Screenshot](https://github.com/ipiyushvaghela/static/blob/main/TrafficSignClassification.jpeg?raw=true)

## Info about other folders
1. Folder named `BestPerformingModels` contains 1 model which has .h5 extension and this used in `app.py` file.
2. Folder named `ModelBuildingIPYNBs` contains IPYNB files in which all the code is present, by using those IPYNBs our model is created, you can customize the code according to your need.

## Contact

Piyush Vaghela - [@ipiyushvaghela](https://twitter.com/ipiyushvaghela) - ipiyushvaghela@gmail.com

Project Link -  [github.com/ipiyushvaghela/TrafficSignClassification](https://github.com/ipiyushvaghela/TrafficSignClassification.git)