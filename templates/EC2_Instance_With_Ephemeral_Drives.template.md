##Description
AWS CloudFormation Sample Template EC2_Instance_With_Ephemeral_Drives: Example to show how to attach ephemeral drives using EC2 block device mappings. **WARNING** This template creates an Amazon EC2 instance. You will be billed for the AWS resources used if you create a stack from this template.
##Parameters
 * **InstanceType** - WebServer EC2 instance type
  * Default: `m1.small`
  * Constraint: `must be a valid EC2 instance type.`
 * **KeyName** - Name of an existing EC2 KeyPair to enable SSH access to the web server
  * Constraint: `must be the name of an existing EC2 KeyPair.`
 * **SSHLocation** - Lockdown SSH access to the bastion host (default can be accessed from anywhere)
  * Default: `0.0.0.0/0`
  * Constraint: `must be a valid CIDR range of the form x.x.x.x/x.`


##Mappings
 * **AWSInstanceType2Arch**:
  * `(u'd2.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'm3.large', {u'Arch': u'HVM64'})`
  * `(u'r3.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.small', {u'Arch': u'PV64'})`
  * `(u'c1.medium', {u'Arch': u'PV64'})`
  * `(u'm3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u't2.small', {u'Arch': u'HVM64'})`
  * `(u'r3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'cr1.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.large', {u'Arch': u'HVM64'})`
  * `(u'c4.8xlarge', {u'Arch': u'HVM64'})`
  * `(u't1.micro', {u'Arch': u'PV64'})`
  * `(u'c3.xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.large', {u'Arch': u'PV64'})`
  * `(u'hs1.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.xlarge', {u'Arch': u'HVM64'})`
  * `(u'c3.4xlarge', {u'Arch': u'HVM64'})`
  * `(u't2.medium', {u'Arch': u'HVM64'})`
  * `(u'hi1.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'i2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c1.xlarge', {u'Arch': u'PV64'})`
  * `(u'd2.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'd2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.4xlarge', {u'Arch': u'HVM64'})`
  * `(u't2.micro', {u'Arch': u'HVM64'})`
  * `(u'm2.2xlarge', {u'Arch': u'PV64'})`
  * `(u'g2.2xlarge', {u'Arch': u'HVMG2'})`
  * `(u'r3.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'm2.xlarge', {u'Arch': u'PV64'})`
  * `(u'm1.medium', {u'Arch': u'PV64'})`
  * `(u'd2.xlarge', {u'Arch': u'HVM64'})`
  * `(u'r3.large', {u'Arch': u'HVM64'})`
  * `(u'i2.xlarge', {u'Arch': u'HVM64'})`
  * `(u'm3.medium', {u'Arch': u'HVM64'})`
  * `(u'i2.4xlarge', {u'Arch': u'HVM64'})`
  * `(u'r3.xlarge', {u'Arch': u'HVM64'})`
  * `(u'c4.large', {u'Arch': u'HVM64'})`
  * `(u'i2.2xlarge', {u'Arch': u'HVM64'})`
  * `(u'cc2.8xlarge', {u'Arch': u'HVM64'})`
  * `(u'm1.xlarge', {u'Arch': u'PV64'})`
  * `(u'm2.4xlarge', {u'Arch': u'PV64'})`
  * `(u'm3.xlarge', {u'Arch': u'HVM64'})`
 * **AWSRegionArch2AMI**:
  * `(u'us-east-1', {u'HVM64': u'ami-0d4cfd66', u'HVMG2': u'ami-5b05ba30', u'PV64': u'ami-0f4cfd64'})`
  * `(u'ap-northeast-1', {u'HVM64': u'ami-1c1b9f1c', u'HVMG2': u'ami-f644c4f6', u'PV64': u'ami-1a1b9f1a'})`
  * `(u'sa-east-1', {u'HVM64': u'ami-55098148', u'HVMG2': u'NOT_SUPPORTED', u'PV64': u'ami-5b098146'})`
  * `(u'cn-north-1', {u'HVM64': u'ami-bcc45885', u'HVMG2': u'NOT_SUPPORTED', u'PV64': u'ami-bec45887'})`
  * `(u'ap-southeast-1', {u'HVM64': u'ami-d44b4286', u'HVMG2': u'ami-12b5bc40', u'PV64': u'ami-d24b4280'})`
  * `(u'ap-southeast-2', {u'HVM64': u'ami-db7b39e1', u'HVMG2': u'ami-b3337e89', u'PV64': u'ami-ef7b39d5'})`
  * `(u'us-west-2', {u'HVM64': u'ami-d5c5d1e5', u'HVMG2': u'ami-a9d6c099', u'PV64': u'ami-d3c5d1e3'})`
  * `(u'us-west-1', {u'HVM64': u'ami-87ea13c3', u'HVMG2': u'ami-37827a73', u'PV64': u'ami-85ea13c1'})`
  * `(u'eu-central-1', {u'HVM64': u'ami-a6b0b7bb', u'HVMG2': u'ami-a6c9cfbb', u'PV64': u'ami-a4b0b7b9'})`
  * `(u'eu-west-1', {u'HVM64': u'ami-e4d18e93', u'HVMG2': u'ami-72a9f105', u'PV64': u'ami-d6d18ea1'})`


##Resources
 * **EC2Instance** - `AWS::EC2::Instance`
 * **EC2SecurityGroup** - `AWS::EC2::SecurityGroup`


##Outputs
 * **Instance** - `{u'Fn::GetAtt': [u'EC2Instance', u'PublicDnsName']}`


**Last Updated:** 2015-11-02 15:20:45.099375
