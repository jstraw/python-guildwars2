import collections

class worlds(collections.MutableMapping):
    uri = 'world_names'

    def __init__(self, client):
        self.worldlist = {}
        worlds = client._request(self.uri)
        for x in worlds:
            self.worldlist[int(x['id'])] = x['name']

    def __getitem__(self, key):
        return self.worldlist[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.worldlist[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.worldlist[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.worldlist)

    def __len__(self):
        return len(self.worldlist)

    def __keytransform__(self, key):
        return int(key)
