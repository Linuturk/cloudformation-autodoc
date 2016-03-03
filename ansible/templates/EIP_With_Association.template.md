
## Description

AWS CloudFormation Sample Template Sample template EIP_With_Association: This template shows how to associate an Elastic IP address with an Amazon EC2 instance - you can use this same technique to associate an EC2 instance with an Elastic IP Address that is not created inside the template by replacing the EIP reference in the AWS::EC2::EIPAssoication resource type with the IP address of the external EIP. **WARNING** This template creates an Amazon EC2 instance and an Elastic IP Address. You will be billed for the AWS resources used if you create a stack from this template.
## Insert



This is an insert into the automatically generated documentation.



**Feel free to use Markdown!**



Use this type of file to insert more details on a template that can't fit into the usual description. Feel free to use images to document the architecture your template deploys.


## Parameters

 * **InstanceType** - WebServer EC2 instance type
  * Default: `t2.small`
  * Constraint: `must be a valid EC2 instance type.`
 * **KeyName** - Name of an existing EC2 KeyPair to enable SSH access to the instances
  * Constraint: `must be the name of an existing EC2 KeyPair.`
 * **SSHLocation** - The IP address range that can be used to SSH to the EC2 instances
  * Default: `0.0.0.0/0`
  * Constraint: `must be a valid IP CIDR range of the form x.x.x.x/x.`

## Mappings

 * **AWSInstanceType2Arch**:
  * `(u'd2.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'g2.8xlarge', {u'Arch': u'HVMG2'})`
  * `(u'm3.large', {u'Arch': u'HVM64'})`
  * `(u'cc2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'r3.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.small', {u'Arch': u'PV64'})`
  * `(u'c1.medium', {u'Arch': u'PV64'})`
  * `(u'm3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u't2.small', {u'Arch': u'HVM64'})`
  * `(u'r3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u't1.micro', {u'Arch': u'PV64'})`
  * `(u'cr1.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.large', {u'Arch': u'HVM64'})`
  * `(u'c4.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.large', {u'Arch': u'PV64'})`
  * `(u'hs1.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'm4.large', {u'Arch': u'HVM64'})`
  * `(u't2.medium', {u'Arch': u'HVM64'})`
  * `(u't2.nano', {u'Arch': u'HVM64'})`
  * `(u'hi1.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'i2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c1.xlarge', {u'Arch': u'PV64'})`
  * `(u'd2.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'd2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.4xlarge', {u'Arch': u'HVM64'})`
  * `(u't2.micro', {u'Arch': u'HVM64'})`
  * `(u'm2.2xlarge', {u'Arch': u'PV64'})`
  * `(u'm4.xlarge', {u'Arch': u'HVM64'})`
  * `(u'g2.2xlarge', {u'Arch': u'HVMG2'})`
  * `(u'r3.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'm2.xlarge', {u'Arch': u'PV64'})`
  * `(u'm4.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.medium', {u'Arch': u'PV64'})`
  * `(u'd2.xlarge', {u'Arch': u'HVM64'})`
  * `(u'r3.large', {u'Arch': u'HVM64'})`
  * `(u'i2.xlarge', {u'Arch': u'HVM64'})`
  * `(u'm3.medium', {u'Arch': u'HVM64'})`
  * `(u't2.large', {u'Arch': u'HVM64'})`
  * `(u'c3.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'r3.xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.large', {u'Arch': u'HVM64'})`
  * `(u'm4.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'i2.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'i2.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.xlarge', {u'Arch': u'PV64'})`
  * `(u'm4.10xlarge', {u'Arch': u'HVM64'})`
  * `(u'm2.4xlarge', {u'Arch': u'PV64'})`
  * `(u'm3.xlarge', {u'Arch': u'HVM64'})`
 * **AWSInstanceType2NATArch**:
  * `(u'd2.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'g2.8xlarge', {u'Arch': u'NATHVMG2'})`
  * `(u'm3.large', {u'Arch': u'NATHVM64'})`
  * `(u'cc2.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'r3.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm1.small', {u'Arch': u'NATPV64'})`
  * `(u'c1.medium', {u'Arch': u'NATPV64'})`
  * `(u'm3.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u't2.small', {u'Arch': u'NATHVM64'})`
  * `(u'r3.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u't1.micro', {u'Arch': u'NATPV64'})`
  * `(u'cr1.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c3.large', {u'Arch': u'NATHVM64'})`
  * `(u'c4.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c3.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm1.large', {u'Arch': u'NATPV64'})`
  * `(u'hs1.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c3.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c4.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c3.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm4.large', {u'Arch': u'NATHVM64'})`
  * `(u't2.medium', {u'Arch': u'NATHVM64'})`
  * `(u't2.nano', {u'Arch': u'NATHVM64'})`
  * `(u'hi1.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'i2.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c1.xlarge', {u'Arch': u'NATPV64'})`
  * `(u'd2.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'd2.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c4.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u't2.micro', {u'Arch': u'NATHVM64'})`
  * `(u'm2.2xlarge', {u'Arch': u'NATPV64'})`
  * `(u'm4.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'g2.2xlarge', {u'Arch': u'NATHVMG2'})`
  * `(u'r3.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c4.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm2.xlarge', {u'Arch': u'NATPV64'})`
  * `(u'm4.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm1.medium', {u'Arch': u'NATPV64'})`
  * `(u'd2.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'r3.large', {u'Arch': u'NATHVM64'})`
  * `(u'i2.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm3.medium', {u'Arch': u'NATHVM64'})`
  * `(u't2.large', {u'Arch': u'NATHVM64'})`
  * `(u'c3.8xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'r3.xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'c4.large', {u'Arch': u'NATHVM64'})`
  * `(u'm4.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'i2.2xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'i2.4xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm1.xlarge', {u'Arch': u'NATPV64'})`
  * `(u'm4.10xlarge', {u'Arch': u'NATHVM64'})`
  * `(u'm2.4xlarge', {u'Arch': u'NATPV64'})`
  * `(u'm3.xlarge', {u'Arch': u'NATHVM64'})`
 * **AWSRegionArch2AMI**:
  * `(u'us-east-1', {u'HVM64': u'ami-60b6c60a', u'HVMG2': u'ami-e998ea83', u'PV64': u'ami-5fb8c835'})`
  * `(u'ap-northeast-1', {u'HVM64': u'ami-383c1956', u'HVMG2': u'ami-08e5c166', u'PV64': u'ami-393c1957'})`
  * `(u'ap-southeast-2', {u'HVM64': u'ami-48d38c2b', u'HVMG2': u'ami-0c1a446f', u'PV64': u'ami-ced887ad'})`
  * `(u'sa-east-1', {u'HVM64': u'ami-6817af04', u'HVMG2': u'NOT_SUPPORTED', u'PV64': u'ami-7d15ad11'})`
  * `(u'cn-north-1', {u'HVM64': u'ami-43a36a2e', u'HVMG2': u'NOT_SUPPORTED', u'PV64': u'ami-18ac6575'})`
  * `(u'ap-southeast-1', {u'HVM64': u'ami-c9b572aa', u'HVMG2': u'ami-5a15d239', u'PV64': u'ami-34bd7a57'})`
  * `(u'ap-northeast-2', {u'HVM64': u'ami-249b554a', u'HVMG2': u'NOT_SUPPORTED', u'PV64': u'NOT_SUPPORTED'})`
  * `(u'us-west-2', {u'HVM64': u'ami-f0091d91', u'HVMG2': u'ami-315f4850', u'PV64': u'ami-d93622b8'})`
  * `(u'us-west-1', {u'HVM64': u'ami-d5ea86b5', u'HVMG2': u'ami-943956f4', u'PV64': u'ami-56ea8636'})`
  * `(u'eu-central-1', {u'HVM64': u'ami-bc5b48d0', u'HVMG2': u'ami-ba1a09d6', u'PV64': u'ami-794a5915'})`
  * `(u'eu-west-1', {u'HVM64': u'ami-bff32ccc', u'HVMG2': u'ami-83fd23f0', u'PV64': u'ami-95e33ce6'})`

## Resources

 * **EC2Instance** - `AWS::EC2::Instance`
 * **IPAddress** - `AWS::EC2::EIP`
 * **IPAssoc** - `AWS::EC2::EIPAssociation`
 * **InstanceSecurityGroup** - `AWS::EC2::SecurityGroup`

## Outputs

 * **InstanceIPAddress** - `{u'Ref': u'IPAddress'}`
 * **InstanceId** - `{u'Ref': u'EC2Instance'}`