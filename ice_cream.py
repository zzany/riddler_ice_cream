from __future__ import division
import math
import random

#define parameters
SIZE_OF_BUCKET = 100
SIZE_OF_SCOOP = 5
NUMBER_OF_FLAVORS = 31
NUM_CUSTOMERS_AHEAD = 500

buckets = [SIZE_OF_BUCKET]*NUMBER_OF_FLAVORS

#initialize popularity
#power law / Zipf distribution
fact = math.factorial(NUMBER_OF_FLAVORS)
distribution = [0]*NUMBER_OF_FLAVORS
for i in range(NUMBER_OF_FLAVORS):
	distribution[i] = fact / (i + 1)

#reset buckets
def reset_buckets():
	buckets = [SIZE_OF_BUCKET]*NUMBER_OF_FLAVORS	

#draw random bucket
def rand_bucket():
	randint = random.randrange(sum(distribution))
	currbucket = 0
	for i in range(NUMBER_OF_FLAVORS):
		if randint < 0:
			break
		else:
			currbucket = i
			randint = randint - distribution[i]
	return currbucket

def scoop_icecream():
	chosen_bucket = rand_bucket()
	current_level = buckets[chosen_bucket]
	if current_level >= SIZE_OF_SCOOP:
		buckets[chosen_bucket] = current_level - SIZE_OF_SCOOP
	else:
		buckets[chosen_bucket] = SIZE_OF_BUCKET + current_level - SIZE_OF_SCOOP

def serve_customers(num_customers):
	for i in range(num_customers):
		scoop_icecream()

def get_lowest_bucket():
	return buckets.index(min(buckets))

def run_trial():
	reset_buckets()
	serve_customers(NUM_CUSTOMERS_AHEAD)
	return get_lowest_bucket()

def run_trials(num_trials):
	results = []
	for i in range(num_trials):
		results.append(run_trial())
	return results

def return_likelihood(results, bucket):
	return results.count(bucket) / len(results)

results = run_trials(10000)
print return_likelihood(results, 0)