class Event():
    def __init__(self, input_date,
    input_name,
    input_no_of_guests,
    input_room_location,
    input_description,
    input_recurring):
        self.date = input_date #start as a string type
        self.name = input_name
        self.guests = input_no_of_guests
        self.room_location = input_room_location
        self.description = input_description
        self.recurring = input_recurring

    
