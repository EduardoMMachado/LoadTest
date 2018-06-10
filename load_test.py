#!/usr/bin/python

"""
    @author: Eduardo Maia Machado
"""

import time
import json
import global_vars
import statistics
from argparse import ArgumentParser
from request_thread import RequestThread

# Arguments Parser
parser = ArgumentParser()

parser.add_argument("-u", "--url", type=str, help="URL to be tested")
parser.add_argument("-n", "--threads_number", type=int, help="Number of threads")
parser.add_argument("-r", "--range", type=float, help="Request search range")
parser.add_argument("-m", "--max_requests", type=int, help="Number of requests")

args = parser.parse_args()

if args.url:
    global_vars.HOST = args.url
if args.threads_number:
    global_vars.N_THREADS = args.threads_number
if args.range:
    global_vars.RANGE = args.range
if args.max_requests:
    global_vars.MAX_REQUESTS = args.max_requests

# Save file name
file_name = 'Performace_test_T' + str(global_vars.N_THREADS) + '_R' + str(global_vars.RANGE) + '_M' + str(global_vars.MAX_REQUESTS) + '.json'

# Start threads
spawn_discount = 0
threads = []
for n in range(global_vars.N_THREADS):
    try:
        t = RequestThread(n, 'Thread-'+str(n))
        t.start()
        threads.append(t)
    except:
        print('\rERROR4', end='')

# Join threads
for t in threads:
    t.join()

print('\n\nRequests time average: ' + str(statistics.mean(global_vars.REQUET_TIME_LIST)))
print('Requests time standard deviation: ' + str(statistics.stdev(global_vars.REQUET_TIME_LIST)))

output = ''
for time in global_vars.REQUET_TIME_LIST:
    output += str(time) + '\n'

# Write json file
with open(file_name, 'w') as file:
    print('\nWrite json file...')
    file.write(output)
    file.close()
