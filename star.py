import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

user = 'Believe'
profile = 'Profile 4'

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'--user-data-dir=C:/Users/{user}/AppData/Local/Google/Chrome/User Data')
chrome_options.add_argument(f'--profile-directory={profile}')

totalNum = 700

def run_script():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # try:
    #     driver.get("https://github.com/johnsmith0212")

    #     wait = WebDriverWait(driver, 10)
    #     follow_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit" and @value="Unfollow"]')))
    #     follow_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit" and @value="Follow"]')))
    #     follow_button.click()
        
    #     stars_tab = wait.until(EC.element_to_be_clickable((By.ID, 'stars-tab')))
    #     stars_tab.click()

    #     star_buttons = wait.until(EC.elements_to_be_clickable((By.XPATH, '//button[normalize-space(span)="Star"]')))
    #     for star_button in star_buttons:
    #         star_button.click()

    # except Exception as e:
    #     print(e)

    # finally:
    #     driver.quit()
    driver.quit()

# Repeat the code 10 times
for _ in range(totalNum):
    run_script()