import collections

wuvwuv_locations = {"56": "The Titanpaw", "54": "Foghaven", "42": "Redlake", "48": "Faithleap", "43": "Hero's Lodge", "60": "Stargrove", "61": "Greenwater Lowlands", "49": "Bluevale Refuge", "52": "Arah's Hope", "53": "Greenvale Refuge", "24": "Champion's demense", "25": "Redbriar", "26": "Greenlake", "27": "Ascension Bay", "20": "Veloka Slope", "21": "Durios Gulch", "22": "Bravost Escarpment", "23": "Garrison", "46": "Garrison", "47": "Sunnyhill", "44": "Dreadfall Bay", "45": "Bluebriar", "28": "Dawn's Eyrie", "29": "The Spiritholme", "40": "Cliffside", "41": "Shadaran Hills", "1": "Overlook", "3": "Lowlands", "2": "Valley", "5": "Pangloss Rise", "4": "Golanta Clearing", "7": "Danelon Passage", "6": "Speldan Clearcut", "9": "Stonemist Castle", "8": "Umberglade Woods", "51": "Astralholme", "39": "The Godsword", "38": "Longview", "59": "Redvale Refuge", "58": "Godslore", "11": "Aldon's Ledge", "10": "Rogue's Quarry", "13": "Jerrifer's Slough", "12": "Wildcreek Run", "15": "Langor Gulch", "14": "Klovan Gully", "17": "Mendon's Gap", "16": "Quentin Lake", "19": "Ogrewatch Cut", "18": "Anzalias Pass", "31": "Askalion Hills", "30": "Woodhaven", "37": "Garrison", "36": "Bluelake", "35": "Greenbriar", "34": "Victors's Lodge", "33": "Dreaming Bay", "55": "Redwater Lowlands", "32": "Etheron Hills", "57": "Cragtop", "50": "Bluewater Lowlands"}


class Objective:
    def __init__(self, d):
        # Because Tower is useless, using hack dict above
        scores = {'tower': 10, 'keep': 25, 'castle': 35, 'camp': 5}
        self.id = int(d['id'])
        self.name = wuvwuv_locations[d['id']]
        try:
            self.score = scores[d['name'].lower()]
        except:
            self.score = scores['camp']

    def __repr__(self):
        return "<Objective: %s (%d) (%d points)" % \
                (self.name, self.id, self.score)


class objective_list(collections.MutableSequence):
    uri = 'wvw/objective_names'
    objectivelist = []

    def __init__(self, client):
        response = client._request(self.uri)
        for m in response:
            self.objectivelist.append(Objective(m))

    def __getitem__(self, key):
        for x in self.objectivelist:
            if key == x.id:
                return x

    def __setitem__(self, key):
        self.objectivelist[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.objectivelist[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.objectivelist)

    def __len__(self):
        return len(self.objectivelist)

    def __keytransform__(self, key):
        return key

    insert = objectivelist.insert
