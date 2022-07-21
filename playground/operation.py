import string
from matplotlib.font_manager import json_dump
import tweepy
import json



class Operation:

 

  # def __init__(self, name, age):
  #   self.name = name
  #   self.age = age

  def verify_tweepy():

    consumer_key = "87FQgnWW9fIqO9uLM5DORZEPw"
    consumer_secret = "4yuffhs4hRZgSHXuejTuiTeqm1L8KNkhaSp6JTzciTiPx955YP"
    access_token = "1535624558551523329-jveJ6nj9cM17gNI72oHtkckuEIap75"
    access_token_secret = "kcCpbzx3iWBf9ttskcEv8qg2KNqakO7uM72uBzhLUXzuX"
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth) 



    try:
        
        
        return "Everything works"
        
    except:
        return "Somrthing went wrong"



  def getObject():

    consumer_key = "87FQgnWW9fIqO9uLM5DORZEPw"
    consumer_secret = "4yuffhs4hRZgSHXuejTuiTeqm1L8KNkhaSp6JTzciTiPx955YP"
    access_token = "1535624558551523329-jveJ6nj9cM17gNI72oHtkckuEIap75"
    access_token_secret = "kcCpbzx3iWBf9ttskcEv8qg2KNqakO7uM72uBzhLUXzuX"
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth) 



    return api


  def getUser(api, name = "default"):
    me = api.verify_credentials()

    if(name == "default"):
        name = me.screen_name


    user = api.get_user(screen_name=name)
    ground_level_following = []

    
    
    for friend in user.friends():
      ground_level_following.append(friend.screen_name)

    

    return user


  # def temptemp(verifiedObject, name = "default"):
    
    

