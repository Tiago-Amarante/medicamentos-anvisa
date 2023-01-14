from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class tools:
    def __init__(self,url):
        self.url = url

    def SiteInitiate(self, download_poth):
        options = Options()
        prefs = {'download.default_directory' : download_poth}
        options.headless = True
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\tadbc\anaconda3\chromedriver.exe',options=options)

    def OpenSite(self):
        self.driver.get(self.url)

    def ClickButton(self,Xpath):
        DownloadBtn = self.driver.find_element(By.XPATH, Xpath)
        DownloadBtn.click()