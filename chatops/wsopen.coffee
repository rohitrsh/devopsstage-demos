module.exports = (robot) ->
#Open website you want
     robot.respond /ws open (.+)/i, (msg) ->
       webSite = msg.match[1]
       @exec = require('child_process').exec
       command = "/opt/stackstorm/chatops/scripts/wsopen.py \"#{webSite}\""

       @exec command, { shell: '/bin/bash' } , (error, stdout, stderr) ->
         msg.send stdout

#Check website acceessible or not
#     robot.respond /ws check (.+)/i, (msg) ->
#       webSite = msg.match[1]
#       @exec = require('child_process').exec
#       command = "/opt/stackstorm/chatops/scripts/wscheck.py \"#{webSite}\""
#
#       @exec command, { shell: '/bin/bash' } , (error, stdout, stderr) ->
#         msg.send stdout
