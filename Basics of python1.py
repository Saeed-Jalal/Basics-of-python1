#Mutable Data Type
#Lists
myHome = ["Bed","Sohva","TV","XBOX","Table","Computer"]
print(myHome)
#Concatenation
print(myHome+["Books","Perfumes"])
#Repetition
print(myHome*2)
#Slicing
print(myHome[1:4])
#append
myClothes = ["Jeans","Shirts"]
myClothes.append("Shoes")
print(myClothes)
#extend
myClothes.extend(["T.shirts","Boxers"])
print(myClothes)

#Dictionaries
myDict = {1:'Home',2:'Car',3:'Ship',4:'Clothes'}
#dict with integer keys
print(myDict)
#dict with mixed keys
myDict = {"jeans":"pent",1:[2,4,3]}
print(myDict.keys())

#Accessing dict
myDict={1:"apple",2:"mango"}
print(myDict[2])
#Dict len
print(len(myDict))
#Dict key
myDict1={1:"Home",2:"Car",3:"Bank"}
print(myDict1.keys())
#Dict values
myDict={1:"Car",2:"Home",3:"Office"}
print(myDict.values())
#Dict items
myDict={1:"Fruit",2:"Apple",3:"Mango",4:"Orange"}
print(myDict.items())
#Dict get

print(myDict.get(3))

#Dict update
myDict2={1:"Fruit",2:"Apple",3:"Mango",4:"Orange"}
myDict2.update({5:"Guava"})
print(myDict2)
#Dict pop
myDict2={1:"Fruit",2:"Apple",3:"Mango",4:"Orange"}
myDict2.pop(2)
print(myDict2)

#Set
mySet = {10,20,30,40,50}
print(mySet)






