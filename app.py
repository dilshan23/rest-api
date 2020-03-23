from flask import Flask, request, jsonify #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    return 'Todo...'

@app.route('/form-example')
def formexample():
    return 'Todo...'

@app.route('/json-example')
def jsonexample():
    return 'Todo...'

@app.route('/query-example1')
def query_example1():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route('/form-example')
def form_example():

    if request.method == 'POST': #this block is only entered when the form is submitted
        return 'Submitted form.'

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''




    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


@app.route('/get_records')
def get_records():
    results = [
        {
          "rec_create_date": "12 Jun 2016",
          "rec_dietary_info": "nothing",
          "rec_dob": "01 Apr 1988",
          "rec_first_name": "New",
          "rec_last_name": "Guy",
        },
        {
          "rec_create_date": "1 Apr 2016",
          "rec_dietary_info": "Nut allergy",
          "rec_dob": "01 Feb 1988",
          "rec_first_name": "Old",
          "rec_last_name": "Guy",
        },
    ]
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, port=9000) #run app in debug mode on port 5000