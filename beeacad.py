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

try:
    response = urllib2.urlopen(url)
except URLError:
    exit("Error: Cannot open URL {0}".format(url))
webContent = response.read()

# Read the response into BeautifulSoup
soup = BeautifulSoup(webContent)

# Finds the User Achievements part of the profile page (there's probably a more elegant way to write this)
achiev = soup.find("div", {"id": "userAchievements"})
if not achiev:
    exit("Error: Failed to extract number of achivements from HTML")
strong = achiev.em

# Removes the parantheses and gives number of achievements
numCode = re.sub(r'[^\w]', '', strong.string)
numCodeAcademy = int(numCode)
		
# Use beeminderpy wrapper to authenticate API
beeapi = beeminderpy.Beeminder(settings.BEEMINDER_AUTH_TOKEN)

# Use current time for datapoint
timestamp = time.time()

# Create datapoint
result = beeapi.create_datapoint(settings.BEEMINDER_USERNAME,settings.BEEMINDER_GRAPH,timestamp,numCodeAcademy,'CodeAcademy Achievements','true')

if result:
    print "Success: Created datapoint"
else:
    exit("Error: create_datapoint returned False")

