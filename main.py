from flask import Flask, render_template
salonOnclick = Flask(__name__)

@salonOnclick.route('/')
def home():
    return render_template('index.html')


if '__main__'== (__name__):
     salonOnclick.run(debug=1)
