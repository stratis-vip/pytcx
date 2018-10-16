#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

"""Testing"""
from libs import reader
from libs.funcs import Find, FindAll

class TrainingDatabaseObject(object):
    def __init__(self, dict):
        vars(self).update(dict)

class Activity(object):
    def __init__(self, dict):
        vars(self).update(dict)

# f = open(sys.argv[1], "r")
# response_json = f.read()
# alfa = json.loads(response_json)
# td = TrainingDatabaseObject(alfa)
# # pdb.set_trace()
# act = Activity(td.TrainingCenterDatabase)
# print act.Author['Name']
# r = reader.Reader("test/error.tcx")
#
# r.read()
# r.write("json/errorTest.json")
#
#
# # print act.Activities[0]['Laps'][0]

F = open("/Users/stratis/Downloads/fb/messages/SnoetraKonstantaki_5018581a12/message.html", "r")
a = F.read()
F.close()

m = Find(r'(.+)(<div class="_4t5n" role="main">.+)(</div>.+<div class="_4t5o">.+)', a)

if m:
    beg = m.group(1)
    end = m.group(3)
    chat = m.group(2)
    G = open("message2.html", "w")
    n = chat.split('</div>\n                        </div>')
    G.write(beg)
    for i in reversed(n):
        G.write(i +'</div>\n                        </div>' )
    G.write(end)
    G.close()



