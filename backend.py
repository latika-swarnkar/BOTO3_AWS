import boto3
import boto3
import logging
from botocore.exceptions import ClientError
import os


# to list all ec2 instances
def list_ec2():
    client = boto3.client('ec2')
    response = client.describe_instances()
    return response

# to create a new ec2 instance


def create_key_pair(keyname):
    ec2 = boto3.client('ec2')
    response_create = ec2.create_key_pair(KeyName=keyname)
    return response_create
    # print(response_create)
    # response = ec2.describe_key_pairs()e


def create_security_group(security_group_name, description):
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
    try:
        response = ec2.create_security_group(GroupName=security_group_name,
                                             Description=description,
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' %
              (security_group_id, vpc_id))

        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(e)


def delete_securitygroup(groupid):
    # Create EC2 client
    ec2 = boto3.client('ec2')
    # Delete security group
    try:
        response = ec2.delete_security_group(GroupId=groupid)
        print('Security Group Deleted')
    except ClientError as e:
        print(e)


def list_securitygroups():
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
        print(response)
    except ClientError as e:
        print(e)


def create_instance(keyname, imageid):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId=imageid,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName=keyname
    )

# to stop a ec2 instance


def stop_instance(instanceid):  # instanceid is the id of the instance to be deleted
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instanceid])

# to start ec2 instance


def start_instance(instanceid):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instanceid])

# to terminate ec2 instance


def terminate_instance(instanceid):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instanceid])


def createS3_bucket(bucket_name):  # bucket_name is the bucket name in S3
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)


def list_s3():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = response['Buckets']
    return buckets

# to retrieve the contents of a bucket


def contents_bucket(bucket_name):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    bucket_objects = my_bucket.objects.all()
    for my_bucket_object in bucket_objects:
        print(my_bucket_object)
    return bucket_objects

# upload file to bucket


def upload_file(file_name, bucket, object_name=None, ExtraArgs={'ACL': 'public-read'}):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# upload_file('pic2.png', 'mybucket-ls')  ->sample run in backend

# download all files of a bucket


def download_files_s3(bucketname):
    s3_resource = boto3.resource('s3')
    s3 = boto3.client('s3')
    list(s3_resource.buckets.all())
    # list_s3() can also be used in place of above
    bucket = s3_resource.Bucket(bucketname)
    files = list(bucket.objects.all())
    for file in files:
        s3.download_file(bucketname, file.key, file.key)
