from flask import  Flask, render_template, jsonify, request, make_response
import json
from pymnet import *
import easygui as es
app = Flask(__name__)
app.debug = True

#filename = '/home/hassan/MultiLayerGraph/App/data/memc_1998_entities.jsons'
# filename = es.fileopenbox()
# entity_type = 'organization'
# file_data = []
# for line in open(filename, 'r'):
#
#     file_data.append(json.loads(line))
#
#
#
file_data = []


def totalRecords(data):
    print('Total number of records is  ', len(data))
    return(len(data))

def types(data):

    uniqueWords = []
    allWords = []

    for i in data:
        for j in i['entities']:
            allWords.append(j['type'])
            if (j['type']) not in uniqueWords:
                uniqueWords.append((j['type']))

    countList = {}

    for i in uniqueWords:
        count = allWords.count(i)

        countList[i] = str(count)



    return(countList)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.loads(request.data)
        if data == 'selectFile':
            filename = es.fileopenbox()

            for line in open(filename, 'r'):
                file_data.append(json.loads(line))

        unique_words = types(file_data)
        total_records= totalRecords(file_data)
        print (unique_words)
        print ('---------')
        print(total_records)
        return (render_template('index.html'))

    else:
        return render_template('index.html')

@app.route('/python', methods=['GET', 'POST'])
def pthonImplemntation():
    # data= data[9:10]
    # data= data[0:1]
    filt = file_data[0:2]
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

    fig = draw(mnet, show=True, layout= 'spring')

    # fig = draw(er(50,3*[0.9]), show=True)
    return  render_template('index.html')


@app.route('/data')
def sum_num():

        # data= data[9:10]
        # data= data[0:1]
        filt = file_data[0:2]
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

        # fig = draw(mnet, show=True, layout= 'spring')

        # fig = draw(er(50,3*[0.9]), show=True)



        return  render_template('something.html', file_data = webplot(mnet, struct, outputfile=None, mult_layer=True))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)