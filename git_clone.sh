#!/bin/bash

cd C:/My_space/Personal-cloud-repo/airflow-demo/

git status
sleep 4
echo "_________Adding files to git___________"
git add *
sleep 4
echo "___________commitng files to git_____________"
git commit -m "Thi is a test commit"
sleep 4
echo "________pushing files to git_________"
git remote add airflow git@github.com:amiteshQA/airflow-demo.git
sleep 4
git push airflow main