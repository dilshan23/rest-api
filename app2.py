
''''

In this tutorial, we are going to see how to create an API endpoint using flask. The endpoint will only accept POST request and it will use content-type application/json.




Step 2: Adding API rest endpoint
We are going to add a new endpoint that will be used to create objects. Before the hello function add the following python code
'''

from flask import request, jsonify

@app.route('/users', methods = ['POST']) 
def new_user():
    user_data = request.get_json() # 
    # add here the code to create the user
    res = {‘status’: ‘ok’}
    return jsonify(res)




'''
The hardest part to understand the previous code is the usage of the request. The request is bound to the flask context. You can think that request on the context of the post, has all the information from the request sent to the endpoint /users

For using the endpoint you need to send the json using the content-type application/json header, let’s see an example using curl:

curl --header "Content-Type: application/json"  --request POST  --data '{"username":"tutorials","password":"secret"}'  http://localhost:5000/users
Using the previous command we sent a curl POST request using the application/json header. You should see the {‘status’: ‘ok’}


'''

