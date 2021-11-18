import bottle

app = bottle.Bottle(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
    