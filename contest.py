#  In the name of ALLAH
#  Author : Raashid Anwar

import json
import requests
import os
import subprocess

while True:
  print("Contest Id : ", end = "")
  contestId = input()
  res = requests.get('https://codeforces.com/api/contest.standings?contestId=' +  contestId + '&from=1&count=5&showUnofficial=true')
  if str(res) == '<Response [200]>':
    path = os.getcwd()
    os.mkdir(str(path) + '/CF/' +  str(contestId))
    os.chdir(str(path) + '/CF/' +  str(contestId))
    break
  else:
    print("Invalid Contest Id")


for data in res.json()['result']['problems']:
  with open(str(data['index']) + '.cpp', 'w') as files:
    for line in open(str(os.getenv("HOME"))+ '/template.cpp', 'r'):
       files.write(line)
  files.close()
  subprocess.Popen(['gedit', data['index'] + '.cpp'])
  print(data['index'] + '.cpp file is Created!')
  
os.system("pwd")
#os.system("/bin/bash")


