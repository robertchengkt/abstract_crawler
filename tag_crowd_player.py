from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://tagcrowd.com/")
driver.find_element_by_link_text("Upload File").click()
driver.find_element_by_name("showFreq").click()
driver.find_element_by_name("uploaded_file").send_keys("/Users/chengchang/Desktop/GettingStartedwiRODS4.1.pdf")
driver.find_element_by_link_text("Visualize!")


# driver.find_element_by_('body').send_keys(Keys.COMMAND + 't')


