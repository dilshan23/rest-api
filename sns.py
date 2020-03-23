import json
import boto3

import requests

client = boto3.client('sns')


def lambda_handler(event, context):

    topic_arn = 'arn:aws:sns:eu-west-1:566957417927:es-count-bewatchlist'
    message =  "Environment:Be-openwatchlist-dev"+"\n"+"Failed Fetchers:"+"\n"+get_count_from_es()
    client.publish(TopicArn = topic_arn,Message = message)



def get_count_from_es():

    ES_URL = 'https://search-be-watc-beattr-grvv4ybjnay-c7hud4wsts5xux6ndcuhan3xj4.eu-west-1.es.amazonaws.com'
    resp = requests.get(ES_URL+'/_cat/indices?pretty&s=index')
    print(str(resp.content))


    print(type(str(resp.content)))


    print(str(resp.content).split())



    indeices_list = str(resp.content).split()


    count_list = []

    for i in range(15,len(indeices_list),9):
        
        print(indeices_list[i])

        count_list.append(indeices_list[i])


    count_list_names = []

    for i in range(11,len(indeices_list),9):
        
        print(indeices_list[i])

        count_list_names.append(indeices_list[i])
        
    error_list = []
    for i in range(len(count_list)):
        if int(count_list[i]) == 0:
            print("error")
            error_list.append("error")
            
            
    error_list1 = [] 
    for i,j in zip(count_list,count_list_names):
        if int(i) == 0:
            error_list1.append(j)


get_count_from_es()