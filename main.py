from flask import Flask, render_template
salonOnclick = Flask(__name__)

@salonOnclick.route('/')
def home():
    return render_template('base.html')
@salonOnclick.route('/contactus')
def contactus():
    return render_template('contactus.html')
@salonOnclick.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


if '__main__'== (__name__):
     salonOnclick.run(debug=1)
