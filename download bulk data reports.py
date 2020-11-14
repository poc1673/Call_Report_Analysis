# Steps to initiating data dowanload:

# [1] Set up the browser
# [2] Move the browser to the appropriate part o the FFIEC website here: https://cdr.ffiec.gov/public/ManageFacsimiles.aspx
# [3] Select "Call" as report type.
# [4] Select" Unique Identifier"; put in unique RSSD; Example is 924405
# [5] Hit "Search"
# [6] Hit "Download" icon
# [7] Select SemiColon Delimited File; Download it.
# [8] Name the file with this format: RSSD_YYYY-MM-DD



date_list = ["09/30/2020","06/30/2020","03/31/2020","12/31/2019","09/30/2019","06/30/2019","03/31/2019","12/31/2018","09/30/2018","06/30/2018","03/31/2018","12/31/2017","09/30/2017","06/30/2017","03/31/2017","12/31/2016","09/30/2016","06/30/2016","03/31/2016","12/31/2015","09/30/2015","06/30/2015","03/31/2015","12/31/2014","09/30/2014","06/30/2014","03/31/2014","12/31/2013","09/30/2013","06/30/2013","03/31/2013","12/31/2012","09/30/2012","06/30/2012","03/31/2012","12/31/2011","09/30/2011","06/30/2011","03/31/2011","12/31/2010","09/30/2010","06/30/2010","03/31/2010","12/31/2009","09/30/2009","06/30/2009","03/31/2009","12/31/2008","09/30/2008","06/30/2008","03/31/2008","12/31/2007","09/30/2007","06/30/2007","03/31/2007","12/31/2006","09/30/2006","06/30/2006","03/31/2006","12/31/2005","09/30/2005","06/30/2005","03/31/2005","12/31/2004","09/30/2004","06/30/2004","03/31/2004","12/31/2003","09/30/2003","06/30/2003","03/31/2003","12/31/2002","09/30/2002","06/30/2002","03/31/2002","12/31/2001","09/30/2001","06/30/2001","03/31/2001"]

from selenium import webdriver
import re
import os
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches",[ "disable-popup-blocking"])
 

def get_bulk_reports(date):
    try:
        driver = webdriver.Chrome(    )
        driver.get("https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx")
        
        rpt_tbl = driver.find_element_by_name("ctl00$MainContentHolder$ListBox1")
        rpt_tbl.send_keys("Call Reports -- Single Period")
        
        
        dt_tbl = driver.find_element_by_name("ctl00$MainContentHolder$DatesDropDownList")
        dt_tbl.send_keys(date)
        
        driver.find_element_by_name("ctl00$MainContentHolder$TabStrip1$Download_0").click()
        sleep(1)
        driver.quit()

    except Exception:
        pass
    
[get_bulk_reports(x) for x in date_list]