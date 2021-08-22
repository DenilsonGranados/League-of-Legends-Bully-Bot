from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Send_email import send_email
import time

#### 120 secs
# PATH= 'D:\Coding\chromedriver.exe'
# driver=webdriver.Chrome(PATH) ## Old way maybe try below way due to version issues
target_player= input("Target's player name>> ") ##"Glendyr"
target_email= input("Target's email>> ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://na.op.gg/summoner/userName="+ target_player)

data= driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[5]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div')
date_pc= 1234 #data.get_attribute('data-game-time')
date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(date_pc)))
result= driver.find_element_by_class_name('GameResult')
action=ActionChains(driver)

while True:
    driver.implicitly_wait(5)
    button=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/button')
    action.click(button).perform()
    loop_date=  driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[5]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div').get_attribute('data-game-time')
    loop_results= driver.find_element_by_class_name('GameResult').text
    if loop_date!= date_pc and loop_results!= result: 
        date_pc= loop_date
        champ= driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[5]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[4]/a').text
        PATH= 'D:\Coding\chromedriver.exe'
        # tube=webdriver.Chrome(PATH) ### Same as in line 12
        tube=webdriver.Chrome(ChromeDriverManager().install())
        tube.get("https://www.youtube.com/")
        search= tube.find_element_by_id("search")
        search.send_keys(champ+' guide')
        search.send_keys(Keys.RETURN)
        tube.implicitly_wait(2)
        link_hold= tube.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
        link1= link_hold.get_attribute('href')
        link2=tube.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/ytd-thumbnail/a').get_attribute('href')
        content= ' Wow you really suck at '+champ+'\n Here try watching these '+link1+'\n '+ link2 
        send_email(target_email, 'You suck at League', content)
    else:
        print('tested')
    time.sleep(120)
    driver.refresh()
        
