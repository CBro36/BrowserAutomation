# Browser Automation

This project is a collection of automated test scripts. The website these tests are performed on is located here: <https://the-internet.herokuapp.com/>. All the tests are written in Python.

## Dependencies

- Selenium
- Selenium-wire
- PyAutoIt
- Google Chrome & Chromedriver (latest versions)

## How to Run

### Running all Tests

While in the `BrowserAutomation` directory, run every test in succession by running `run_tests.py`.

e.g. `python run_tests.py`

### Running a Single Test

While in the `BrowserAutomation` directory, run a specific test in the `Tests` directory by using `unittest`.

e.g. `python -m unittest Tests/test_add_remove.py`
