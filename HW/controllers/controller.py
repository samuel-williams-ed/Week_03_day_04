from flask import render_template, request, redirect
from app import app
from models.events_list import event_list
from models.event import Event


test_event = event_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def show():
    return render_template('index.html', event_list=test_event)

@app.route('/test', methods=['POST'])
def create():
    date = request.form['input_date']
    name = request.form['input_name']
    no_of_guests = request.form['input_no_of_guests']
    room_location = request.form['input_room_location']
    description = request.form['input_description']
    recurring = request.form['input_recurring']
    new_event = Event(date, name, no_of_guests, room_location, description, recurring)
    event_list.append(new_event)
    return redirect('/test')

