from flask import Flask

app=Flask(__name__)

#Our in-memory databases
users={}
tasks={}

# Auto-incrementing IDs
next_user_id=1
next_task_id=1


