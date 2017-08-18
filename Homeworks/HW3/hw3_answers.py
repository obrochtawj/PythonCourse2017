#Homework 3
#William O'Brochta

#There won't be many GitHub commits of this homework because the authorization keys need to be deleted before commiting.

#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time
import operator

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')    
#Make the API wait when the rate limit is reached.
api = tweepy.API(auth, wait_on_rate_limit=True)


#See rate limit
api.rate_limit_status()

#Look at Patrick's followers
patrick= api.get_user('patrickrickert')
#Get all their names
patrick_followers=api.followers(patrick.id,count=200)

#Use their names to get all their information.
people_follow=0
patrick_popular={}
while people_follow < len(patrick_followers):
    try:
        patrick_screen_name=patrick_followers[people_follow].screen_name
        new_follower=api.get_user(patrick_followers[people_follow].id)
        patrick_popular[patrick_screen_name]=new_follower
        people_follow+=1
    except:
        time.sleep(1)

#Follower with the most number of followers
people_following={}
#For all the names in the list of follower's information
for patrick_screen_name in patrick_popular:
    #Get their followers count
    people_follow_count=patrick_popular[patrick_screen_name].followers_count
    #Put it in a dictionary with name and number of followers
    people_following[patrick_screen_name]=people_follow_count
#Find the follower with the greatest number of followers.
max(people_following.items(), key=lambda k: k[1])
#Best_Food_Porn has 109747 followers

#Most active follower (greatest number of total tweets)
people_statuses={}
for patrick_screen_name in patrick_popular:
    people_statuses_count=patrick_popular[patrick_screen_name].statuses_count
    people_statuses[patrick_screen_name]=people_statuses_count
max(people_statuses.items(), key=lambda k: k[1])
#Simonwillo has tweeted 54273 times.

#Look at Patrick's friends
patrick_friends=api.friends(patrick.id,count=200)

#Same process as before for all this code.
people_friends=0
patrick_friends_list={}
while people_friends < len(patrick_friends):
    try:
        patrick_screen_name=patrick_friends[people_friends].screen_name
        new_follower=api.get_user(patrick_friends[people_friends].id)
        patrick_friends_list[patrick_screen_name]=new_follower
        people_friends+=1
    except:
        time.sleep(1)

people_friends={}
for patrick_screen_name in patrick_friends_list:
    people_followers_count=patrick_friends_list[patrick_screen_name].followers_count
    people_friends[patrick_screen_name]=people_followers_count

#Split up friends into categories. Create empty lists for the categories.
layman_people=[]
expert_people=[]
celebrity_people=[]
#Create list of friends sorted by number of followers
sorted_friends = sorted(people_friends, key=lambda x: people_friends[x])
#Create a loop to put the friends into categories based on number of followers.
for k in sorted_friends:
    if people_friends[k]<100:
        layman_people.append(k)
    elif 99 < people_friends[k] <1000:
        expert_people.append(k)
    else:
        celebrity_people.append(k)

#Create list of friends with fewer than 1000 followers.
layexpert_people=[]
for k in sorted_friends:
    if people_friends[k]<1000:
        layexpert_people.append(k)

#Create dictionary with friend's name in its category and display number of followers.
layman_friends=dict((k,patrick_friends_list[k]) for k in layman_people)
expert_friends=dict((k,patrick_friends_list[k]) for k in expert_people)
celebrity_friends=dict((k,patrick_friends_list[k]) for k in celebrity_people)

#Find layman friend with most tweets.
layman_statuses={}
for patrick_screen_name in layman_friends:
    people_statuses_count=layman_friends[patrick_screen_name].statuses_count
    layman_statuses[patrick_screen_name]=people_statuses_count
#Layman friend with most tweets
max(layman_statuses.items(), key=lambda k: k[1])
#Haleybpritchard has tweeted 1634 times.

expert_statuses={}
for patrick_screen_name in expert_friends:
    people_statuses_count=expert_friends[patrick_screen_name].statuses_count
    expert_statuses[patrick_screen_name]=people_statuses_count
#Expert friend with most tweets
max(expert_statuses.items(), key=lambda k: k[1])
#LucyRose193 has tweeted 18221 times.

celebrity_statuses={}
for patrick_screen_name in celebrity_friends:
    people_statuses_count=celebrity_friends[patrick_screen_name].statuses_count
    celebrity_statuses[patrick_screen_name]=people_statuses_count
#Celebrity friend with most tweets
max(celebrity_statuses.items(), key=lambda k: k[1])
#MaraWilson has tweeted 95150 times.

#Celebrity friend with most followers
celebrity_followers={}
for patrick_screen_name in celebrity_friends:
    people_follow_count=celebrity_friends[patrick_screen_name].followers_count
    celebrity_followers[patrick_screen_name]=people_follow_count
max(celebrity_followers.items(), key=lambda k: k[1])
#President Obama has 93507297 followers.

#Most tweets of any follower and their followers
#Sort followers into categories like was done previously for friends.
sorted_followers = sorted(people_following, key=lambda x: people_following[x])
layexpert_followers=[]
for k in sorted_followers:
    if people_following[k]<1000:
        layexpert_followers.append(k)

#Do not run the code that follows. Doing so takes many hours!!
#Most tweets of any followers and their followers
for name_follow in layexpert_followers:
    #Go to each follower
    following=api.followers_ids(name_follow)
    most_tweets=0
    iterator=0
    #For each follower's followers:
    while iterator<len(following):
        try:
            #Get that follower's information
            user=api.get_user(following[iterator])
            #Pull out their number of tweets.
            statuses_count=user.statuses_count
            #If number of tweets is more than the previous highest,
            #store that value and name.
            if most_tweets < statuses_count:
                most_tweets=statuses_count
                most_tweets_user=str(user.name)
            #Go to next follower.
            iterator+=1
            #Sleep so that there's rate limit error.
            time.sleep(65)
        #Ignore followers with locked profiles.
        except tweepy.TweepError:
            print "Continue."
        #If something happens, continue waiting until the rate limit is reset.
        except:
            time.sleep(65)

most_tweets
most_tweets_user
#Kat Robinson has tweeted 27817 times.


#Most tweets of any friends and their friends
for name_follow in layexpert_people:
    following=api.friends_ids(name_follow)
    most_tweets=0
    iterator=0
    while iterator<len(following):
        try:
            user=api.get_user(following[iterator])
            statuses_count=user.statuses_count
            if most_tweets < statuses_count:
                most_tweets=statuses_count
                most_tweets_user=str(user.name)
            iterator+=1
            time.sleep(5)
        except tweepy.TweepError:
            print "Continue."
        except:
            time.sleep(65)

most_tweets
most_tweets_user
#The Independent tweeted 588987 times.
