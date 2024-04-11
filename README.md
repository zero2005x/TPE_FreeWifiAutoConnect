# Taipei Public Wi-Fi Auto Connect

## 簡介 / Introduction

此Python腳本旨在自動連接到台北公共Wi-Fi，幫助使用者免去手動選擇並連接Wi-Fi的麻煩。腳本使用Selenium Webdriver自動化網頁互動，自動完成登入頁面的同意條款操作，從而實現自動連接。

This Python script is designed to automate the process of connecting to Taipei Public Wi-Fi, sparing users the hassle of manually selecting and connecting to Wi-Fi. The script automates web interactions using the Selenium Webdriver, automatically agreeing to terms on the login page, thus achieving auto-connection.

## 環境需求 / Environment Requirements

- Python 3
- Selenium
- WebDriver (Geckodriver for Firefox or Chromedriver for Chrome)
- Firefox 或 Chrome 瀏覽器 / Firefox or Chrome browser

## 安裝 / Installation

1. 確保已安裝Python 3。
   Ensure Python 3 is installed.

2. 安裝Selenium庫：
   Install the Selenium library:

   ```bash
   pip install selenium
   ```

3. 下載對應的WebDriver並放置於可執行路徑中。下載連結：
   Download the corresponding WebDriver and place it in an executable path. Download links:

   - Firefox (Geckodriver): https://github.com/mozilla/geckodriver/releases
   - Chrome (Chromedriver): https://sites.google.com/a/chromium.org/chromedriver/

## 使用說明 / Usage

1. 修改腳本中的`geckodriver_path`和`firefox_binary_path`變量，以匹配您的Geckodriver路徑和Firefox安裝路徑。對於Chrome用戶，需將相關代碼改為使用Chromedriver和Chrome的路徑。
   
   Modify the `geckodriver_path` and `firefox_binary_path` variables in the script to match your Geckodriver path and Firefox installation path. For Chrome users, change the relevant code to use Chromedriver and Chrome's path.

2. 在終端機或命令提示符中運行腳本：
   
   Run the script in a terminal or command prompt:

   ```bash
   python TPE_FreeWifiAutoConnect.py
   ```

## 注意事項 / Notes

- 腳本默認設置為無頭模式，不會顯示瀏覽器界面。您可以通過註釋掉`options.add_argument('--headless')`行來禁用無頭模式。
  
  The script is set to headless mode by default, not displaying the browser interface. You can disable headless mode by commenting out the `options.add_argument('--headless')` line.

- 確保您的電腦連接到台北公共Wi-Fi的範圍內才能正常使用此腳本。
  
  Ensure your computer is within the range of Taipei Public Wi-Fi for the script to work properly.

## 貢獻 / Contributing

歡迎提交Pull Request來改進此腳本。請確保您的代碼清晰且有適當的註釋。

Contributions to improve this script are welcome. Please ensure your code is clean and well-commented.