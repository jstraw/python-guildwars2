python-guildwars2
=================

Guild Wars 2 Python Binding

This Software is licensed under the GPL Version 3. (License files coming soon)

Installing
----------
Should be usable with pip via:
pip install https://github.com/jstraw/python-guildwars2/archive/master.zip

Using
-----
```
import guildwars2

gw2 = guildwars2.GuildWars2()
m = gw2.wvw.find('stormbluff')
for x in m.red.map.objectives.values():
   if x.guild == None:
      g = 'None'
   else:
      g = x.guild
   print x.name, x.owner, x.guild
```

Item and recipes are not available yet (Pull Request welcome)
Documentation and Tests coming.
