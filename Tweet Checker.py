tweet = input("Enter your tweet here: ")
tweet_checker = len(tweet)
tweet_limit = 140

if tweet_checker <= tweet_limit:
    print(f"Length of tweet ({tweet_checker} characters) is acceptable.")
else:
    print(f"Length of tweet ({tweet_checker} characters) is unacceptable. It is {tweet_checker - tweet_limit} characters too long.")