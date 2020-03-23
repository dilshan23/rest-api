import json
import boto3

session = boto3.session.Session(profile_name = 'prodaccess')


s3= session.resource('s3')


myData = {'firstName':'Saravanan','lastName':'Subramanian','title':'Manager', 'empId':'007'}
data = json.dumps(myData)
s3.Bucket('dd-testbucket').put_object(Key= 'EmpId007', Body=data)
