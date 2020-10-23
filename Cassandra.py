from cassandra.cluster import Cluster
from cassandra.query import tuple_factory, BatchStatement, ConsistencyLevel, SimpleStatement
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
	cluster = Cluster(["192.168.64.13"])
	session = cluster.connect('test')

	keys = randomString(10, n)
	values = randomString(90, n)

	start_time = time.time()
	insert_user = session.prepare("INSERT INTO myTable (key, value) VALUES (?, ?)")
	for i,key in enumerate(keys):
		batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
#		print(key, values[i])
		batch.add(insert_user,(key, values[i]))
		session.execute(batch)
        elapsed_time = time.time() - start_time
	print("Insert Time: ", elapsed_time)

	start_time = time.time()
	value = ""
	for key in keys:
		query = SimpleStatement("SELECT value from myTable where key='{key1}';".format(key1=key), consistency_level=ConsistencyLevel.ONE)
		results = session.execute(query)
#		for x in results:
#			print(x.value)
        elapsed_time = time.time() - start_time
	print("Query Time: ", elapsed_time)

	start_time = time.time()
	for key in keys:
#		print(key)
		query = SimpleStatement("DELETE FROM myTable WHERE key='{key1}';".format(key1=key), consistency_level=ConsistencyLevel.ONE)
		result = session.execute(query)
        elapsed_time = time.time() - start_time
	print("Delete Time: ", elapsed_time)
	print("Finished expriment", n)

#experiment(10)
experiment(1000)
experiment(10000)
experiment(100000)
