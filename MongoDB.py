from pymongo import MongoClient
import random
import string
import time

def randomString(stringLength=10, n = 10):
	random.seed(1)
	keyVal = []
	for x in range(n):
		letters = string.ascii_lowercase
		keyVal.append(''.join(random.choice(letters) for i in range(stringLength)))
	return keyVal

def experiment(n):
	try:
		conn = MongoClient('192.168.64.26',27017)
		print("Connected successfully!!!")
	except:
		print("Could not connect to MongoDB")

	# database
	db = conn.test
	collection = db.sharan
	letters = string.ascii_lowercase

	keys = randomString(10, n)
	values = randomString(90, n)

	#Insert Record
	start_time=time.time()
	for i, key in enumerate(keys):
		value = values[i]
		key_val = {
        		"_id":key,
        		"value":values[i] 
    		}
		print(key)
		rec_id = collection.insert_one(key_val)
	elapsed_time=time.time()-start_time
	print("Insert Time: ", elapsed_time)

	#Query Record
	start_time = time.time()
	for key in keys:
		rec_id = collection.find({"_id":key})
		for x in rec_id:
			print(x)
	elapsed_time = time.time()-start_time
	print("Query Time: ", elapsed_time)

	#Delete Record
	start_time = time.time()
	for key in keys:
		print(key)
		rec_id = collection.delete_one({"_id":key})

	elapsed_time = time.time()-start_time
	print("Delete Time", elapsed_time)

experiment(1000)
experiment(10000)
experiment(100000
