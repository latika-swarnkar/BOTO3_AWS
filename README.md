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

    x)Retrieve contents of a bucket
    
    xi)Create Key Pair


2. Then,I created the frontend for this using flask python framework in frontend.py file.All the functions from functions.py were imported  first and then route for each function are created.

3. Then for publishing the image to Dockerhub,I created a requirements.txt file and then wrote the libraries to be installed like flask and  boto3. 
Then by creating the Dockerfile ,an image is built and pushed to DockerHub.(https://hub.docker.com/repository/docker/latika25/aws_boto3)

4.I have also pushed this code on github.(https://github.com/latika-swarnkar/BOTO3_AWS)

5. Then,I created an EC2 instance and connected it through SSh.I first installed docker,pulled the image from docker hub and created a container.Go to <public_ipv4_ec2>:5001 to see the app.

## Commands Used:(all the dependencies(docker,python3,flask,etc) already installed)

1.To run application:

    python3 frontend.py
    
    By pm2:(have not included this command in Dockerfile)
    
        pm2 start frontend.py --interpreter python3
        
2.Docker Commands:

    To build image:
    
        sudo docker build -t latika25/aws_boto3:v1 .
        
    To push this image on DockerHub:
    
        sudo docker push latika25/aws_boto3:v1
        
3.For hosting on Ec2:

    i)Install Docker (https://docs.docker.com/engine/install/ubuntu/)
    
    ii)sudo docker login
    
    iii)sudo docker pull latika25/aws_boto3:v1 .
    
    iv)To run container out of this image:
            sudo docker run --name myboto -p 5001:5001 --env REGION=us-east-1 --env ACCESS_KEY=AKIAX24HVZXMN3KZFUX6  --env      SECURITY_KEY=TjDnM439E4ewVYNrmfRmVgop5D/znkv/cVz1AcIU --env OUTPUT=json latika25/boto3_aws:v1  
            OR
            sudo docker run --name myboto -p 5001:5001 latika25/boto3_aws:v1     
    v)Go to <public_ipv4_ec2>:5001

## Sample Inputs:

1. For creating EC2 instance:

    Enter any existing key-pair name ='ec2-instance' ,
    
    Enter ami id='ami-04505e74c0741db8d'(For Ubuntu Machine)
    
2. For starting/stopping/terminating an instance

    Give instanceid='i-081765edf56'
   
3. For creating S3 bucket

   Give Bucket name='mybucket-latika'

## Output FrontEnd:
### 1.Home Page
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/Home.png?raw=true)
### 2.EC2 Service Home Page
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/EC2ServiceHome1.png?raw=true)
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/EC2ServiceHome2.png?raw=true)
### 3.S3 Service Home Page
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/s3_home.png?raw=true)
### 4.Create New Key-Pair
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/create_key_pair.png?raw=true)
### 5.Creating EC2 Instance
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/create_ec2_instance.png?raw=true)
### 6.Listing EC2 Instance
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/list_ec2_instances.png?raw=true)
### 7.Stopping/Starting/Terminating EC2 Instance
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/EC2ServiceHome2.png?raw=true)
### 8.Listing after stopping a instance
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/list_instances_after_stopped.png?raw=true)
### 9.Create S3 Bucket
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/creates3Bucket.png?raw=true)
### 10.Uploading Files in a Bucket
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/uploadfileto_bucket.png?raw=true)
### 11.Downloading Files in Bucket
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/downloadingFilesFromBucket.png?raw=true)
### 12.Lists S3 Bucket
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/listallBuckets.png?raw=true)
### 13.Show Items of a Bucket
![alt text](https://github.com/latika-swarnkar/BOTO3_AWS/blob/master/output_images/show_items_of_bucket.png?raw=true)












