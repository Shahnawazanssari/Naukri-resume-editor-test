# Naukri Resume Editor UI Bug Test

This project automates the validation of a specific UI behavior in the **Naukri.com Resume Editor**. It aims to identify and reproduce a bug where the **placeholder text does not behave correctly** when applying ordered or unordered list formatting to an empty editor.


## What It Tests

- Verifies that the placeholder disappears when list formatting is applied to an empty field.
- Checks that the placeholder does **not** reappear when the text is deleted after typing in a list.
- Tests this behavior for both **ordered** and **unordered** lists.
- Uses **soft assertions** via `pytest-check` so all checks are performed, even if one fails.


## Tech Stack

- **Language**: `Python`
- **Testing Framework**: `Pytest`
- **Browser Automation**: `Selenium`
- **Soft Assertions**: `Pytest-check`
- **HTML Reports**: `Pytest-html`


### Requirements

- Python 3.x+
- Google Chrome browser
- ChromeDriver


## How to Run
```bash
pip install -r requirements.txt
pytest tests/ --html=report.html --self-contained-html
