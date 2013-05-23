import collections

class maps(collections.MutableMapping):
   uri = 'map_names'

   def __init__(self, client):
      self.maplist = {}
      maps = client._request(self.uri)
      for x in maps:
          self.maplist[int(x['id'])] = x['name']

   def __getitem__(self, key):
      return self.maplist[self.__keytransform__(key)]

   def __setitem__(self, key, value):
      self.maplist[self.__keytransform__(key)] = value

   def __delitem__(self, key):
      del self.maplist[self.__keytransform__(key)]

   def __iter__(self):
      return iter(self.maplist)

   def __len__(self):
      return len(self.maplist)

   def __keytransform__(self, key):
      return int(key)
