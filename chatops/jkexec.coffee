module.exports = (robot) ->
#Execute the job you want!
     robot.respond /jk exec (.+)/i, (msg) ->
       jobName = msg.match[1]
       @exec = require('child_process').exec
       command = "/opt/stackstorm/chatops/scripts/jkexec.sh \"#{jobName}\""

       @exec command, { shell: '/bin/bash' } , (error, stdout, stderr) ->
         msg.send stdout
