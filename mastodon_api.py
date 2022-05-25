#!/usr/bin/env python3

import pickle
from api_entities import *
from api_config import API_Configuration

#read here for more info: https://docs.joinmastodon.org/methods/apps/

#interact with this, the "base" of this entire api
class API_Base():

    def __init__(self):
        #The first thing we will need to do is to register an application, in order to be able to generate access tokens later
        application = API_Application()
        #if application.has_obtained_secret() and not application.has_obtained_token():
        #    application.authenticate()
        
    def get_public_timeline(self):
        pass

    def post_status(self):
        pass


#only this code is relevant:
api_base = API_Base()

#getting the instances public timeline
#print(random_instance.get_public_timeline())
