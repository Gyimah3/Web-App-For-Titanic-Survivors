# Web-App-For-Titanic-Survivors

In this project, I built a web App with a user-friendly interface to embed my ML model from Titanic Survival Prediction Project.

### Manual Setup

For manual installation, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: friendly_web_interface_for_ML_models> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

    **NB:** For MacOs users, please install `Xcode` if you have an issue.



- Run the demo apps (being at the repository root):

        streamlit run strmlit_app.py

- You can access the hosted app on Huggingface spaces at the link below :
