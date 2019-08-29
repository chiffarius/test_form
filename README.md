Example test automation for certain form generator.

This code is made for Windows (as it uses chromedriver.exe)
Requirements:

Windows,
Chrome Browser installed and in PATH,
Python 3.7,
pip,
allure (https://docs.qameta.io/allure/#_installing_a_commandline)

How to run tests and view generated report:

'pip install -r requirements.txt' or 'python -m pip install requirements.txt'

'pytest --alluredir=my_allure_results'

'allure serve my_allure_results/'