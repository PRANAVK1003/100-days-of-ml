#Indexing
index = ['Pranav', 'Aniket', 'Yash']
print("index[0]", index[0])
#Slicing : removing the list members before stated index .
print("After Slicing: ", index[1:])

#Dictionaries : Same as list but contains key value pairs . 
protaginists = {"Bleach":"Aizen", "DragonBall":"Goku","Jujutsu Kaisen":"Yuji Itadori", "Attack On Titan":"Eren Yeager"}
print(protaginists)
print(protaginists["Bleach"])
#changing the value for key 
protaginists["Jujutsu Kaisen"]= "Gojo Satoru"
print(len(protaginists))
#ordered dictionaries 
from collections import OrderedDict
rappers = {}
rappers["Drake"]= "God's plan "
rappers["Kanye"]= "Jesus Walks"
print(rappers)
print(rappers["Drake"])
print(rappers.items)
print(OrderedDict(sorted(rappers.items(),key=lambda x:x[1])))
