import unittest
import logging
from logging import FileHandler, Logger
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='web_test.log', encoding='utf-8', level=logging.INFO)

options = Options()
options.binary_location = r'C:\Users\kulau\AppData\Local\Mozilla Firefox\firefox.exe'

HOME_SITE="https://www.cathaybk.com.tw/cathaybk/"
HOME_SLOGAN="/html/body/div[1]/main/section/div[3]/div[1]/h1"
PRODUCTS="/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div"
CREDIT_CARD=r"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]"
CREDIT_CARD_DETAIL_MANU=r"/html/body/div[1]/main/article/div/div/div/div[1]/div/div"
STOPPED_CREDIT_CARD=r"/html/body/div[1]/main/article/section[6]/div"
STOPPED_CREDIT_CARD_LIST=f"{STOPPED_CREDIT_CARD}/div[2]/div/div/div"


class Test(unittest.TestCase):
            
    def setUp(self) -> None:
        
        self.driver = webdriver.Firefox(options=options, service=Service(executable_path="C:\\Users\\kulau\\Documents\\GitHub\\homeworks\\geckodriver.exe"))
        self.driver.get(HOME_SITE)
        self.wait = WebDriverWait(self.driver, 10)

        
    def test1(self):
        logging.info('test 1 starts')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "lnk_LogoLink"))
            )
            self.driver.save_screenshot("test1.png")
        except TimeoutException as e:
            logging.log("test 1 Fail", e.msg)
        finally:
            self.driver.quit()
        logging.info('test 1 ends')

    def test2(self):
        logging.info('test 2 starts')
        try:
            self.wait.until(
                    EC.presence_of_element_located((By.ID, "lnk_Link"))
                )
            self.wait.until(
                    EC.presence_of_element_located((By.XPATH, PRODUCTS))
                ).click()
            self.wait.until(
                    EC.presence_of_element_located((By.XPATH, CREDIT_CARD))
                )        
            self.credit_links = self.wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, f"{CREDIT_CARD}/following-sibling::div/a"))
                )
            print(f"credit links: {len(self.credit_links)} ")
            self.driver.save_screenshot("test2.png")
        finally:
            self.driver.quit()
        logging.info('test 2 ends')
    
    def test3(self):
        logging.info('test 3 starts')
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "lnk_Link"))
            )
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, PRODUCTS))
            ).click()
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, CREDIT_CARD))
            )        
            self.credit_links = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, f"{CREDIT_CARD}/following-sibling::div/a"))
            )
            self.credit_links[0].click()
            
            # 停發卡
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"{CREDIT_CARD_DETAIL_MANU}/a[6]/p"))
            ).click()
            self.stopped_credit_links =self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"{STOPPED_CREDIT_CARD}"))
            )
            self.stopped_credit_cards =self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, f"{STOPPED_CREDIT_CARD_LIST}"))
            )
            print(f"已停發卡數量: {len(self.stopped_credit_cards)}")
            self.driver.save_screenshot("test3.png")
        finally:
            self.driver.quit()
        logging.info('test 3 ends')

    def tearDown(self) -> None:
        self.driver.quit()
    


if __name__ == '__main__':
    unittest.main()