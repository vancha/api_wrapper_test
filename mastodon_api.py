import requests
import json
import pickle
from abc import ABCMeta, abstractmethod



#read here for more info: https://docs.joinmastodon.org/methods/apps/




#interact with this, the "base" of this entire api
class API_Base(metaclass=ABCMeta):


    def __init__(self):
        #The first thing we will need to do is to register an application, in order to be able to generate access tokens later
        pass

    class API_Entity(object):
        @property
        @abstractmethod
        def api_method_host(self):
            pass

        @property
        @abstractmethod
        def api_method_path(self):
            pass

        requests = requests
        def __init__():
            raise NotImplementedError("Please Implement this method")

        def create_from_api():
            raise NotImplementedError("Please Implement this method")

    class API_Account(API_Entity):
        def __init__(id,username,acct,url,display_name,note,avatar,avatar_static,header,header_static,locked,emojis,discoverable,created_at,last_status_at,statuses_count):
            pass

    class API_Activity(API_Entity):
        pass

    class API_Announcement(API_Entity):
        pass

    class API_AnnouncementReaction(API_Entity):
        pass

    #required to create OAuth2 credentials
    class API_Application(API_Entity):
        #required attributes
        name            = ""

        #optional attributes
        website         = ""
        vapid_key       = ""

        #client attributes
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

    class API_Attachment(API_Entity):
        pass

    class API_Card(API_Entity):
        pass

    class API_Context(API_Entity):
        pass

    class API_Conversation(API_Entity):
        pass

    class API_Emoji(API_Entity):
        pass

    class API_Error(API_Entity):
        pass

    class API_FeaturedTag(API_Entity):
        pass

    class API_Field(API_Entity):
        pass

    class API_Filter(API_Entity):
        pass

    class API_History(API_Entity):
        pass

    class API_IdentityProof(API_Entity):
        pass

    class API_Instance(API_Entity):
        def __init__(self, uri):
            self.uri = uri

        def get_public_timeline(self):
            public_timeline = requests.get(self.uri+"/api/v1/timelines/public/").json()
            return public_timeline

    class API_List(API_Entity):
        pass

    class API_Marker(API_Entity):
        pass

    class API_Mention(API_Entity):
        pass

    class API_Notification(API_Entity):
        pass

    class API_Poll(API_Entity):
        pass

    class API_Preferences(API_Entity):
        pass

    class API_PushSubscription(API_Entity):
        pass

    class API_Relationship(API_Entity):
        pass

    class API_Report(API_Entity):
        pass

    class API_Results(API_Entity):
        pass

    class API_ScheduledStatus(API_Entity):
        pass

    class API_Source(API_Entity):
        pass

    class API_Tag(API_Entity):
        pass

    class API_Token(API_Entity):
        pass



#only this code is relevant:
api_base = API_Base()

#getting the instances public timeline
#print(random_instance.get_public_timeline())
