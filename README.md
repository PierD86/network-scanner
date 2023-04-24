network scanner
==============================

Create a network scanner to understand devices connected to the target subnet

Virtual Env creation
-----
- move to the project folder
- run `python -m venv env`
- run `env\Scripts\activate`
- run `pip install -r requirements.txt`
- run `pre-commit install`

Check Type Hinting
-----
- move to the project folder containing `pippo.py` you want to check
- run `mypy pippo.py`

Create scanner.exe
-----
- run `pyinstaller --onefile src/scanner.py`
- run `bash bash/exe-cleaner.sh`


Project Organization
--------------------

    ├── LICENSE
    ├── README.md                   <- General information
    ├── .pre-commit-config.yaml     <- Pre-commit configuration
    ├── requirements.txt            <- Requirements file for reproducing virtual environment
	├── env                         <- Virtual Enviroment
    ├── data                        <- Folder with data
	├── notebooks                   <- Jupyter notebooks
    └── src                         <- Source code of the project

--------
