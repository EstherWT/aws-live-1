from flask import Flask, render_template, request, url_for
from pymysql import connections
import os
import boto3

customhost = "database-1.czj7uvclfwmy.us-east-1.rds.amazonaws.com"
customuser = "admin"
custompass = "admin123"
customdb = "internshipDB"
custombucket = "bucket-internship1"
customregion = "us-east-1"


app = Flask(__name__, static_folder='assets')

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}


@app.route("/", methods=['GET'])
def dconn.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()isplay_internship():

    statement = "SELECT * FROM Internship"
    cursor = db_
    cursor.close()

    return render_template('index.html', internship = result)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
