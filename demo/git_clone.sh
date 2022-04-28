#!/bin/bash

cd C:/My_space/Personal-cloud-repo/airflow-demo

echo "_________Taking the latest pull from main___________"
git pull origin main
sleep 3
echo "_________Adding files to git___________"
git add *
sleep 2
echo "_________Checking status___________"
git status
sleep 2
echo "___________committing files to git_____________"
git commit -m "Pushing from the shell script"
sleep 3
echo "________pushing files to git_________"
git push origin main
sleep 4
echo "________Files has been pushed_________"
