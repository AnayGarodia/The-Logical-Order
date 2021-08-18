#! bin/bash
echo "Hell0 ,$(whoami)"
echo "RUNNING GIT EXECUTE FILE"
echo "$(git add .)"
echo "ENTER THE COMMIT MESSAGE :--"
read commitMessage
echo "$(git commit -m "$commitMessage")"
echo = "$(git pull)"
echo "$(git push)"
echo "FINISHED GIT PUSH"
echo "EXITING PROGRAM"
