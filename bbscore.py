#!/usr/bin/env python3

from datetime import datetime
from passlib.hash import pbkdf2_sha256
import linecache
import getpass
import readline
import sys
import re
import os

# Variable assignments. Will read these in from a config file via linecache and assigned to the correct variable. 
# i.e. bbspath = linecache(bbsconfg,1) and so on. Hopefully this will be able to be created by a GUI to create the file, like BBSCONFIG in CNet. 

ansiColors = {"c0" : "[30m", "c1" : "[31m", "c2" : "[32m", "c3" : "[33m", "c4" : "[34m",
               "c5" : "[35m", "c6" : "[36m", "c7" : "[37m", "c8" : "[1;30m",
               "ca" : "[1;31m", "cb" : "[1;32m", "cc" : "[1;33m", "cd" : "[1;34m",
               "ce" : "[1;35m", "cf" : "[1;36m", "cg" : "[1;37m", "Z0" : "[40m" , "Z1" : "[41m",
               "Z2" : "[42m", "Z3" : "[43m", "Z4" : "[44m", "Z5" : "[45m", "Z6" : "[46m",
               "Z7" : "[47m"}

bbsSetup = 'config.txt'
user = {}
now = datetime.now()
bbsName = linecache.getline(bbsSetup, 1)
bbsName = bbsName.strip('\n')
bbsSysop = linecache.getline(bbsSetup, 2)
bbsSysop = bbsSysop.strip('\n')
bbsCity = linecache.getline(bbsSetup, 3)
bbsCity = bbsCity.strip('\n')
bbsState = linecache.getline(bbsSetup, 4)
bbsState = bbsState.strip('\n')
bbsCountry = linecache.getline(bbsSetup, 5)
bbsCountry = bbsCountry.strip('\n')
bbsFQDN = linecache.getline(bbsSetup, 6)
bbsFQDN = bbsFQDN.strip('\n')
bbsPath = linecache.getline(bbsSetup, 7)
bbsPath = bbsPath.strip('\n')
newsPath = bbsPath + "news/"
sysTextPath = bbsPath + "systext/"
sysDataPath = bbsPath + "sysdata/"
pFilesPath = bbsPath + "pfiles/"
doorsPath = pFilesPath
newsHeaderPath = newsPath + "headers/"
currentcalldate = str(now.year) + str(now.month) + str(now.day)

# Still some clean up that can be done. Also, the user dictionary doesn't get returned back to the whole program. Because it was
# created in a function, it's only good there. So need to work on that. Doing it as a class would probably be the best. Have to read up on how to do that.  
# I'm sure there are ways to slim it down and make it more "pythonic", but getting a rough working framework is the first goal. 
# I'll worry about bells and whistles and fancy coding later on. Next step is to get it to display Welcome and News files, then the Main Menu.


# This function reads the file passed to it and does a regex search for the MCI triggers, and then replaces the MCI trigger with the correct
# ANSI escape codes. 

def repl(m):
    code = ansiColors[m.group(2)]
    return '\033' + code

def mciAnsi(fileName):
  file = open(fileName , 'r')
  for lines in file:
    lines = re.sub(r'(\{)(\w+)(\})', repl , lines)
    print lines.strip('\n')
  print ("\033[0m")
  
# This just displays the sys.start file which is shown before logging on. 
def display_start():
  mciAnsi(sysTextPath + 'sys.start' , 'r') 
  

# This is where the logon info is checked against the user db. Right now the db is just a simple text file. The goal is to use SQLite.
def user_auth(username): 
  pass_tries = 0 
  pass_times = 3
  while pass_tries < pass_times:
    userdb = open(bbsPath + "users/" + username + "/data.txt" , "r") 
    for items in userdb.readlines():
      (key, val) = items.split(":") # Take each line, and split the items between the ":", and save them to key and val
      user[key] = val # Take those pieces of data from above and put them into the dictionary "user" with the corresponding key and value
    print ("\nEnter Password") 
    passwrd = getpass.getpass(": ") 
    if str(passwrd) == user["password"].strip('\n') : #compares password to "password" key in the dictionary. 
      return 
    else: 
      print ("\nIncorrect Password!")
      pass_tries += 1  
  else:
    print ("\nToo many bad login attempts. Try later.")
    sys.exit() # We'll add an option for feedback to Sysop later.

# The logon procedure
def login():
  uname_tries = 0
  uname_times = 3
  while uname_tries < uname_times:
    print("\nEnter \"NEW\" if you have no account.") 
    print("Enter your handle.")
    username = raw_input(": ")
    if len(username) > 0 and username != "new" :
      try:
        userdb = open(bbsPath + "users/" + username + "/data.txt" , "r")
      except IOError:
        print("\nUnknown user.")
        uname_tries += 1
        if uname_tries >= uname_times:
          print("\nToo many unknown user attempts. Contact SysOp!") #Can do a bbstext linecache here.
          sys.exit()
        else:
          pass
      else:
        user_auth(username)
        break
    elif username == 'new':
      new_user_signup()
    elif username =='':
      uname_tries += 1
      if uname_tries >= uname_times:
        print("\nToo many unknown user attempts. Contact SysOp!") #Can do a bbstext linecache here.
        sys.exit()
    else:  
      print("\nToo many bad login attempts. Try again later.") #Can do a bbstext linecache here.
      sys.exit()
  return

# The logoff procedure. Will display the sys.end file. 
def logoff():
  logoffinput = raw_input("\nAre you sure you want to logoff? [y/N]") #We'll use linecache here from BBSTEXT file
  if logoffinput == "y" :
    mciAnsi(sysTextPath + 'sys.end') 
    sys.exit()
  else: return

def new_user_signup(): # New User sign up. Nothing here yet..
  print ("\nNot accepting New Users at this time.")
  sys.exit()

# This grabs a listing of the news files in the news directory
def get_news_items():
  newslist = os.listdir(newsPath)
  return newslist

# This just displays the news files. 
def display_file(item):
  file = open(newsPath + item, 'r') 
  lines = file.readlines()
  del lines[0]
  for i in lines:
    print (i).strip('\n')
  return lines

# This will grab a header for a news file. You'll be able to create multiple headers and assign one to a news item. 
def header_setup(item):
  header = open(newsPath + item , "r")
  header_file = header.readline()
  if header_file[0] == ";":
    header_file = header_file.replace(";" , "")
    header_file = header_file.replace("\n" , "")
    header.close()
    return header_file

# This is to display the news header
def display_header(header_file):
  header = open(newsHeaderPath + header_file , 'r')
  for lines in header:
    print (lines).strip('\n')
  return

# This checks the user's last call date and shows the items that are new. 
def do_news():
  newslist = get_news_items()
  for item in newslist:
    try:
      if int(item.strip('.news')) > int(user['lastcall']):
        header_file = header_setup(item)
        print("\033[2J")
        display_header(header_file)
        display_file(item)
        raw_input('\nPress [ENTER] to continue..\n')
      else:
        pass
    except ValueError:
      pass

def udbase():
  print("\033[2J")
  print("Upload/Download Base Test Menu")
  print("Please choose an option below to test the Zmodem file transfer for this BBS")
  print("1. Recieve our test file\n2. Send us a test file\nQ. Quit")
  udmenu = raw_input("\nChoose (1 or 2 or Quit): ")
  while udmenu != "q" or "Q" :
    if udmenu == "1":
      os.system("sz -b /home/mobbyg/anet/zmodem_test.zip")
      udmenu = "0"
      return
    elif udmenu == "2":
      os.system("cd /home/mobbyg/anet/;rz -bZ")
      udmenu = "0"
      return
    else:
      udmenu ="0"
      return
    
# The main menu for the BBS. 
def main_menu():
  pass
  print ("\nEntering BBS core...")
  while True:
    userinput = raw_input("\nANet BBS >: ") # We'll use linecache here from BBSTEXT file
    if userinput == "o" or userinput == "logoff" :
      logoff()
    elif userinput == "o!" :
      break
    elif userinput == "inf" :
      try:
        mciAnsi(sysTextPath + 'sys.info')
      except IOError:
        print("No system information file found.")
    elif userinput =="u" :
      udbase() 
    else: print ("\nThat Command is not yet active.") #We'll use linecache here from BBSTEXT file
    
#core starts here...    
#display_start() # Function to display the sys.start

# This is pretty much the BBS. Display the start screen, login the user, show the news and then go to the Main Menu. 
# The Main Menu will call the modules for the BBS, like Gfiles, PFiles/Doors and U/D Bases. 
try:
  mciAnsi(sysTextPath + 'sys.start')
except IOError:
  pass
login()
do_news()
try:
  mciAnsi(sysTextPath + 'sys.welcome')
except IOError:
  pass
main_menu() # This is next up. The main menu system
