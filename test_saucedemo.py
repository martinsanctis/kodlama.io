from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_empty_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://saucedemo.com")
        sleep(2)
        loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required")
        sleep(60)

    def test_login_without_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://saucedemo.com")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("username")
        sleep(2)
        loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required")
        sleep(60)

    def test_locked_out_user_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://saucedemo.com")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"{errorMessage.text}")
        
        sleep(25)

    def test_close_error(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://saucedemo.com")
        # usernameInput = driver.find_element(By.ID, "user-name")
        # usernameInput.send_keys("asd")
        # passwordInput = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"{errorMessage.text}")
        loginButtonContainer = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        loginButtonContainer.click()
        sleep(10)
        #//*[@id="login_button_container"]/div/form/div[3]/h3/button/svg
    
    # def test_error_message(self):
    #     driver = webdriver.Chrome(ChromeDriverManager().install())
    #     errorMessage = driver.find_element(By.XPATH, self)
    #     print(f"{errorMessage.text}")

    def test_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://saucedemo.com")
        
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginButton.click()
        sleep(2)
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"{len(products)} adet ürün var")
        sleep(60)
        

testClass = Test_Sauce()
testClass.test_close_error()

# print(f"{errorMessage.text(Test_Sauce.test_empty_login)}")...

while True:
    continue
# /html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3