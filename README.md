# malwrCliSubmit

A wrapper cli script, written in python,  around kinda api (https://github.com/PaulSec/API-malwr.com) to interact with the free and public malwr sandbox site, there's been tested on linux with python 2.7.x . The idea its quite simple , submit malware artifacts (file samples) for behavioral analysis on on that sandbox, without intervention, or automated submitting if your preffer to say.

 

For usage you need install have : linux,python, install the malwr.com api , and credentials on malwr.com site (its free!)

after following the instructions embebed into the script you should isue a command like

 

malwrCliSubmit.py --login someUser --password somePassword -s someSuspicius.File

you should get the file name and the url for the analisis, say

someSuspicius.File -> https://malwr.com/submission/status/ZTVlZTgwMDE2MGFmNDc0ZTg3MTNlMTM1YzYxAxgyZGY
