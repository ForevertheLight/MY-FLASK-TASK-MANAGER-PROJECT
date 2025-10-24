from flask import Flask

app=Flask(__name__)

#Our in-memory databases
users={}
tasks={}

# Auto-incrementing IDs
next_user_id=1
next_task_id=1

#Creating the User Model
#A user in this system needs five things
user = {
    'id': 1,
    'firstName': 'Joshua',
    'lastName': 'Fashola',
    'email': 'fashjosh2004@gmail.com',
    'phone': '08160840249'
}
