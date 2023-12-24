from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from secrets import instagram_username, instagram_password

bot = webdriver.Firefox()
def login():
    bot.get('https://www.instagram.com/')
    time.sleep(3)
    #Inspect in console input fields and then copy XPath
    username = bot.find_element(By.CSS_SELECTOR, 'div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    password = bot.find_element(By.CSS_SELECTOR, 'div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    submit_button = bot.find_element(By.CSS_SELECTOR, '._acap')
    username.send_keys(instagram_username)
    password.send_keys(instagram_password)
    submit_button.click()
    # password.send_keys(Keys.RETURN)
    time.sleep(10)
    
def like_posts(hashtags):
    for hashtag in hashtags:
        bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        # Scroll down to load more posts
        bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # Find all post links
        parent = bot.find_element(By.CSS_SELECTOR, '._aaq8 > div:nth-child(2) > div:nth-child(1)')  #it is the lower element which contains all posts 
        posts = parent.find_elements(By.CSS_SELECTOR, '._ac7v > ._aabd') #_ac7v is row element, then select all posts inside that row (3 of them). By this we select all posts
        links = []
        for post in posts:
            link = post.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(link)
        for link in links:
            try:
                if link:
                    bot.get(link)
                    time.sleep(5)
                    try:
                        like_button = bot.find_element(By.CLASS_NAME, 'xp7jhwk') #class name of like button
                        like_button.click()
                        time.sleep(10)
                    except Exception as ex:
                        print(f"Error liking post: {ex}")
                        bot.close()
            except Exception as ex:
                print(f"Error extracting link: {ex}")
                bot.close()
#Execute functions
login()
like_posts(["animals", "nature", "lake", "sea", "beach", "mountin", "sunrise", "sky", "sun", "animals", "dogs", "cats", "naturephotography"])

