From flask import Flask

app = Flask(_name_)

@app.route("/info") def 1w(): return "Welcome to LW...Heloooooo."

app.run(host='0.0.0.0')
