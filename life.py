import random
deathlist=["karma killed you.","you were on Santa's naughty list.","you got hit by a stray baseball bat.","someone peed on your wound.","you got a papercut.","you took off your blindfold and killed yourself.","you ate overdue chunks of milk.","you threatened a cub and got mauled.","you went peacefully in your sleep.","you drank too much water."]
deathlist10=["karma killed you.","you were on Santa's naughty list.","you got hit by a stray baseball bat.","someone peed on your wound.","you got a papercut.","you took off your blindfold and killed yourself.","you ate overdue chunks of milk.","you let your dog poop on the wrong yard.","you threatened a cub and got mauled.","you went peacefully in your sleep.","you drank too much water.", "you said \"YOLO!\", then did something stupid."]

maxage=random.randint(0,107)
if(maxage==0):
    maxage=random.random()
age=0
while(age<maxage):
    age+=1
if(maxage==0):
    print("\nUnlucky, you died because your mother didn't want to go through labor.\n")
elif(maxage<=1):
    if(maxage==1):
        print("\nYou died at the age of {} year because {}\n".format(int(age),random.choice(deathlist)))
    else:
        age=round(maxage*12)
        if(age==0):
            age=1
        elif(age==12):
            age=11
        if(int(age)==1):
            print("\nYou died at the age of {} month because {}\n".format(int(age),random.choice(deathlist)))
        else:
            print("\nYou died at the age of {} months because {}\n".format(int(age),random.choice(deathlist)))
else:
    print("\nYou died at the age of {} years because {}\n".format(age,random.choice(deathlist10)))