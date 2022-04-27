import json
import re
from flask import Flask, render_template, request, flash, redirect,url_for

app = Flask(__name__)
app.secret_key = 'f3cfe9ed8fae309f02079dbf'

#load input from file
with open('outputfile.json') as file:
    todolist = json.load(file)


@app.route('/')
def home():
    """Home route"""
    todo=todolist
    #render the index page
    return render_template('index.html',todolist=todo)


@app.route("/submit",methods=["post"])
def submit():
    """Function to receive Post data"""
    errors=[] #list to hold errors

    #get data
    email=request.form['email']
    task=request.form['task']
    priority=request.form['priority']

    input_priority=['low','medium', 'high']
    #validation
    email_regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not (re.search(email_regex,email)): #validation for email
        errors.append('Invalid Email')
    
    if priority not in input_priority: #validation for priority
        errors.append('Invalid Priority')

    if len(errors)>0:
        for i in errors:
            flash(i)
        return redirect(url_for('home'))
    else:
        dictionary=dict()
        if len(todolist)>0:
            dictionary["id"] = todolist[len(todolist)-1]["id"]+1
        else:
            dictionary["id"] = 1
        dictionary["task"]=task
        dictionary["email"]=email
        dictionary["priority"]=priority
        todolist.append(dictionary)

        return redirect(url_for('home'))

@app.route("/delete/<id>")
def delete(id):
    """Function to delete a task"""
    for x in range(0,len(todolist)):
        if todolist[x]["id"]==int(id):
            todolist.pop(x)             
    return redirect(url_for('home'))

@app.route("/clear", methods=["post"])
def clear():
    """Function to clear the tasks"""
    todolist.clear()
    return redirect(url_for('home'))

@app.route("/save")
def save():
    """Function to clear the tasks"""
    with open('outputfile.json', 'w') as fout:
        json.dump(todolist, fout)
    flash("Your To do tasks have been saved")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)