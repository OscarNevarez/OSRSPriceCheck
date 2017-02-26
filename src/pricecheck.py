'''
Created on Feb 24, 2017

@author: Oscar Nevarez


'''
import discord
import aiohttp
import json

try: 
    from discord.ext import commands
    from aiohttp import ClientSession
    librariesAvailable = True

except:
        
    librariesAvailable = False

class Osrspricecheck:
    """A cog used for checking GE prices on OSRS!"""

    def __init__(self, bot):
        self.bot = bot
        self.osBuddyUrl = "https://rsbuddy.com/exchange?id="
        self.baseUrl = "http://services.runescape.com/m=itemdb_oldschool"
        self.GEItemSearchEndPoint = "/api/catalogue/items.json?category=1&alpha="
        
    'returns the first item in items'
    def __getFirstItem(self, items):
        try:
            item = items['items'][0]
        except:
            item = "No item found with that name"
        return item
    def __getId(self, item):
        try:
            idN = item['id']
        except:
            idN = 0
        return idN
    def __getItemData(self, item):
        name = item['name']
        price = item['current']['price']
        return name + ": " + str(price)
        
    @commands.command()
    async def price(self, *, itemName):
        """Search for the price of an item"""
        url = self.baseUrl + self.GEItemSearchEndPoint + itemName
        async with aiohttp.get(url) as response:
            items = await response.json()
            item = self.__getFirstItem(items)
            idN = self.__getId(item)
            itemData = self.__getItemData(item)

        try:
            await self.bot.say(itemData)
            await self.bot.say(self.osBuddyUrl+str(idN))
        except Exception as e:
            await self.bot.say(e)
           

def setup(bot):
    if librariesAvailable:
        bot.add_cog(Osrspricecheck(bot))
    else:
        raise RuntimeError("Install discord and/or urllib using pip")
        
