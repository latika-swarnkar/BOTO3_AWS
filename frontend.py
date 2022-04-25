from backend import *
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
        imageid = request.form['imageid']
        create_instance(keyname, imageid)
        return redirect(url_for('listec2'))
    else:
        return render_template('create_ec2.html')


@ app.route("/list_ec2")
def listec2():
    # response = list_ec2()
    # return response
    response = list_ec2()
    return render_template('list_ec2.html', response=response)


@ app.route("/start", methods=['POST', 'GET'])
def startc2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        start_instance(instanceid)
        # return "Start Done"
        return redirect(url_for('listec2'))
    else:
        return render_template('ec2.html')


@ app.route("/stop", methods=['POST', 'GET'])
def stopec2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        stop_instance(instanceid)
        # return "Stop Done"
        return redirect(url_for('listec2'))
    else:
        return render_template('ec2.html')


@ app.route("/terminate", methods=['POST', 'GET'])
def terminatec2():
    if request.method == 'POST':
        instanceid = request.form['instanceid']
        terminate_instance(instanceid)
        # return "Terminate Done"
        return redirect(url_for('listec2'))
    else:
        return render_template('ec2.html')

# S3 Service home page


@ app.route("/s3")
def s3():
    return render_template('s3.html')


@ app.route("/list_bucket")
def lists3():
    buckets = list_s3()
    return render_template('list_buckets.html', buckets=buckets)


@ app.route("/create_bucket", methods=['POST', 'GET'])
def creates3():
    if request.method == 'POST':
        bucketname = request.form['bucketname']
        response = createS3_bucket(bucketname)
        print("s3 creation:", response)
        # return "Bucket created"
        return redirect(url_for('lists3'))
    else:
        return render_template('create_bucket.html')


@ app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        bucketname = request.form['bucketname']
        file_name = request.form['file_name']
        response = upload_file(file_name, bucketname)
        print("file upload response", response)
        return file_name+" uploaded"
        # return redirect(url_for('lists3'))
    else:
        return render_template('upload.html')


@ app.route("/download")
def download():
    if request.method == 'POST':
        bucketname = request.form['bucketname']
        download_files_s3(bucketname)
        return "Files Downloaded"
    else:
        return render_template('s3.html')


# This app is running on host:0.0.0.0 and  port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
