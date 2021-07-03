ythonSeleniumExample
This repo is created to show subjects below:

* **Selenium** library usage with Python.
* Getting arguments in terminal before executing python file.
* You should add selenium drivers to path in your pc.

[Pyhton]: https://www.python.org/
[Pytest]: https://docs.pytest.org/en/6.2.x/getting-started.html
[Allure]: https://docs.qameta.io/allure/
[pytest-html-reporter]: https://github.com/prashanth-sams/pytest-html-reporter
## How It Works

1. Install **[Pyhton]** to your pc.(Python 3.9.0)
2. Install **[Pytest]** to your pc via pip.
3. Install **[Allure]** to your pc.
4. Install **[pytest-html-reporter]** to your pc.

## Usage
When every instalation is done you use command below for execution the test.
* --alluredir variable is the path the results of the test will be stored for allure framework
* --html variable is the path the results of the test will be stored for python html report

 ```sh
    $ pytest --alluredir="./allure_results" --html=./results/report.html 
 ```
To create allure test report you should execute command below:

 ```sh
    $ allure serve <path of the allure results folder>  
 ```