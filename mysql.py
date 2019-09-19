import _mysql


# make the connection 
db =_mysql.connect(host="172.104.189.102" , user ="remote_user" , port=3306,passwd="myPassw0rd_01",db="twitter")

# add the tweet method

def add_tweets(tweet_arr) :
    counter = 1 
    for tweet in tweet_arr:
        
        query_text  = """INSERT INTO tweet (id, text, user_id, user_screen_name, user_name, created_at, retweets, likes, replies, profile_pic) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format( int(tweet['tweet_id']) , str(tweet['text']).replace("'",'') ,  int(tweet['user_id']), tweet['user_screen_name'], tweet['user_name'], int(tweet['created_at']), int(tweet['retweets']) , int(tweet['likes']), int(tweet['replies']) , tweet['profile_pic'] )
        db.query( query_text )

        print("tweet {}  added".format(str(counter)) )
        counter += 1


def check_if_tweet_exists(time):
    query_text = """SELECT COUNT(*) FROM tweet WHERE created_at = {};""".format(str(time))
    db.query( query_text )
    count = db.store_result().fetch_row()
    result = int(count[0][0])
    if result == 1 :
        return True
    elif result == 0 :
        return False
    else :
        print("passed")
        
#check_if_tweet_exists(1539338621000) 