from instabot import Bot

my_bot = Bot()
my_bot.login(username="montre.satovi", password="Njuskica123")
user_id = my_bot.get_user_id_from_username("lego")
user_info = my_bot.get_user_info(user_id)
print(user_info['biography'])
