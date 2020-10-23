
import redis
from random import seed
from random import random
import time
import random
import string


def randomString(stringLength=10, n = 10):
	random.seed(1)
	keyVal = []
	for x in range(n):
		letters = string.ascii_lowercase
		keyVal.append(''.join(random.choice(letters) for i in range(stringLength)))
	return keyVal

def experiment(n):
	r = redis.Redis(
    		host='192.168.64.13',
    		port=6379)

	keys = randomString(10, n)
	values = randomString(90, n)

	start_time = time.time()
	for i,key in enumerate(keys):
#		print(key, values[i])
		r.set(key, values[i])
        elapsed_time = time.time() - start_time
	print("Insert Time: ", elapsed_time)

	start_time = time.time()
	for key in keys:
		value = r.get(key)
#		print(value)
        elapsed_time = time.time() - start_time
	print("Query Time: ", elapsed_time)

	start_time = time.time()
	for key in keys:
#		print(key)
		r.delete(key)
        elapsed_time = time.time() - start_time
	print("Delete Time: ", elapsed_time)
	print("Finished expriment", n)

experiment(10)
experiment(1000)
experiment(10000)
experiment(100000)

