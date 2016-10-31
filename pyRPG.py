#!/usr/bin/env python
import random as r
def chance(perc):
    if perc/100.0 < r.random():
        return True
    return False
def multiplier():
    return r.choice([0.25,0.5,0.75,1,1.25,1.5,1.75,2,3])
class Person:
    stats = {}
    parent1Stats = {}
    parent2Stats = {}
    def __init__(self,min = 15, max = 50, mmin = 0.5, mmax = 3, minage = 14,maxage = 99,hasParents=False,parent1Stats = {"SEX" : "PLACEHOLDER"}, parent2Stats = {"SEX":"PLACEHOLDER"}):
        self.new = {}
        self.namelist = {"Male" : ["Skullcape" , "Hieronymus" , "Karsten" , "Cenk" , "Bréanainn" , "Yavor" , "Chavaqquq" , "Delaiah" , "Ramaz" , "Gernot" , "Lasse" , "Wigmar" , "Emeka" , "Flavio" , "Rainer" , "Roshan"],
                    "Female" : ["Imelda", "Helena" , "Niobe" , "Mia", "Marley", "Serpil", "Liat" , "Putu" , "Willy" , "Loretta" , "Oksana" , "Chisomo" , "Mathilde" , "Siiri" , "Antonija" , "Anica", "Kylie"],
                    "Other" : ["Lior", "Ale" , "Vanja" , "Yanick" , "Kasey" , "Blair" , "Tendai" , "Abimbola" , "Gabi" , "Brett" , "Lashawn" , "Tiyamike" , "Udo" , "Guanting" , "Toby" , "Sasha" , "Ji-Young" , "Shun" , "Oghenekaro" , "Chioma"],
                    "Sur" : ["Van Rossem" , "Teel" , "Garner" , "Katranjiev" , "Biondo" , "Madsen" , "Popov" , "Yamashita" , "Bryan" , "Wolf" , "Santana" , "Zino" , "Horn" , "Lewerenz" , "Armbruster" , "Herriot" , "Gardyner" , "Ikin" , "Mayes" , "Campo" , "Oliver" , "Bergström"],
                   }
        self.stats = ["HP", "MP", "STR", "SPE" ,"DEX", "CHA"]
        if not hasParents:
            for curStat in self.stats:
                if chance(50):
                   self.new[curStat] = multiplier() , "x"
                   continue
                self.new[curStat] = r.randint(min, max) , ""
            self.new["AGE"] = r.randint(minage, maxage)
            self.new["SEX"] = r.choice(["Male", "Female", "Other"])
            self.new["ORIENTATION"] = r.choice(["Straight", "Straight", "Bi", "Gay", "Gay"])
            self.new["NAME"] = r.choice(self.namelist[self.new["SEX"]])
            self.new["SUR"] = r.choice(self.namelist["Sur"])
        else:
            for element in parent1Stats:
                if element in ["SEX", "ORIENTATION", "NAME", "AGE"]:
                    continue
                if element == "SUR":
                    if chance(50):
                        parent1Stats[element]
                    else:
                       self.new[element] = parent2Stats[element]
            self.new["AGE"] = 0
            self.new["ORIENTATION"] = []
            if parent1Stats["SEX"]  == parent2Stats["SEX"]:
               self.new["SEX"] = parent1Stats["SEX"]
               self.new["ORIENTATION"] = r.choice(["Gay", "Gay", "Straight", "Bi"])
            else:
               self.new["ORIENTATION"] = r.choice(["Gay", "Straight", "Bi"])
               self.new["SEX"] = r.choice(["Male", "Female", "Other"])
               self.new["NAME"] = r.choice(self.namelist[self.new["SEX"]])
               self.new["SUR"] = r.choice([parent1Stats["NAME"], parent2Stats["NAME"]])
        self.stats =self.new
print(Person().stats)
print(Person(parent1Stats = Person().stats, parent2Stats = Person().stats).stats)

input("press enter key to exit")
