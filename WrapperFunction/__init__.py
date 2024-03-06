import time
import fastapi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = fastapi.FastAPI()


@app.get("/")
def docs():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/test")
def chat():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://www.ubuntu.com/')
    response = driver.find_element(By.XPATH,"//body").text
    return {"data": response, "status": "success"}


