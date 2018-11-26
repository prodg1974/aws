import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

#print (response)


ec2_2 = boto3.resource('ec2')

ids=[]
instances = ec2_2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type, instance.public_ip_address
          ,instance.public_dns_name,instance.root_device_name
          ,instance.root_device_type, instance.state)
    ids.append(instance.id)

#ec2_2.instances.filter(InstanceIds=ids).start()
