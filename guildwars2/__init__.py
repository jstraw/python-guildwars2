import os
import requests

import wvw.locations
import wvw.matches
import events
import worlds
import maps
import items
import recipes

############ Hax to make wvw sane
wuvwuv_locations = {"56": "The Titanpaw", "54": "Foghaven", "42": "Redlake", "48": "Faithleap", "43": "Hero's Lodge", "60": "Stargrove", "61": "Greenwater Lowlands", "49": "Bluevale Refuge", "52": "Arah's Hope", "53": "Greenvale Refuge", "24": "Champion's demense", "25": "Redbriar", "26": "Greenlake", "27": "Ascension Bay", "20": "Veloka Slope", "21": "Durios Gulch", "22": "Bravost Escarpment", "23": "Garrison", "46": "Garrison", "47": "Sunnyhill", "44": "Dreadfall Bay", "45": "Bluebriar", "28": "Dawn's Eyrie", "29": "The Spiritholme", "40": "Cliffside", "41": "Shadaran Hills", "1": "Overlook", "3": "Lowlands", "2": "Valley", "5": "Pangloss Rise", "4": "Golanta Clearing", "7": "Danelon Passage", "6": "Speldan Clearcut", "9": "Stonemist Castle", "8": "Umberglade Woods", "51": "Astralholme", "39": "The Godsword", "38": "Longview", "59": "Redvale Refuge", "58": "Godslore", "11": "Aldon's Ledge", "10": "Rogue's Quarry", "13": "Jerrifer's Slough", "12": "Wildcreek Run", "15": "Langor Gulch", "14": "Klovan Gully", "17": "Mendon's Gap", "16": "Quentin Lake", "19": "Ogrewatch Cut", "18": "Anzalias Pass", "31": "Askalion Hills", "30": "Woodhaven", "37": "Garrison", "36": "Bluelake", "35": "Greenbriar", "34": "Victors's Lodge", "33": "Dreaming Bay", "55": "Redwater Lowlands", "32": "Etheron Hills", "57": "Cragtop", "50": "Bluewater Lowlands"}


class GuildWars2:
   base_url = 'https://api.guildwars2.com/v1/'
   self.ver = '0.0.0'
   user_agent = 'python-guildwars2 %s' % self.ver

   def __init__(self, lang='en', user_agent=None):
      self.lang = lang
      if 'GW2_DEBUG' in os.environ:
         self.debug = True
      if user_agent:
         self.user_agent = user_agent


   
   def __request(self, uri, **kwargs):
      url = '%s%s.json' % (self.base_url, uri)
      kwargs.setdefault('headers', {})['Accept'] = 'application/json'
      kwargs['headers']['User-Agent'] = self.user_agent

      kwargs.setdefault('params', None)
      
      r = requests.get(url, params=kwargs['params'], headers=kwargs['headers'])
      return r.json()
