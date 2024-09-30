from troposphere import Base64, FindInMap, GetAtt, Join
from troposphere import Output, Parameter, Ref, Template
from troposphere.ec2 import Instance, NetworkInterfaceProperty, SecurityGroup
from troposphere.ec2 import SecurityGroupRule

# Create a new CloudFormation template
t = Template()

# Create a security group resource
# This security group allows SSH and ICMP traffic
sg = t.add_resource(SecurityGroup(
    "MySecurityGroup",
    GroupDescription="Allow SSH and ICMP traffic",
    SecurityGroupIngress=[
        SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        ),
        SecurityGroupRule(
            IpProtocol="icmp",
            FromPort="8",
            ToPort="-1",
            CidrIp="0.0.0.0/0",
        ),
    ],
))

# Create an EC2 instance resource
instance = t.add_resource(Instance(
    "MyInstance",
    ImageId="ami-0c55b159cbfafe1f0",
    InstanceType="t2.micro",
    KeyName="mykeypair",
    NetworkInterfaces=[
        NetworkInterfaceProperty(
            GroupSet=[Ref(sg)],
            AssociatePublicIpAddress="true",
            DeviceIndex="0",
            DeleteOnTermination="true",
            SubnetId="subnet-abcde012",
        ),
    ],
))

# Print the CloudFormation template in YAML format
print(t.to_yaml())