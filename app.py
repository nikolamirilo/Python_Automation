from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from secrets import instagram_username, instagram_password

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        #Inspect in console input fields and then copy XPath
        email = bot.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        password = bot.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        submit_button = bot.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        email.send_keys(self.username)
        password.send_keys(self.password)
        submit_button.click()
        # password.send_keys(Keys.RETURN)
        time.sleep(10)
    
    def like_posts(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        # Scroll down to load more posts
        bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        
        # Find all post links
        parent = bot.find_element(By.CSS_SELECTOR, '._ac7v')
        posts = parent.find_elements(By.CSS_SELECTOR, '._aabd')
        for post in posts:
            try:
                link = post.find_element(By.TAG_NAME, 'a').get_attribute('href')
                if link:
                    bot.get(link)
                    time.sleep(5)
                    try:
                        like_button = bot.find_element(By.CLASS_NAME, 'xp7jhwk')
                        like_button.click()
                        time.sleep(10)
                    except Exception as ex:
                        print(f"Error liking post: {ex}")
                        time.sleep(60)
            except Exception as ex:
                print(f"Error extracting link: {ex}")
                time.sleep(2)
bot = InstagramBot(instagram_username, instagram_password)
bot.login()
bot.like_posts('nature')

