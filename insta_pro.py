#from instabot we will follow someone's account with our account.

from instabot import Bot

bot = Bot()
bot.login(username= "Your_username", password= "Your_password")
bot.follow('lavisha.gurwani')

#upload photo in insta with caption
bot.upload_photo('C:/users/preeti/Dekstop/python.jpg', caption="i love python")

#unfollow the account
bot.unfollow(username='users_account')

#text the same msg to multiple accounts
bot.send_message("I love python", ['soorya_username', '2nd_username', '3rd username'])

#get info of users that follows you
followers = bot.get_user_followers('preetigurwani')

for follower in followers:
    print(bot.get_user_info(follower))    #now it will give us all followers info in list form  

#now take info of users we follow means followings
followings = bot.get_user_following('preetigurwani')
for following in followings:
    print(bot.get_user_info(following))