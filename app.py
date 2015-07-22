#we need to import request to access th e details of user


from flask import Flask,render_template,request,url_for



#initialise the flask application
app=Flask(__name__)


@app.route('/')
def form():
    return render_template('form_submit.html')




#Define a route for the action of the form ,


@app.route('/hello/',methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html',name=name)    


if __name__ == '__main__':
   app.run()      
