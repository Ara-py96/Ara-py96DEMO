from ter import place

data = open("c:/Users/ARAVIND/Documents/my.txt","a")
data.write("\n")

print("% This is a buiding simulater %")
e = input("enter your name ")
data.write(e+"\n")
m = input("Enter your Mobile Number ")
data.write(m+"\n")

pl = input("enter a area to start build ")
data.write(pl+"\n")
p1 = place(pl)
print("defalt city is chennai")
r = int(input("do you want to change the city for all yor builds if yes enter 1 if no enter 2 "))
if r  == 1:
    data.write("yes\n")
 
    i = input("enter city name ")
    data.write(i+"\n")
    place.setLocation(place,i)
    print("city is set as",p1.area)
    data.write(place.area+"\n")
    p = p1.building.__init__(p1, p1.location)
  
    t = input("enter new building name ")
    data.write(t+"\n")

    p1.building.buld(p1, t)
else:
    data.write("no\n")

   
    p1.setWhere(p1.location)
    data.write(place.area+"\n")
    p = p1.building.__init__(p1,p1.where)
    t = input("enter new building name ")
    data.write(t+"\n")
    p1.building.buld(p1,t)
data.close()









                

            




                 
