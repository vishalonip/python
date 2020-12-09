import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')

#List all ebs Volumes:

for vol in ec2.volumes.all():
	print vol.id, vol.state