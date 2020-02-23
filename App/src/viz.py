from pymnet import *
import json


filename= '/home/hassan/MultiLayerGraph/App/data/memc_1998_entities.jsons'
data=[]
for line in open(filename, 'r'):

    data.append(json.loads(line))


def singleLayer(data):
    #data= data[9:10]
    #data= data[0:1]
    data= data[0:1]
    nodes = []
    struct = []
    mnet = MultilayerNetwork(aspects= 1, fullyInterconnected=False)
    for i in data:

        d=i['entities']

        # for i in range(len(d)):
        #     if d[i]['type']== 'person':
        #         nodes.append(d[i])
        for i in range(len(d)):
            nodes.append(d[i])
            #print(d[i])



        for i in range(len(nodes)):
            if len(nodes) > 1:
                i=0
                first_node_name = nodes[i]['name']
                first_node_layer = nodes[i]['type']

                nodes.pop(i)
                for j in range(len(nodes)):

                    second_node_name = nodes[j]['name']
                    second_node_layer = nodes[j]['type']
                    struct.append([first_node_name, second_node_name, first_node_layer, second_node_layer])








    #print(data[0]['entities'])
    for i in struct:
        mnet[i[0],i[1],i[2],i[3]] =1


    #fig = draw(mnet, show=True, layout= 'spring')

    #fig = draw(er(50,3*[0.9]), show=True)
    fig = webplot(mnet,struct ,outputfile=None)


singleLayer(data)

# mnet = MultilayerNetwork(aspects=1,fullyInterconnected=False)
# mnet['sato','tanaka','work','work'] = 1
# mnet['sato','3','work','new'] = 1
# fig=draw(mnet, show=True, layout='spring')

def multiplex(data):
    data = data[0:3]

    nodes = []
    struct = []

    mnet = MultiplexNetwork(couplings="categorical", fullyInterconnected= False)
    names= ['organization','person','location']
    for elm in names:

        for i in data:

            d=i['entities']

            for i in range(len(d)):
                if d[i]['type']== elm:
                    nodes.append(d[i])
            # for i in range(len(d)):
            #     nodes.append(d[i])
            #     #print(d[i])



            for k in range(len(nodes)):
                #print (len (nodes))
                if len(nodes) == 1:
                    nodes = []
                if len(nodes) > 1:
                    k=0
                    first_node_name = nodes[k]['name']
                    first_node_layer = nodes[k]['type']

                    nodes.pop(k)
                    for j in range(len(nodes)):

                        second_node_name = nodes[j]['name']
                        second_node_layer = nodes[j]['type']
                        struct.append([first_node_name, second_node_name, first_node_layer, second_node_layer])

    # print(nodes)
    # print (struct)
    for i in struct:
        mnet[i[0],i[1],i[2],i[3]] =1




    #fig = draw(mnet,show=True)
    fig = webplot(mnet, struct, outputfile=None)


#multiplex(data)