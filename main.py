from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/user_page/<name>')
def user_page(name):
    print( name + ' is a good name.')
    return render_template("schedule.html")
    #return name + 'is a good name.
    

@app.route('/route_test')
def route_test():
    print(url_for('index'))
    print(url_for('user_page',name = 'Sam'))
    

if __name__ == "__main__":
    app.run()



