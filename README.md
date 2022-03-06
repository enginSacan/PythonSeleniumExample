# PythonSeleniumExample

This repo is created to show subjects below:

* **Selenium** library usage with Python.
* Getting arguments in terminal before executing python file.
* You should add selenium drivers to path in your pc.

[Pyhton]: https://www.python.org/
[Pytest]: https://docs.pytest.org/en/6.2.x/getting-started.html
[Allure]: https://docs.qameta.io/allure/
[pytest-html-reporter]: https://github.com/prashanth-sams/pytest-html-reporter
[pytest-html]: https://pypi.org/project/pytest-html/
## How It Works

1. Install **[Pyhton]** to your pc.(Python 3.9.0)
2. Install **[Pytest]** to your pc via pip.
3. Install **[Allure]** to your pc.
4. Install **[pytest-html-reporter]** to your pc.
5. Install **[pytest-html]** to your pc.

## Usage
When every instalation is done you use command below for execution the test.
* --alluredir variable is the path the results of the test will be stored for allure framework
* --html variable is the path the results of the test will be stored for python html report
* --browser variable is for browser choose (chrome or firefox)

 ```sh
    $ pytest --alluredir="./allure_results" --html=./results/report.html --browser=firefox
 ```
To create allure test report you should execute command below:

 ```sh
    $ allure serve <path of the allure results folder>  
 ```
## Test Cases
### Task-1
* Navigate to https://www.n11.com/
* Log in with facebook
* Verify successful login
### Task-2
* Navigate to https://www.n11.com/
* Navigate to Perfume & Deodorant under the Cosmetic & Personal Care tab. (Do not
use URL navigation)(Kozmetik & Kişisel Bakım/Parfüm & Deodorant)
* Search for ‘Lacoste’ in Brand filter
* Select ‘Lacoste’
* Click 7th product on the search result page
* Add product to the ‘Favorites’ (Favorilerim)
* Navigate to Favorites (Favorilerim)
* Verify the product title is the same as with the product details page
### Task-3
* Navigate to https://www.n11.com/
* Write all the links at the footer to the text file (About us, help, etc)
* Click Brands (Markalar) at the footer
* Verify the footer links with the text file
