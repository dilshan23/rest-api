import boto3


#read

session = boto3.session.Session(profile_name = 'prodaccess')


s3= session.resource('s3')


for bucket in s3.buckets.all():

    print(bucket.name)

    '''

Retrieving a List From S3 Bucket
The list is stored as a stream object inside Body. It can be read using read() API of the get_object() returned value. It can throw an "NoSuchKey" exception if the key is not present.

import boto3
import pickle
#Connect to S3
s3 = boto3.client('s3')
#Read the object stored in key 'myList001'
object = s3.get_object(Bucket='mytestbucket',Key='myList001')
serializedObject = object['Body'].read()
#Deserialize the retrieved object
myList = pickle.loads(serializedObject)
print myList


'''


import json

myData = {'firstName':'Saravanan','lastName':'Subramanian','title':'Manager', 'empId':'007'}
data = json.dumps(myData)
s3.put_object(Bucket='dd-testbucket',body = 'data',Key='EmpId007')


#s3.Bucket('dd-testbucket').put_object(Key= 'EmpId007', Body=data)