# BOTO3_AWS
AWS Services created using Pythob Boto3
## Steps:
1. I created the following functions in functions.py file:
     i) create ec2 instance
     ii) start ec2 instance
     iii) stop ec2 instance
     iv) terminate ec2 instance
     v) list all ec2 instances
     vi)create s3 bucket
     vii) list all the s3 bucket
     viii) upload files to the bucket
     ix) download files from a bucket
     x)update bucket policy
     xi)Retrieve bucket policy
3. Then,I created the frontend for this using flask python framework in frontend.py file.All the functions from functions.py were imported first and then route for each function are created.
4. Then for publishing the image to Dockerhub,I created a requirements.txt file and then wrote the libraries to be installed like flask and boto3.
   Then by creating the Dockerfile ,an image is built and pushed to DockerHub.
6. An EC2 instance can be created now 

