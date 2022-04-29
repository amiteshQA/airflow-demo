#!/usr/bin/env bash


cd C:/My_space/Personal-cloud-repo/airflow-demo

git stash
#sleep 2
osascript echo "_________Taking the latest pull from main___________"
git pull origin main
#sleep 3
git stash apply
#sleep 2
osascript echo "_________Adding files to git___________"
git add .
#sleep 2
osascript echo "_________Checking status___________"
git status
#sleep 2
osascript echo "___________committing files to git_____________"
git commit -m "Pushing from the shell script"
#sleep 2
osascript echo "________pushing files to git_________"
git push origin main
#sleep 2
osascript echo "________Files has been pushed_________"
