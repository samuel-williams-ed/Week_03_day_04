# request - a flask object that allows is to access pyaloads sent from browsers
# when browsers send a 'POST'
from flask import render_template, request, redirect
from app import app
from models.todo_list import tasks
from models.task import Task


@app.route('/')
def index_home():
    return render_template('home.html')

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)

# defining the page where URL and a method is being called
# called 'create' because of RESTful convention
@app.route('/tasks', methods=['POST'])
def create():
    # We access the data being sent from 'POST' by using the 'request' flask library object
    print("###################")
    print(request.form)
    
    # from the received data store the value from the dict under 'title' 
    # accessing key form 'input' form in HTML
    accessed_title = request.form['user_sent_title']
    print(accessed_title)
    accessed_description = request.form['user_sent_description']
    print(accessed_description)
    
    # take data from the form and create a new task
    # NB as soon as we make a change to file and refresh HTML the data will reset to initial state
    new_task = Task(accessed_title, accessed_description, True)
    Task.add_task(new_task)
    # allows modular adding of a task. 
    # logic for new tasks is kept within the Task class

    # # when the create() fucntion is called we return the homepage - temp, for tidiness
    # return index()

    # redirect will make a new GET request
    #  redirect will load the page without starting up any functions again
    return redirect('/tasks')