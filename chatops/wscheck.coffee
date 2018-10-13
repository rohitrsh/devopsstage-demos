module.exports = (robot) ->
#Check website acceessible or not
     robot.respond /ws check (.+)/i, (msg) ->
       webSite = msg.match[1]
       @exec = require('child_process').exec
       command = "/wscheckupl/wscheck.py \"#{webSite}\""

       @exec command, { shell: '/bin/bash' } , (error, stdout, stderr) ->
         msg.send stdout
