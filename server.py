from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    timestamp = datetime.now().strftime("%B %d %Y %X %p")
    total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total} fruits.")
    return render_template("checkout.html", total=total, timestamp=timestamp)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    