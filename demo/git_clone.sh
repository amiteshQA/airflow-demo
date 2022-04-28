#!/bin/bash

cd C:/Horizon/hackathon_amitesh/airflow-demo

echo "_________Taking the latest pull from main___________"
git pull origin main
# sleep 5
echo "_________Adding files to git___________"
git add *
# sleep 4
echo "_________Checking status___________"
git status
# sleep 4
echo "___________committing files to git_____________"
git commit -m "Pushing from the shell script"
# sleep 4
echo "________pushing files to git_________"
git push origin main
# sleep 4
echo "________Files has been pushed_________"
