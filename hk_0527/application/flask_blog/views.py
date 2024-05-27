from flask_blog import app

@app.route('/')
def show_entries():
    return f'Hello World! My name is Tyson'