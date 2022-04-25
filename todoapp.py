from flask import Flask, render_template, request, redirect #Imports Flask library

app =  Flask(__name__) #Creates a website in a variable called "app"

@app.route('/') #Decorator "@" is used to augment function definitions. If browser requests the address '/' (the default, or home address), then our app should route that request to this function.

def index():
    author = "Me"
    name = "David"
    return render_template('index.html', author=author, name=name) #Sends author and name variable to html

@app.route('/signup', methods = ['POST']) #We apply a decorator to the signup function, saying that we want it to be used when the browser requests /signup. It will accept the HTTP POST method, which you can see is mentioned in the HTML form element as method="post".

def signup():
    email = request.form['email'] #In the signup method we can retrieve the email address using the request object. In the HTML we used name="email", which means that in the request object we can use request.form["email"]. When we write request.form["email"] we are using request.form as a Python Dictionary
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)