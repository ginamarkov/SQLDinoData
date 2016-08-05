import csv
import wikipedia as w
import sys
import sqlite3

conn = sqlite3.connect("Dino.db")
c = conn.cursor()

def menu ():
	print("Hello! Welcome to our Dino database. Here is some information from wikipedia about dinos. \n\n")
	print (w.summary("Dinosaurs", sentences=5))
	choice = (int(raw_input(" \n\n You can learn about many things.\n\t If you want to learn about the diet of dinosaurs and how it correlates with their region, type 1. \n\t If you want to know how many dinos walk on two versus four legs, type 2.  \n\t Finally, if you want to know when and by whom each dino was discovered, type 3. \n\t If you want to quit, type 4.")))
	while choice != 4:
		if choice == 1:
			query1()
		elif choice == 2:
			print "query2"
		elif choice == 3:
			print "query3"
		else:
			choice = (int(raw_input("Choice not available. Please choose a real query. If you want to quit, type 4")))
	print ("Goodbye!")
	sys.exit(0)


def query1():
	user_diet = (raw_input("Choose what diet to learn about - carnivorous, herbivorous, omnivorous, or herbivorous/omnivorous. If you want to quit, type quit.").lower())
	while user_diet!="quit"
		user_limit = raw_input("How many dinos do you want to know this about?")
		c.execute('SELECT BigTable.Name, Location.Location, Diet.Diet FROM BigTable '\
				+'JOIN Location ON BigTable.Location_ID = Location.Location_ID '\
				+'JOIN Diet ON BigTable.Diet_ID = Diet.Diet_ID '\
				+'GROUP BY Diet.Diet, Location.Location '\
				+'LIMIT('+user_limit+')')
				

		bigList = [[str(item) for item in results] for results in c.fetchall()]


		for item in bigList:
			if item[2] == user_diet:
				print "The " +item[0]+ " is " +item[2]+ " and is found in " +item[1]
	menu()
					

query1()





conn.commit()
conn.close()

