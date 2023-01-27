from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = '/home/mirenko/Downloads/Compressed/chromedriver_linux64/chromedriver' 

def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

#Open Website

browser = create_webdriver()
browser.get('https://github.com/collections/machine-learning')

# Extract all project
projects = browser.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")

# Extract information for each project
projectList = {}
for proj in projects:
    projName = proj.text 
    projUrl = proj.find_elements_by_xpath('a')[0].get_attribute('href') 
    projectList[projName] = projUrl

browser.quit()

projectDf = pd.DataFrame.from_dict(projectList, orient = 'index')

projectDf['projectName'] = projectDf.index
projectDf.columns = ['projectUrl', 'projectName']
projectDf = projectDf.reset_index(drop=True)

projectDf.to_csv('projectList.csv')

