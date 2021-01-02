import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ftplib

nomevideo="cut.mp4"
corsi = os.listdir()

def carica_video(video):
    session = ftplib.FTP('ftp.online-training.it','4200647@aruba.it','Ocnarf123')
    file = open(nomevideo,'rb')  # file to send
    session.cwd('/www.online-training.it/softaculous/datadir/moodledata/repository/videoPESANTI')
    session.storbinary('STOR ./'+nomevideo, file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

# Using Chrome to access web
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
# Open the website
driver.get('https://www.online-training.it/moodle29/login/index.php')

# Find boxes
id_box = driver.find_element_by_id('username')
pass_box = driver.find_element_by_id('password')

#fill boxes
id_box.send_keys('admin')
pass_box.send_keys('Password123!')

# Find login button
login_button = driver.find_element_by_id('loginbtn')
# Click login
login_button.click()






#COURSE MANAGEMENT AND CREATION
#MODIFICARE IL CATEGORY ID!!!
driver.get('https://www.online-training.it/moodle29/course/edit.php?category=3&returnto=catmanage')
id_fullname = driver.find_element_by_id('id_fullname')
id_shortname = driver.find_element_by_id('id_shortname')
id_enddate_enabled = driver.find_element_by_id('id_enddate_enabled')
id_saveanddisplay = driver.find_element_by_id('id_saveanddisplay')

#fill boxes
#MODIFICARE!!!!
id_fullname.send_keys('NOME CORSO')
id_shortname.send_keys('SRTNM')
id_enddate_enabled.click()
id_saveanddisplay.click()






###ADD VIDEO
#driver.get('https://www.online-training.it/moodle29/course/view.php?id=7#section-1')
#currentURL =  driver.Url
###PARSARE URL!
id_corso="7"

driver.get('https://www.online-training.it/moodle29/course/view.php?id=7#section-1')

rotella = driver.find_element_by_id('action-menu-toggle-2')
webdriver.ActionChains(driver).move_to_element(rotella).click(rotella).perform()
modifica=driver.find_element_by_link_text('Attiva modifica')
modifica.click()
time.sleep(5)
#modifica=driver.find_element_by_link_text('Aggiungi una attività o una risorsa')
modifica=driver.find_element_by_xpath('(//*[@class="section-modchooser-text"])[2]')
webdriver.ActionChains(driver).move_to_element(modifica).click(modifica).perform()


id_item=driver.find_element_by_id('item_resource')
#id_item=driver.find_element_by_link_text('id_item_resource')
id_item.click()
submit_button = driver.find_element_by_name('submitbutton')
submit_button.click()

id_name=driver.find_element_by_id('id_name')
###MODIFICARE!!!
id_name.send_keys(nomevideo[:-4])
driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
driver.implicitly_wait(3) 
file_upload=driver.find_element_by_xpath('//*[@title="Aggiungi..."]')
file_upload.click()
#webdriver.ActionChains(driver).move_to_element(file_upload).click(file_upload).perform()
###MODIFICARE!!!
repo=driver.find_element_by_link_text('videoPESANTI')
repo.click()
video=driver.find_element_by_id('reposearch')
video.send_keys(nomevideo[:-4])
video.send_keys(Keys.RETURN)
video=driver.find_element_by_xpath('//*[@class="fp-filename-field"]')
video.click()


file_submit=driver.find_element_by_xpath('//*[@class="fp-select-confirm btn-primary btn"]')
file_submit.click()

finalmente=driver.find_element_by_id('id_submitbutton2')
finalmente.click()
