#!/usr/bin/python

import datetime
import httplib
import json
import re
import sys
import time
import urllib
import urllib2

from bs4 import BeautifulSoup

import beeminderpy
import settings



# Open user's CodeAcademy Profile
url = settings.CODEACADEMY_PROFILE
response = urllib2.urlopen(url)
webContent = response.read()

# Read the response into BeautifulSoup
soup = BeautifulSoup(webContent)

# Finds the User Achievements part of the profile page (there's probably a more elegant way to write this)
achiev = soup.find("div", {"id": "userAchievements"})
strong = achiev.em

# Removes the parantheses and gives number of achievements
numCode = re.sub(r'[^\w]', '', strong.string)
numCodeAcademy = int(numCode)
		
# Use beeminderpy wrapper to authenticate API
beeapi = beeminderpy.Beeminder(settings.BEEMINDER_AUTH_TOKEN)

# Get timestamp
timestamp = time.time()

# Create datapoint
result = beeapi.create_datapoint(settings.BEEMINDER_USERNAME,settings.BEEMINDER_GRAPH,timestamp,numCodeAcademy,'CodeAcademy Achievements','true')

if result:
    print "Success: Created datapoint"
else:
    print "Error: create_datapoint returned False"
