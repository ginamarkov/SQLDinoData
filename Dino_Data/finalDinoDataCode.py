import csv
import wikipedia as w
import sys
import sqlite3

conn = sqlite3.connect("Dino.db")
c = conn.cursor()

def menu ():
    print("Hello! Welcome to our Dino database. Here is some information from wikipedia about dinos. \n\n")
    print (w.summary("Dinosaurs", sentences=5))
    choice = (int(raw_input(" \n\n You can learn about many things about dinos. \n\t If you want to learn about the diet of dinos and how it correlates with their region, type 1. \n\t If you want to know when and by whom each dino was discovered, type 2. \n\t If you want to know how many of our dinos walk on two versus four legs, type 3. \n\t If you want to know how many dinos from a certain period had a certain diet, type 4. \n\t Finally, if you want to quit, type 5.")))
    while choice != 5:
        if choice == 1:
            query1()
        elif choice == 2:
            query2()
        elif choice == 3:
            query3()
        elif choice == 4:
            query4()
        else:
            choice = (int(raw_input("Choice not available. Please choose again. If you want to quit, type 5.")))
    print ("Bye!!!")
    sys.exit(0)


def query1():
    user_diet = (raw_input(" \n\n Choose what diet to learn about - carnivorous, herbivorous, omnivorous, or herbivorous/omnivorous. If you want to quit, type quit.").lower())
    while user_diet!="quit":
        user_limit = (raw_input(" \n How many dinos do you want to know this about?"))
        c.execute('SELECT BigTable.Name, Location.Location, Diet.Diet FROM BigTable '\
                +'JOIN Location ON BigTable.Location_ID = Location.Location_ID '\
                +'JOIN Diet ON BigTable.Diet_ID = Diet.Diet_ID '\
                +'WHERE Diet.Diet = ("'+user_diet+'") '\
                +'LIMIT('+user_limit+')')
                
        bigList = [[str(item) for item in results] for results in c.fetchall()]

        for item in bigList:
            item[1] = str(item[1])
            item[1] = item[1].replace("|", ",")
            for char in item[1]:
                if char.index == (len(item[1])-1):
                    char = char+"."
            print "The " +item[0]+ " is " +item[2]+ " and is found in " +item[1]+ "."

        user_diet = (raw_input(" \n Choose what diet you want to learn about - carnivorous, herbivorous, omnivorous, or herbivorous/omnivorous. If you want to quit, type quit.").lower())
    menu()


def query2():
    user_limit_2 = (raw_input(" \n\n Here, you can learn the name of the scientist who discovered a dino and the date they discovered it. If you want to quit, type quit. \n For how many dinos do you want to know this info?"))
    while user_limit_2 != "quit":
        c.execute('SELECT BigTable.Name, Discovery.Discovered_By, Discovery.Date_Of_Discovery FROM BigTable '\
                +'JOIN Discovery ON BigTable.Discovery_ID = Discovery.Discovery_ID '\
                +'LIMIT('+user_limit_2+')')

        bigList2 = [[str(item) for item in results] for results in c.fetchall()]

        for item in bigList2:
            print " \n The " +item[0]+ " was discovered by " +item[1]+ " in the year " +item[2]+ "."

        user_limit_2 = (raw_input(" \n Here, you can learn the name of the scientist who discovered a dino and the date they discovered it. If you want to quit, type quit. \n For how many dinos do you want to know this info?"))
    menu()


def query3():
    user_legs = (raw_input(" \n\n Do you want to know how many 2 legged or 4 legged dinos there are in the database? If you want to quit, type quit."))
    while user_legs != "quit":
        c.execute('SELECT Char_Info.Legs_No, COUNT(BigTable.Dino_ID) FROM BigTable '\
                +'JOIN Char_Info ON BigTable.Char_ID = Char_Info.Char_ID '\
                +'WHERE Legs_No = ('+user_legs+') '\
                +'GROUP BY Char_Info.Legs_No ')
               
        bigList3 = [[str(item) for item in results] for results in c.fetchall()]

        for item in bigList3:
            print " \n There are " +item[1]+ " instances of " +item[0]+ " legged dinos in our database."

        user_legs = (raw_input(" \n Do you want to know how many 2 legged or 4 legged dinos there are in the database? If you want to quit, type quit."))
    menu()



def query4():
    user_period = (raw_input(" \n\n Input a time period to delve into - Early Jurassic, Mid Jurassic, Late Jurassic, Early Cretaceous, or Late Cretaceous. If you want to quit, type quit."))
    while user_period != "quit":
        user_diet2 = (raw_input(" \n Great! You chose the the " +user_period+ " period! \n Do you want to know how many herbivorous, omnivorous, or carnivorous dinos there were in this period?").lower())
        c.execute ('SELECT Period.Period, Diet.Diet, COUNT(BigTable.Dino_ID) FROM BigTable '\
                +'JOIN Period ON BigTable.Period_ID = Period.Period_ID '\
                +'JOIN Diet ON BigTable.Diet_ID = Diet.Diet_ID '\
                +'WHERE Period = ("'+user_period+'") '\
                +'AND Diet = ("'+user_diet2+'") '\
                +'GROUP BY Period.Period, Diet.Diet ')
        
        bigList4 = [[str(item) for item in results] for results in c.fetchall()]
        # print bigList4

        for item in bigList4:
            print " \n In the " +item[0]+ " period, there are " +item[2]+ " dinos that are " +item[1]+ "."

        user_period = (raw_input(" \n\n Input a time period to delve into - Early Jurassic, Mid Jurassic, Late Jurassic, Early Cretaceous, or Late Cretaceious. If you want to quit, type quit."))    
    menu()



menu()
conn.commit()
conn.close()