import tweepy, csv
from credentials import consumer_key, consumer_secret, access_token_secret, access_token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
i = 1
user = input("Enter user_id:\n")
with open(user+".csv", "w", newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "id", "Created", "Tweet", "Likes", "Retweet Count", "lang"])
for status in tweepy.Cursor(api.user_timeline, id = user).items():
    writer.writerow([str(i), status.id_str, str(status.created_at), status.text, status.favorite_count, status.retweet_count, status.lang])
    

