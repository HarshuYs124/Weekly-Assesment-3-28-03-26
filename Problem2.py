from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
o = ChromeOptions()
# holdes the browser
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

# launch browser
driver.get("https://www.myntra.com/")
driver.maximize_window()

# explicit wait
wait=WebDriverWait(driver, 15)
#locating genz catagory
genz = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Genz')]")))

actions=ActionChains(driver)
# hover on genz
actions.move_to_element(genz).pause(3).perform()

# locating the jackets
jacket=wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Jackets Under ₹899')]")))
jacket.click()

# locating and selecting filter 1
driver.find_element(By.XPATH, "//label[contains(.,'glitchez')]").click()
sleep(2)
# locating nad selecting filter 2
driver.find_element(By.XPATH, "//label[contains(.,'Black')]").click()

# locating sortby
sort=driver.find_element(By.XPATH, '//div[@class="sort-sortBy"]')

# hover sortby
actions.move_to_element(sort).pause(2).perform()
# clicking Popularity
driver.find_element(By.XPATH, "//label[contains(text(),'Popularity')]").click()
sleep(3)
# choosing the product
driver.find_element(By.XPATH, "(//li[contains(@class,'product-base')])[1]").click()
sleep(3)
# switch window
driver.switch_to.window(driver.window_handles[1])
# select size
driver.find_element(By.XPATH, "//p[contains(@class,'size-buttons-unified-size')]").click()
# click add to bag
driver.find_element(By.XPATH, "//div[contains(text(),'ADD TO BAG')]").click()

# close window
driver.quit()



