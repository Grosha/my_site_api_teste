# API tests for service 'MySiteReport'

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

Python 3.7
Pip

```
$ brew install python
```

### Installing

A step by step series of examples that tell you have to get a development env running

1) Install pipenv

```
$ pip install pipenv
```

2) Proceed to project folder and install all needed dependencies

```
$ pipenv install --dev
```

At this point you could work with code, just set in your ide right path to python interpreter - virtual env that was created in previous steps.


### Run tests:

1. Go to the project folder in terminal
2. Enter:
    ```
    $ pipenv run pytest tests/
    ```

### Check report:

1. Report will presence in the terminal
2. Report could be seen via browser -> go to the folder with project -> open file **pytest_report.html**


## Author
@grosha
