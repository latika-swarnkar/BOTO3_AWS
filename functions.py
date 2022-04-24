import glob
import boto3
import json
# glob library is used to find the files(used in upload function of bucket)
# here ,we have used json to covert the dictionary to json object(in update bucket policy)


def list_ec2():
    # first create the ec2 client
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    # response now contains the list of instances
    return (response)


def create_instance(keyname, filename, imageid, groupname):
    ec2 = boto3.client('ec2')

    # Step1:
    # first create the new key-pair as we do by ui in aws
    resp = ec2.create_key_pair(KeyName=keyname)
    # filename is a name of file to be downloaded which contains the key.
    # This filename is with .pem extension
    file = open(filename, 'w')
# we are just writing the ketMaterial(which contains the actual key) out of many attributes present in resp object
    file.write(resp['KeyMaterial'])
    file.close()

    # Step2:
    # Create Security Group
    resp_security = ec2.describe_security_groups()
    description = 'This is ec2 instance with keyname='+keyname
    response = ec2.create_security_group(
        GroupName=groupname, Description=description, VpcId=resp_security['VpcId'])
    gid = response['GroupId']
    ec2.authorize_security_groups_ingress(
        GroupId=gid,
        IpPermissions=[{
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
            {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
        ]
    )

    # Step3:
    # Create EC2
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(
        ImageId=imageid,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=keyname,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebc': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 20
                }
            }
        ],
        SecurityGroups=[groupname]
    )
    print(instances)


def stop_instance(instanceid):  # instanceid is the id of the instance to be deleted
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instanceid])


def start_instance(instanceid):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instanceid])


def terminate_instance(instanceid):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instanceid])


def createS3_bucket(name):  # name is the bucket name in S3
    # first create the s3 client
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=name)


def list_s3():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return (response)
    # print(response['Buckets'])


def upload_files(filename, bucket, object_name=None, args=None):
    '''
    filename is name of file on my local machine
    bucket:s3 bucket name
    object_name=name of file object on s3
    args:custom args(to make the object public,etc)
    '''
    if object_name is None:
        object_name = filename
    s3 = boto3.client('s3')
    response = s3.upload_file(filename, bucket, object_name, ExtraArgs=args)
    print(response)

# upload_files('data/f1.jpg','Bucketname')


def uploadlist_of_files(bucketname):
    files = glob.glob('data/*')
    args = {'ACL': 'public-read'}
    for file in files:
        upload_files(file, bucketname, args=args)
        print(uploaded, file)


def download_files_s3(bucketname):
    s3_resource = boto3.resource('s3')
    s3 = boto3.client('s3')
    list(s3_resource.buckets.all())
    # list_s3() can also be used in place of above
    bucket = s3_resource.Bucket(bucketname)
    files = list(buxket.objects.all())
    for file in files:
        s3.download_file(bucketname, file.key, file.key)


def update_bucketpolicy(bucket_policy):
    bucket_policy = json.dumps(bucket_policy, bucket_name)
    s3 = boto3.client('s3')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


def Retrieve_policy(bucket_name):
    s3 = boto3.client('s3')
    s3.get_bucket_policy(Bucket=bucket_name2)
