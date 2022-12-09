import requests
import sys
import os
import json
from decouple import config
import smtplib
import datetime

class Member:
    def __init__(self, id, name, last_star_ts, global_score, local_score, stars, completion_day_level) -> None:
        self.id = id
        self.name = name
        self.last_star_ts = last_star_ts
        self.global_score = global_score
        self.local_score = local_score
        self.stars = stars
        self.completion_day_level = completion_day_level
        if self.name is None: self.name = 'Anonymous'

    def __str__(self) -> str:
        s = '[{}] {}: {}'.format(self.id, self.name, self.local_score)
        return s

class Leaderboard:
    def __init__(self, event, owner_id, members) -> None:
        self.event = event
        self.owner_id = owner_id
        self.members = {}
        for k, v in members.items():
            self.members[k] = Member(**v)
        self.maxNameLength = self.getMaxMemberNameLength()
        self.maxScoreLength = self.getMaxScoreLength()

    def __str__(self) -> str:
        sMembers = ''
        for m in self.members.values():
            sMembers += '{}\n'.format(m)
        s = 'event: {}\nowner: {}\nMembers: \n{}'.format(self.event, self.owner_id, sMembers)
        return s

    def sortedMembers(self):
        sortedMems = []
        while len(sortedMems) < len(self.members):
            currMax = -1
            currMem = None
            for m in self.members.values():
                if m in sortedMems: continue
                if m.local_score > currMax:
                    currMax = m.local_score
                    currMem = m
            sortedMems.append(currMem)
        return sortedMems
    
    def toString(self):
        lines = []
        sortedMems = self.sortedMembers()
        maxLine = 0
        for m in sortedMems:
            numSpaces = 2
            numSpaces += (self.maxNameLength - len(m.name))
            numSpaces += (self.maxScoreLength - len(str(m.local_score)))
            sLine = '[{}] {} {}{}'.format(m.id, m.name, ' '*numSpaces, m.local_score)
            if len(sLine) > maxLine: maxLine = len(sLine)
            lines.append(sLine)

        sTitle = '{} Leaderboard'.format(self.event)
        numSpaces = 0
        if len(sTitle) < maxLine:
            numSpaces = (maxLine - len(sTitle))/2
            sTitle = '{}{}\n'.format(' '*int(numSpaces),sTitle)
            sTitle += '='*maxLine
            numSpaces = 0
        elif len(sTitle) > maxLine:
            numSpaces = (len(sTitle) - maxLine)/2
            sTitle += '\n{}'.format('='*len(sTitle))

        s = sTitle + '\n'
        for l in lines:
            s += '{}{}\n'.format(' '*int(numSpaces),l)
        return s

    def print(self):
        print(self.toString())

    def getMaxMemberNameLength(self):
        currMax = 0
        for m in self.members.values():
            if len(m.name) > currMax: currMax = len(m.name)
        return currMax
    
    def getMaxScoreLength(self):
        currMax = 0
        for m in self.members.values():
            if len(str(m.local_score)) > currMax: currMax = len(str(m.local_score))
        return currMax

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

def send_message(number, carrier, message):
    recip = '{}{}'.format(number, CARRIERS[carrier])
    smtpauth = config('SMTP_Login')

    server = smtplib.SMTP(config('SMTP_Server'), config('SMTP_Port'))
    server.starttls()
    server.login(smtpauth['Username'],smtpauth['Password'])

    server.sendmail(smtpauth['Username'], recip, message)

def getBoard(year=None):
    if year is None: year = (datetime.date.today()).year
    path = 'https://adventofcode.com/{}/leaderboard/private/view/{}.json'.format(year,config('Id'))

    token = config('AoC_token')
    headers = {'Cookie': 'session={}'.format(token)}
    r = requests.get(path, headers=headers)
    data = r.json()

    return Leaderboard(**data)

def getYears():
    years = []
    curr = (datetime.date.today()).year
    for y in range(2015,curr+1):
        years.append(str(y))
    return years

def menu():
    main = 'Main Menu\n'
    main += '-'*len('Main Menu')
    main += '\n'
    main += '1. Current Leaderboard\n'
    main += '2. Past Leaderboard\n'
    main += '9. Quit\n'

    match input(main):
        case "1":
            (getBoard()).print()
        case "2":
            year = input("Enter year [2015-{}]:".format((datetime.date.today()).year))
            if year not in getYears():
                print("Invalid option. Try Again.\n")
                return menu()
            else:
                (getBoard(year)).print()
        case "9":
            sys.exit(0)
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

while (True):
    menu()