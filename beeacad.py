#!/usr/bin/python
import urllib
import urllib2
import re

import beeminderpy
import settings
import httplib
import json
import sys
import time
import datetime

from bs4 import BeautifulSoup

#Opens your CodeAcademy Profile
url = settings.CODEACADEMY_PROFILE
response = urllib2.urlopen(url)
webContent = response.read()

#Reads the response into BeautifulSoup
soup = BeautifulSoup(webContent)

#Finds the User Achievements part of the profile page (there's probably a more elegant way to write this)
achiev = soup.find("div", {"id": "userAchievements"})
strong = achiev.em

#Removes the parantheses and gives number of achievements
numCode = re.sub(r'[^\w]', '', strong.string)
numCodeAcademy = int(numCode)
		
#Using beeminderpy wrapper, authenticate api
beeapi=beeminderpy.Beeminder(settings.BEEMINDER_AUTH_TOKEN)

#get timestamp
timestamp = time.time()

#Create Datapoint
beeapi.create_datapoint(settings.BEEMINDER_USERNAME,settings.BEEMINDER_GRAPH,timestamp,numCodeAcademy,'CodeAcademy Achievements','true')
print "Created Datapoint"
