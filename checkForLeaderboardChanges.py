import requests
import sys
import os
from decouple import config

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
    
    def print(self):
        lines = []
        sortedMems = board.sortedMembers()
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
        print(s)

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

path = 'https://adventofcode.com/2022/leaderboard/private/view/1897802.json'
#path = 'https://www.nightfallgames.net/1897802.json'

token = config('AoC_token')
headers = {'Cookie': 'session={}'.format(token)}
r = requests.get(path, headers=headers)
data = r.json()

board = Leaderboard(**data)
board.print()