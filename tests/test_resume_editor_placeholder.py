import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(r'C:\\Drivers\\chromedriver-win64\\chromedriver.exe')  # Update path if needed
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    return driver

def test_resume_editor_placeholder_behavior():
    driver = setup_driver()
    try:
        driver.get("https://www.naukri.com/resume-editor")
        time.sleep(1)

        section_to_edit = driver.find_element(By.CSS_SELECTOR, "div[class='sectionRowContainer'] div:nth-child(2) div:nth-child(1) div:nth-child(1) p:nth-child(1)")
        section_to_edit.click()
        time.sleep(1)

        editor = driver.find_element(By.XPATH, "//div[@class='DraftEditor-root']")
        editor.click()
        time.sleep(1)

        try:
            popup = driver.find_element(By.XPATH, "//div[@class='btn-text']")
            if popup.is_displayed():
                popup.click()
                time.sleep(1)
        except Exception:
            pass

        ordered_list_btn = driver.find_element(By.XPATH, "//div[@title='Ordered']")
        ordered_list_btn.click()
        time.sleep(1)

        placeholder = driver.find_element(By.CLASS_NAME, "public-DraftEditorPlaceholder-inner")
        print("After Ordered List - placeholder visible:", placeholder.is_displayed())
        check.is_false(placeholder.is_displayed(), "BUG: Placeholder should not be visible after applying ordered list")

        actions = ActionChains(driver)
        actions.send_keys("Test Item").perform()
        time.sleep(1)
        actions.send_keys("\b" * 9).perform()
        time.sleep(1)

        placeholder = driver.find_element(By.CLASS_NAME, "public-DraftEditorPlaceholder-inner")
        print("After text delete - placeholder visible:", placeholder.is_displayed())
        check.is_false(placeholder.is_displayed(), "BUG: Placeholder visible after deleting text for ordered list")

        editor.click()
        time.sleep(1)
        unordered_list_btn = driver.find_element(By.XPATH, "//div[@title='Unordered']")
        unordered_list_btn.click()
        time.sleep(1)

        placeholder = driver.find_element(By.CLASS_NAME, "public-DraftEditorPlaceholder-inner")
        print("After Unordered List - placeholder visible:", placeholder.is_displayed())
        check.is_false(placeholder.is_displayed(), "BUG: Placeholder should not be visible after applying unordered list")

        actions.send_keys("Bullet Item").perform()
        time.sleep(1)
        actions.send_keys("\b" * 12).perform()
        time.sleep(1)

        placeholder = driver.find_element(By.CLASS_NAME, "public-DraftEditorPlaceholder-inner")
        print("After unordered list text delete - placeholder visible:", placeholder.is_displayed())
        check.is_false(placeholder.is_displayed(), "BUG: Placeholder visible after deleting text for unordered list")

    finally:
        driver.quit()
