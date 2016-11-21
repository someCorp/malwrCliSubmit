#!/usr/bin/env python
""" wrapper to upload unatenndly samples to malwr free sandbox """
try:
  import sys
except ImportError:
  errMsg = "\nfailed lib, try pip install sys\n"
  sys.stderr.write(errMsg)
  sys.exit(1)
try:
  from MalwrAPI import MalwrAPI
except ImportError:
  errMsg = """
failed lib, try git clone https://github.com/PaulSec/API-malwr.com.git
and THEN pip install -r /some/path/API-malwr.com/requirements.txt
as super user , say sudo pip install -r /some/path/API-malwr.com/requirements.txt
consider /some/path its the directory where the API where downloaded
usually will be your home , say /home/user/API-malwr.com

after install the API that copy this script to /some/path/API-malwr.com/
to lauch the script use the following example
/some/path/API-malwr.com/malwr-cli-submit.py --login someRegisteredUserOnMalwrSite --password superSecret -s /some/badware.ext

after that you and if the submission works fine, should see an error message bugging ssl stuff and for

SNIMissingWarning:
InsecurePlatformWarning:

sample.txt -> https://malwr.com/submission/status/MTc2OWU5OGNiMjAxNDVjNjgxNGE4NjQwNDM0NjdjZTg/

this happens cause urllib its a bit old, try to upgrade or ignore the error redirecting stderr

/some/path/API-malwr.com/malwr-cli-submit.py --login someRegisteredUserOnMalwrSite --password superSecret -s /some/badware.ext 2>/dev/null

"""
  sys.stderr.write(errMsg)
  sys.exit(1)
try:
  import argparse
except ImportError:
  errMsg = "\nfailed lib, try pip install argparse\n"
  sys.stderr.write(errMsg)
  sys.exit(1)


parser = argparse.ArgumentParser(description="submit files on cli way to malwr", version='0.0.0a')
parser.add_argument("-l", "--login", help="login name on malwr portal",
                    type=str, required=True, default="")
parser.add_argument("-p", "--password", help="password on malwr portal",
                    type=str, required=True, default="")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-s", "--sample", help="file to submit on malwr portal",
                   type=str, required=False, default=None)
group.add_argument("-d", "--directory", help="directory with samples to submit on malwr portal",
                   type=str, required=False, default=None)

try:
  args = parser.parse_args()
  login = args.login
  password = args.password
  fileToSubmit = args.sample
  try:
    directoryToSubmit = args.directory
  except IOError as e:
    errMsg = "\nnon existant file or directory , maybe bad login or password\n\n"
    sys.stderr.write(errMsg)
    directoryToSubmit = None
except StandardError as e:
  errMsg = "\nnon existant file or directory , maybe bad login or password\n\n"
  sys.stderr.write(errMsg)
  sys.stderr.write(str(e))
  sys.stderr.write("\n\n")
  sys.exit(3332)

if len(sys.argv) <= 6:
  errMsg = "\nbad args\n\n" + "exec " + sys.argv[0] + " -h to get help\n\n"
  sys.stderr.write(errMsg)
  sys.exit(3333)

api_authenticated = MalwrAPI(verbose=False, username=login, password=password)

if fileToSubmit != None:
  res = api_authenticated.submit_sample(fileToSubmit)
  for key, value in res.items():
    if key == "analysis_link":
      fileUrl = "https://malwr.com" + value
    if key == "file":
      fileMsg = value + " -> " + fileUrl
  print fileMsg
  sys.exit(0)
if directoryToSubmit != None:
  res = api_authenticated.submit_folder(directoryToSubmit)
  for i in res:
    for key, value in i.items():
      if key == "analysis_link":
        fileUrl = "https://malwr.com" + value
      if key == "file":
        fileMsg = value + " -> " + fileUrl
    print fileMsg
  sys.exit(0)
