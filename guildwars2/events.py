import collections

class event_mapping(collections.MutableMapping):
   """This is used in context of the events search only, 
   and is exposed as events.mapping (dictionary)"""
   uri = 'event_names'

   def __init__(self, client):
      self.eventlist = {}
      events = client._request(self.uri)
      events = [(x['id'], x['name']) for x in events]
      self.eventlist.update(events)

   def __getitem__(self, key):
      return self.eventlist[self.__keytransform__(key)]

   def __setitem__(self, key, value):
      self.eventlist[self.__keytransform__(key)] = value

   def __delitem__(self, key):
      del self.eventlist[self.__keytransform__(key)]

   def __iter__(self):
      return iter(self.eventlist)

   def __len__(self):
      return len(self.eventlist)

   def __keytransform__(self, key):
      return key
