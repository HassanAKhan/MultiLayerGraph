from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
import json
import timeit
import plotly.graph_objects as go
import numpy as np
from flask.views import MethodView
import easygui as es
from pymnet import *
import json

# Creating a Flask application
app = Flask(__name__)
api = Api(app)
CORS(app)



filename = es.fileopenbox()

#filename = '/home/hassan/MultiLayerGraph/App/data/memc_1998_entities.jsons'
entity_type = 'organization'
data = []
for line in open(filename, 'r'):

    data.append(json.loads(line))


class TotalRecords(MethodView):


    def get(self):
        # data= data[9:10]
        # data= data[0:1]
        filt= data[0:1]
        nodes = []
        struct = []
        mnet = MultilayerNetwork(aspects=1, fullyInterconnected=False)
        for i in filt:

            d = i['entities']

            # for i in range(len(d)):
            #     if d[i]['type']== 'person':
            #         nodes.append(d[i])
            for i in range(len(d)):
                nodes.append(d[i])
                # print(d[i])

            for i in range(len(nodes)):
                if len(nodes) > 1:
                    i = 0
                    first_node_name = nodes[i]['name']
                    first_node_layer = nodes[i]['type']

                    nodes.pop(i)
                    for j in range(len(nodes)):
                        second_node_name = nodes[j]['name']
                        second_node_layer = nodes[j]['type']
                        struct.append([first_node_name, second_node_name, first_node_layer, second_node_layer])

        # print(data[0]['entities'])
        for i in struct:
            mnet[i[0], i[1], i[2], i[3]] = 1

        #fig = draw(mnet, show=True, layout= 'spring')

        # fig = draw(er(50,3*[0.9]), show=True)

        return webplot(mnet, struct, outputfile=None, mult_layer= True)

api.add_resource(TotalRecords, '/alldata')





for line in open(filename, 'r'):
    data.append(json.loads(line))



def totalRecords(data):
    print('Total number of records is  ', len(data))


def types(data):
    start = timeit.default_timer()
    uniqueWords = []
    allWords = []

    for i in data:
        for j in i['entities']:
            allWords.append(j['type'])
            if (j['type']) not in uniqueWords:
                uniqueWords.append((j['type']))

    countList = []

    for i in uniqueWords:
        count = allWords.count(i)

        countList.append(i + ' ' + str(count))

    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print(countList)


def nameCount(data, entity_type):
    start = timeit.default_timer()
    uniqueWords = []
    allWords = []

    for i in data:
        for j in i['entities']:
            if (j['type']) == entity_type:
                allWords.append(j['name'])

    for i in allWords:
        if i not in uniqueWords:
            uniqueWords.append(i);

    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print(len(uniqueWords))


def spread(data):
    allWords = []

    for i in data:
        for j in i['entities']:
            if (j['type']) == entity_type:
                allWords.append(j['name'])

    uniqueWords = []

    for i in allWords:
        if i not in uniqueWords:
            uniqueWords.append(i);
    countList = []

    for i in uniqueWords:
        count = allWords.count(i)

        countList.append(str(count))

    spreadList = []
    uni = []
    for i in countList:
        spread = countList.count(i)
        if i not in uni:
            uni.append(i)
            spreadList.append({'occurrence of': i, 'count': spread})

    # return (spreadList)
    s = sorted(spreadList, key=lambda i: int(i['occurrence of']), reverse=False)
    # return len(countList)

    occ = []
    cou = []

    for i in s:
        occ.append(i['occurrence of'])
        cou.append(i['count'])

    fig = go.Figure(data=[go.Table(
        header=dict(values=['Word occurances', 'Count'],
                    line_color='darkslategray',
                    fill_color='grey',
                    align='left'),
        cells=dict(values=[occ,  # 1st column
                           cou],  # 2nd column
                   line_color='darkslategray',
                   fill_color='white',
                   align='left'))
    ])

    fig.update_layout(width=500, height=3000)
    fig.show()


def pop(data):
    org_loc_ppl_count = 0
    org_loc_count = 0
    org_ppl = 0
    loc_ppl_count = 0
    org_count = 0
    ppl_count = 0
    loc_count = 0

    for i in data:
        org = False
        loc = False
        ppl = False

        for j in i['entities']:

            if j['type'] == 'organization':
                org = True

            elif j['type'] == 'location':
                loc = True

            elif j['type'] == 'person':
                ppl = True

        if org and loc and ppl:
            org_loc_ppl_count = org_loc_ppl_count + 1

        elif org and loc and ppl == False:
            org_loc_count = org_loc_count + 1

        elif org and loc == False and ppl:
            org_ppl = org_ppl + 1

        elif org == False and loc and ppl:
            loc_ppl_count = loc_ppl_count + 1

        elif org and loc == False and ppl == False:
            org_count = org_count + 1

        elif org == False and loc and ppl == False:
            loc_count = loc_count + 1

        elif org == False and loc == False and ppl:
            ppl_count = ppl_count + 1

    print(' Organisation and location and person:   ' + str(org_loc_ppl_count), \
          '\n Organisation and location: ' + str(org_loc_count), \
          '\n Organisation and person: ' + str(org_ppl), \
          '\n Location and person: ' + str(loc_ppl_count), \
          '\n Organisation: ' + str(org_count), \
          '\n Location: ' + str(loc_count), \
          '\n Person: ' + str(ppl_count))

# totalRecords(data)

