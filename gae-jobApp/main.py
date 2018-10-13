import os
import json
import random
from httplib import HTTPException
from urllib2 import HTTPError, URLError
from flask import Flask, jsonify, make_response, request
app = Flask(__name__)
log = app.logger
@app.route('/' , methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req))

    result = req.get("result")
    parameters = result.get("parameters")
    jobName = parameters.get("jobName")
    os.system('curl -k -X POST https://<jenkins url>/job/'+jobName+'/build --user username:password')
    res = makeWebhookResult(req)
    print res
    res = json.dumps(res, indent=4)
    print "response"+(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

webhookinput = (webhook)
print webhookinput

def makeWebhookResult(req):
    speech = "Great Job Executed Sucessfully"

#    result = req.get("result")
#    parameters = result.get("parameters")

#    job = parameters.get("jobName")


    print("Response:")
    print(speech)
#    print(job)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-jobexec"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    print "Starting app on port %d" % port
    app.run(debug=True, port=port, host='0.0.0.0')

