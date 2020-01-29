from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/polyhax")
def ph():
    return render_template('polyhacks.html')
    
if __name__ == "__main__":
    app.run(debug=True)
