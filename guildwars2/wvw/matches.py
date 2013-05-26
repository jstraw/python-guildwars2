import collections

# import objective list alone to prevent namespace issue
from objectives import objective_list


class Match:
    uri = 'wvw/match_details'

    def __repr__(self):
        return "<World vs World Match: %s Tier %d (%s)>" % \
                (self.region, self.tier, self.match)

    def __init__(self, client, match_id, red, blue, green):
        # Set the match id (and break it into region / tier)
        self.match = match_id
        if match_id[0] == '1':
            self.region = 'us'
        else:
            self.region = 'eu'
        self.tier = int(match_id[-1])

        # Get Objective List
        ol = objective_list(client)

        # Pull the match details and create servers / objective lists
        self.details = client._request(self.uri, 
                params = {'match_id': self.match})
        map_temp = {}
        for x in self.details['maps']:
            if 'RedHome' == x['type']:
                map_temp['red'] = (x['objectives'], x['scores'])
            elif 'BlueHome' == x['type']:
                map_temp['blue'] = (x['objectives'], x['scores'])
            elif 'GreenHome' == x['type']:
                map_temp['green'] = (x['objectives'], x['scores'])
            elif 'Center' == x['type']:
                map_temp['eb'] = (x['objectives'], x['scores'])
        self.red = Color(
                Server(red, client.worlds[red], self.details['scores'][0]),
                Map(map_temp['red'][0], ol, map_temp['red'][1])
            )
        self.blue = Color(
                Server(blue, client.worlds[blue], self.details['scores'][1]),
                Map(map_temp['blue'][0], ol, map_temp['blue'][1])
            )
        self.green = Color(
                Server(green, client.worlds[green], self.details['scores'][2]),
                Map(map_temp['blue'][0], ol, map_temp['blue'][1])
            )
        self.eb = Color(
                None,
                Map(map_temp['eb'][0], ol, map_temp['eb'][1])
            )
        self.eternal = self.eb

class Color:
    def __init__(self, server, _map):
        self.server = server
        self.map = _map


class Server:
    def __init__(self, _id, name, score):
        self.id = _id
        self.name = name
        self.score = score

class Map:
    def __init__(self, objectives, ol, scores):
        self.red_score = scores[0]
        self.blue_score = scores[1]
        self.green_score = scores[2]
        self.objectives = {}
        for x in objectives:
            self.objectives[x['id']] = ol[x['id']]
            self.objectives[x['id']].owner = x['owner'].lower()
            if 'owner_guild' in x:
                self.objectives[x['id']].guild = x['owner_guild']
            else:
                self.objectives[x['id']].guild = None



class match_list:
    uri = 'wvw/matches'

    def __init__(self, client):
        self.matchlist = []
        response = client._request(self.uri)
        for m in response['wvw_matches']:
            self.matchlist.append(Match(client,
                m['wvw_match_id'], m['red_world_id'],
                m['blue_world_id'], m['green_world_id'])
            )

    def find(self, item):
        """Find and return the match being searched for"""
        for m in self.matchlist:
            red = m.red.server
            blue = m.blue.server
            green = m.green.server
            a = (red.id, blue.id, green.id)
            b = ' '.join((red.name.lower(), 
                blue.name.lower(), green.name.lower()))
            try:
                _id = int(item)
                if _id in a:
                    return m
            except:
                if item in b:
                    return m
        return False
            
