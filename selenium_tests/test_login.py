import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith", "SuperSecretPassword!", "success"),
    ("tomsmith", "wrongpassword", "failure"),
    ("wronguser", "SuperSecretPassword!", "failure")
])

def test_login(username, password, expected):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)

    message = driver.find_element(By.ID, "flash").text

    if expected == "success":
        assert "You logged into a secure area!" in message
    else:
        assert "Your username is invalid!" in message or "Your password is invalid!" in message

    driver.quit()