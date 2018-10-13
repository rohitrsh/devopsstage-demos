#!/usr/bin/env python
import json
import os
import sys

env = sys.argv[1]
urls = sys.argv[2]



def urlResult(env,urls):
#    env = jc-env
#    urls = jc-url

    devUrl = {'kibana':'dev-kibana.test.com','mq':'dev-mq.test.com','db':'dev-db.test.com','api':'dev-api.test.com','www':'dev-www.test.com'}
    sitUrl = {'kibana':'sit-kibana.test.com','mq':'sit-mq.test.com','db':'sit-db.test.com','api':'sit-api.test.com','www':'sit-www.test.com'}
    stgUrl = {'kibana':'stage-kibana.test.com','mq':'stage-mq.test.com','db':'stage-db.test.com','api':'stage-api.test.com','www':'stage-www.test.com'}
    ppUrl = {'kibana':'pp-kibana.test.com','mq':'pp-mq.test.com','db':'pp-db.test.com','api':'pp-api.test.com','www':'pp-www.test.com'}
    pdUrl = {'kibana':'kibana.test.com','mq':'mq.test.com','db':'db.test.com','api':'pi.test.com','www':'www.test.com'}

    if (env == "dev"):
        speech = "The url of " + urls + " is " + devUrl[urls] + "."
    elif (env == "sit"):
        speech = "The url of " + urls + " is " + sitUrl[urls] + "."
    elif (env == "stage"):
        speech = "The url of " + urls + " is " + sitUrl[urls] + "."
    elif (env == "preprod"):
       speech = "The url of " + urls + " is " + ppUrl[urls] + "."
    elif (env == "prod"):
       speech = "The url of " + urls + " is " + pdUrl[urls] + "."
    else:
       print "No env found"

    print("*Here you go!*")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-jiocloud-envirnoment-url"
    }

urlResult(env,urls)
