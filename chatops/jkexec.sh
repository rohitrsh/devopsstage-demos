#!/bin/bash
jobName=$1

jobExec () {
	curl -k -X POST -s https://<jenkins URL>/job/$jobName/build --user username:password
}

if jobExec == 0; then
	echo "Job Executed Suvessfully"
else
	echo "Job Execution Faled"
fi
