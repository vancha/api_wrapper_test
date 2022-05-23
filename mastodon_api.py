import requests
import json
import pickle

#interact with this, the "base" of this entire api
class API_App(object):
    #store client_id and _secret in cache, as these will be used to obtain oauth tokens
    client_id       = ""
    client_secret   = ""

    #https://mastodon.example/api/v1/apps
    def __init__(name):
        try:
            #try and get an app from the cache
            #cached_app = pickle.load(open("apistate.pickle","rb"))
            pass
        except(OSError,IOError) as e:
            #it didn't exist, create it here
            pass
        

    def verify_credentials(self):
        pass


    class API_Entity(object):
        requests = requests
        def __init__():
            raise NotImplementedError("Please Implement this method")

    class API_Account(API_Entity):
        def __init__(id,username,acct,url,display_name,note,avatar,avatar_static,header,header_static,locked,emojis,discoverable,created_at,last_status_at,statuses_count):
            pass

    class API_Instance(API_Entity):
        def __init__(self, uri):
            self.uri = uri

        def get_public_timeline(self):
            public_timeline = requests.get(self.uri+"/api/v1/timelines/public/").json()
            return public_timeline

#only this code is relevant:
#creating a new instance
random_instance = API_App.API_Instance('https://mastodon.sdf.org')

#getting the instances public timeline
#print(random_instance.get_public_timeline())
