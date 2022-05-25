from abc import ABCMeta, abstractmethod
import requests
import pickle
import json


DEFAULT_METHOD_HOST = "https://mastodon.sdf.org"

#read here for more info: https://docs.joinmastodon.org/methods/apps/
class API_Entity(metaclass=ABCMeta):
    
    def api_method_host(self):
        return DEFAULT_METHOD_HOST

    @property
    @abstractmethod
    def api_method_path(self):
        pass

    #requests = requests

class API_Account(API_Entity):
    def __init__(id,username,acct,url,display_name,note,avatar,avatar_static,header,header_static,locked,emojis,discoverable,created_at,last_status_at,statuses_count):
        pass

class API_Activity(API_Entity):
    pass

class API_Announcement(API_Entity):
    pass

class API_AnnouncementReaction(API_Entity):
    pass

class API_Application(API_Entity):
    #POST: create a new application to obtain OAuth2 credentials
    #   params:
    #       client_name     - A name for your application
    #       redirect_uris   - Where the user should be redirected after authorization. To display the authorization code to the user instead of redirecting to a web page, use urn:ietf:wg:oauth:2.0:oob in this parameter
    #       scopes          - Space separated list of scopes. If none is provided, defaults to read (optional)
    #       website         - A URL to the homepage of your app (optional)
    def api_method_path(self):
        return "/api/v1/apps"
    
    #https://mastodon.example/api/v1/apps
    def __init__(self):
        try:
            with open("application.pkl", "rb") as f:
                self.cached = pickle.load(f)
        except Exception:
            payload = {'client_name':'baguette','redirect_uris':'urn:ietf:wg:oauth:2.0:oob'}
            session = requests.Session()
            response = session.post(self.api_method_host() + self.api_method_path(),data=payload)
            if response.status_code == 200:
                self.cached = json.loads(response.content)
            with open("application.pkl", "wb") as f:
                pickle.dump(self.cached, f)
        if not self.has_obtained_token():
            self.authenticate()
    
    def has_obtained_token(self):
        if hasattr(self,'token'):
            return True
        else:
            return False


    #get oauth token from /oauth/token
    def authenticate(self):
        self.token = API_Token('client_credentials',self.cached['client_id'],self.cached['client_secret'],'ietf:wg:oauth:2.0:oob')
        #self.verify_credentials()
        
    

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
    
    def api_method_path(self):
        return '/oauth/token'
        
    def verify(self):
        headers = {'Authorization':'Bearer '+ self.get_app_token()}
        session = requests.Session()
        response = session.get(self.api_method_host() + "/api/v1/apps/verify_credentials",headers=headers)
        if not response.status_code == 200:
            raise Exception("error, could not verify: code "+str(response.status_code))
    
    
    def __init__(self,grant_type, client_id, client_secret, redirect_uri, scope="read",code=None):
        try:
            with open("token.pkl", "rb") as f:
                self.cached = pickle.load(f)
                #print('token existed:'+str(self.cached))
        except Exception:
            print('creating token')
            
            payload = {
                'grant_type':grant_type,
                'client_id':client_id,
                'client_secret':client_secret,
                'redirect_url':redirect_uri,
                'scope':scope
            }
            if code:
                payload['code']=code
            
            session = requests.Session()
            response = session.post(self.api_method_host() + self.api_method_path(),data=payload)
            if response.status_code == 200:
                self.cached = json.loads(response.content)
                try:
                    self.verify()
                except Exception:
                    raise CouldNotVerifyException('test')
            else:
                raise Exception('could not get token')
        
        with open("token.pkl", "wb") as f:
            pickle.dump(self.cached, f)
            
    def get_app_token(self):
        return self.cached['access_token']

