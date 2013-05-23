import collections

class Match:
    uri = 'wvw/match_details'
    def __init__(self, client, match_id, red, blue, green):
        # TODO: make details sane
        self.details = client._request(self.uri, 
                params = {'match_id': self.match})
        self.red = {'id': red, 'name': client.world[red], 
                    'score': details['scores'][0]}
        self.blue = {'id': blue, 'name': client.world[blue],
                    'score': details['scores'][1]}
        self.green = {'id': green, 'name': client.world[green],
                    'score': details['scores'][2]}
        self.match = match_id
        if match_id[0] == '1':
            self.region = 'us'
        else:
            self.region = 'eu'
        self.tier = int(match_id[-1])


class match_list:
    uri = 'wvw/matches'

    def __init__(self, client):
        self.matchlist = []
        response = client._request(self.uri)
        for m in response:
            self.matchlist.append(Match(
                m['wvw_match_id'], m['red_world_id'],
                m['blue_match_id'], m['green_world_id'])
            )

    def find(self, item):
        """Find and return the match being searched for"""
        try:
            int(item)
            key = 'id'
        except ValueError:
            key = 'name'
        for m in matchlist:
            if item in m.red[key]:
                return m
            elif item in m.blue[key]:
                return m
            elif item in m.green[key]:
                return m
            elif item in m.match:
                return m
        return False
            
