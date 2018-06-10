#!/usr/bin/python

"""
    @author: Eduardo Maia Machado
"""

import requests
import time
import threading
import random
import global_vars

class RequestThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            global_vars.CURRENT_REQUEST += 1
            if global_vars.CURRENT_REQUEST > global_vars.MAX_REQUESTS:
                print('\rEXIT', end='')
                exit()

            params = {
                'range_start': round(global_vars.RANGE, 2),
                'range_end': round(global_vars.RANGE + 0.5, 2)
            }

            global_vars.RANGE = random.random() * 100000

            try:
                print('\rREQUESTS: ' + str(global_vars.CURRENT_REQUEST) + ' RESPONSES: ' + str(global_vars.CURRENT_RESPONSE), end='')
                r = requests.get(global_vars.HOST, params=params)

                if r.status_code == 200:
                    global_vars.CURRENT_RESPONSE += 1
                    global_vars.REQUET_TIME_LIST.append(r.elapsed.total_seconds())
                else:
                    print('\rERROR2', end='')  # Status != 200

            except Exception:
                print('\rERROR3', end='')  # Other fail
                exit()
