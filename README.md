beeacademy
==========

Scrapes achievements from Code Academy and updates beeminder graph (uses python library built by https://github.com/mattjoyce/beeminderpy)

Setup: Make sure you've got BeautifulSoup installed and that you've set up a custom beeminder graph #you're going to want it custom so you can change the graph to not auto sum.

1. Create a settings file (settings.py) via *cp settings.py.readme settings.py; $EDITOR settings.py*

2. Put in local env variables: 

3. Make a cron job to run beeacad.py once a day (or however often you'd like) to update your graph with your current total of achievements from codeacademy via *crontab -e*


TODO
====

* Add commandline paramaters to script

* Use ConfigParser
