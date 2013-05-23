import os
import requests

import wvw.objectives
import wvw.matches
import events
import worlds
import maps
#import items
#import recipes



class GuildWars2:
   base_url = 'https://api.guildwars2.com/v1/'
   ver = '0.0.0'
   user_agent = 'python-guildwars2 %s' % ver

   def __init__(self, lang='en', user_agent=None):
      self.lang = lang
      if 'GW2_DEBUG' in os.environ:
         self.debug = True
      if user_agent:
         self.user_agent = user_agent
      self.maps = maps.maps(self)
      self.worlds = worlds.worlds(self)


   
   def _request(self, uri, **kwargs):
      url = '%s%s.json' % (self.base_url, uri)
      kwargs.setdefault('headers', {})['Accept'] = 'application/json'
      kwargs['headers']['User-Agent'] = self.user_agent

      kwargs.setdefault('params', None)
      
      r = requests.get(url, params=kwargs['params'], headers=kwargs['headers'])
      return r.json()
