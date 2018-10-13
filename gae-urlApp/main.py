import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)
    print res
    res = json.dumps(res, indent=4)
    print "response"+(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "jc.url":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")

    env = parameters.get("jc-env")
    urls = parameters.get("jc-url")
   
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

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-envirnoment-url"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

