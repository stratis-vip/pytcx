#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

"""Testing"""

import sys
import os
# import cProfile
import time
from libs import reader


class Timer(object):
    def __init__(self):
        self.start = 0.0
        self.end = 0.0
        self.interval = 0.0

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


# with Timer() as t:
#     R = reader.Reader(sys.argv[1])
#     R.read()
#     F = open("%s.json" % sys.argv[1], "w")
#     F.write(R.to_json())
#     F.close()


# print 'Request took %.03f sec.' % t.interval
# cProfile.run('reader.Reader(sys.argv[1])')
# R = reader.Reader(sys.argv[1])
# cProfile.run('R.read()')
# R.read()

# if R.is_valid:
#     pass
# else:
#     print 'Error reading:', R.last_error
# # cr = Creator(None)
# # print cr.version
# print '{%s}' % R.to_json()
# # print R.author.build.to_string()
# # for act in R.activities:
# #     print act.to_json()
# # print R.activities.to_json()


if len(sys.argv) == 3 and os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
    FL = sys.argv[2]
    LIST_OF_TCXS = os.listdir(sys.argv[1])
    jsons = []
    tcxs = []
    for i in LIST_OF_TCXS:
        if i.split(".")[-1].lower() == 'tcx':
            jsons.append("%s/%s.json" % (FL, i.split(".")[0]))
            tcxs.append("%s/%s" % (sys.argv[1], i))
    # print os.path.join(sys.argv[2],b[0])
    for i, item in enumerate(tcxs):
        print("Converting %s: %d from %d" % (tcxs[i], i+1, len(tcxs)))
        R = reader.Reader(item)
        R.read()
        if R.is_valid:
            R.write(jsons[i])
        else:
            print(R.last_error)
    print ("All done!")

else:
    print("Usage: convert_tcx [folder_with_tcx's] [folder_to_save]")
    exit(1)


import MySQLdb
conn = MySQLdb.connect (host = "localhost",user = "root",passwd = "")
cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print("server version:", row[0])
cursor.close ()
conn.close ()