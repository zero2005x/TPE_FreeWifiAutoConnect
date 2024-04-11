import logging
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


# 設定日誌級別為DEBUG來獲取詳細信息
# Set the logging level to DEBUG to get detailed information
logging.basicConfig(level=logging.DEBUG)

# 初始化Tkinter，但不顯示主窗口
# Initialize Tkinter, but do not display the main window
Tk().withdraw()

# 函數檢查文件是否存在且正確
# Function to check if the file exists and is correct
def select_file(prompt, initialdir, filetypes):
    path = askopenfilename(title=prompt, initialdir=initialdir, filetypes=filetypes)
    if path:
        return path
    else:
        logging.error("File selection cancelled.")
        exit()

# 指定geckodriver WebDriver路徑
# Specify the geckodriver WebDriver path
geckodriver_path = r"C:\Users\liangtinglin\Documents\python\TaipeiWifiAutoConnect\geckodriver.exe"  # 替換為你的geckodriver的實際路徑
                                                                                  # Replace with your actual geckodriver path
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # 替換為你的Firefox瀏覽器的實際路徑
                                                                       # Replace with your actual Firefox browser path

# 檢查文件是否存在和正確
# Check if the files exist and are correct
if not os.path.isfile(geckodriver_path) or not "geckodriver.exe" in geckodriver_path:
    logging.warning("Invalid or missing geckodriver. Please select geckodriver.exe.")
    geckodriver_path = select_file("Select geckodriver.exe", "/", [("Executable", "*.exe")])

if not os.path.isfile(firefox_binary_path) or not "firefox.exe" in firefox_binary_path:
    logging.warning("Invalid or missing Firefox binary. Please select firefox.exe.")
    firefox_binary_path = select_file("Select firefox.exe", "/", [("Executable", "*.exe")])

service = FirefoxService(executable_path=geckodriver_path)

# 設置Selenium Webdriver的選項
# Set the Selenium Webdriver options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # 無頭模式
                                    # Headless mode
options.binary_location = firefox_binary_path  # 指定Firefox二進制路徑
                                                # Specify Firefox binary path

# 使用指定的Service
# Use the specified Service
driver = webdriver.Firefox(service=service, options=options)

try:
    # 访问台北公共Wi-Fi的正确登入页面
    # Access the correct login page for Taipei Public Wi-Fi
    driver.get("https://portal.tpefree.taifo.taipei/loginOut.aspx")
    logging.info("访问台北公共Wi-Fi登入页面")

    # 等待並點擊同意條款並開始上網的按鈕。若按鈕的ID发生变化，需要相应调整
    # Wait and click the button to agree to the terms and start surfing. If the button's ID has changed, it needs to be adjusted accordingly
    agree_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnContinue"))
    )
    agree_button.click()
    logging.info("已點擊同意條款並開始上網按鈕")

except TimeoutException:
    logging.error("在等待同意按鈕時發生超時")
except WebDriverException as e:
    logging.error(f"WebDriver异常: {e}")
finally:
    # 确保最后关闭浏览器，避免留下未关闭的进程
    driver.quit()