from functions import *
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

# Home Page


@app.route("/")
def index():
    return render_template('index.html')

# Ec2 Service home page


@app.route("/ec2")
def ec2():
    return render_template('ec2.html')


# Page for creating new ec2 instance
@app.route("/new_ec2", methods=['POST', 'GET'])
def createc2():
    if request.method == 'POST':
        keyname = request.form['keyname']
        filename = keyname+'.pem'
        imageid = request.form['imageid']
        groupname = request.form['groupname']
        create_instance(keyname, filename, imageid, groupname)
        return redirect(url_for('list_ec2', name=listec2))
    else:
        return render_template('create_ec2.html')


@ app.route("/list_ec2")
def listec2():
    response = list_ec2()
    return response


@ app.route("/start", methods=['POST', 'GET'])
def startc2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        start_instance(instanceid)
        return redirect(url_for('list_ec2', name=listec2))
    else:
        return render_template('ec2.html')


@ app.route("/stop", methods=['POST', 'GET'])
def stopec2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        stop_instance(instanceid)
        return redirect(url_for('list_ec2', name=listec2))
    else:
        return render_template('ec2.html')


@ app.route("/terminate", methods=['POST', 'GET'])
def terminatec2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        terminate_instance(instanceid)
        return redirect(url_for('list_ec2', name=listec2))
    else:
        return render_template('ec2.html')

# S3 Service home page


@ app.route("/s3")
def s3():
    return render_template('s3.html')


@ app.route("/list_bucket")
def lists3():
    response = list_s3()
    return response


@ app.route("/create_bucket", methods=['POST', 'GET'])
def creates3():
    if request.method == 'POST':
        bucketname = request.form['bucketname']
        createS3_bucket(bucketname)
        return redirect(url_for('list_bucket', name=lists3))
    else:
        return render_template('create_bucket.html')


@ app.route("/upload")
def upload():
    return render_template('s3.html')


@ app.route("/download")
def download():
    return render_template('s3.html')


# This app is running on host:0.0.0.0 and  port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
