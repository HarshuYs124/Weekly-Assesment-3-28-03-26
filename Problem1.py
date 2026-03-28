from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
# holdes the browser
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

# launch browser
driver.get("https://www.shoppersstack.com/")

# maximize the window
driver.maximize_window()

# wait used for window not for find_element
driver.implicitly_wait(30)

# find the element and click it
ele=(driver.find_element(By.XPATH,"//img[@src='https://m.media-amazon.com/images/I/61BGE6iu4AL._AC_UY218_.jpg']"))
ele.click()

# used for explicit wait
wait=WebDriverWait(driver,10)

# Locate the delivery input field and entering the pincode
driver.find_element(By.ID,"Check Delivery").send_keys("302022")

# explicit wait used to wait until the check button is enabled
wait.until(EC.element_to_be_clickable((By.ID,"Check"))).click()

# closing the window
driver.quit()





