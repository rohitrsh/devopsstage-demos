module.exports = (robot) ->
#Execute the job you want!
     robot.respond /url (.+) (.+)/i, (msg) ->
       jcEnv = msg.match[1]
       jcUrl = msg.match[2]
       @exec = require('child_process').exec
       command = "/opt/stackstorm/chatops/scripts/url.py \"#{jcEnv}\" \"#{jcUrl}\""

       @exec command, { shell: '/bin/bash' } , (error, stdout, stderr) ->
         msg.send stdout
