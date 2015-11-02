##Description
AWS CloudFormation Sample Template ElasticBeanstalk_in_VPC: Sample template showing how to create an Elastic Beanstalk environment in a VPC. The stack contains 2 subnets: the first subnet is public and contains the load balancer, a NAT device for internet access from the private subnet and a bastion host to allow SSH access to the Elastic Beanstalk hosts. The second subnet is private and contains the Elastic Beanstalk instances. You will be billed for the AWS resources used if you create a stack from this template.
##Parameters
 * **BastionInstanceType** - Bastion Host EC2 instance type
  * Default: `m1.small`
  * Constraint: `must be a valid EC2 instance type.`
 * **BastionKeyName** - Name of an existing EC2 KeyPair to enable SSH access to the bastion host
  * Constraint: `must be the name of an existing EC2 KeyPair.`
 * **KeyName** - Name of an existing EC2 KeyPair to enable SSH access to the Elastic Beanstalk hosts
  * Constraint: `must be the name of an existing EC2 KeyPair.`
 * **NATInstanceType** - NAT Device EC2 instance type
  * Default: `m1.small`
  * Constraint: `must be a valid EC2 instance type.`
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
 * **AWSNATRegionArch2AMI**:
  * `(u'us-east-1', {u'NATHVM64': u'ami-b0210ed8', u'NATPV64': u'ami-c02b04a8'})`
  * `(u'ap-northeast-1', {u'NATHVM64': u'ami-11dc2a11', u'NATPV64': u'ami-c7e016c7'})`
  * `(u'sa-east-1', {u'NATHVM64': u'ami-63fa417e', u'NATPV64': u'ami-93fb408e'})`
  * `(u'cn-north-1', {u'NATHVM64': u'ami-be3fad87', u'NATPV64': u'ami-bc3fad85'})`
  * `(u'ap-southeast-1', {u'NATHVM64': u'ami-1a9dac48', u'NATPV64': u'ami-b098a9e2'})`
  * `(u'ap-southeast-2', {u'NATHVM64': u'ami-43ee9e79', u'NATPV64': u'ami-0fed9d35'})`
  * `(u'us-west-2', {u'NATHVM64': u'ami-75ae8245', u'NATPV64': u'ami-2dae821d'})`
  * `(u'us-west-1', {u'NATHVM64': u'ami-ada746e9', u'NATPV64': u'ami-67a54423'})`
  * `(u'eu-central-1', {u'NATHVM64': u'ami-1e073a03', u'NATPV64': u'ami-3604392b'})`
  * `(u'eu-west-1', {u'NATHVM64': u'ami-ef76e898', u'NATPV64': u'ami-cb7de3bc'})`
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
 * **Region2Principal**:
  * `(u'us-east-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'ap-northeast-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'sa-east-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'eu-central-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'ap-southeast-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'ap-southeast-2', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'us-west-2', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'us-west-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
  * `(u'cn-north-1', {u'EC2Principal': u'ec2.amazonaws.com.cn', u'OpsWorksPrincipal': u'opsworks.amazonaws.com.cn'})`
  * `(u'eu-west-1', {u'EC2Principal': u'ec2.amazonaws.com', u'OpsWorksPrincipal': u'opsworks.amazonaws.com'})`
 * **SubnetConfig**:
  * `(u'Private', {u'CIDR': u'10.0.1.0/24'})`
  * `(u'Public', {u'CIDR': u'10.0.0.0/24'})`
  * `(u'VPC', {u'CIDR': u'10.0.0.0/16'})`


##Resources
 * **BastionHost** - `AWS::EC2::Instance`
 * **BastionIPAddress** - `AWS::EC2::EIP`
 * **BastionSecurityGroup** - `AWS::EC2::SecurityGroup`
 * **BeanstalkSecurityGroup** - `AWS::EC2::SecurityGroup`
 * **GatewayToInternet** - `AWS::EC2::VPCGatewayAttachment`
 * **InboundEphemeralPublicNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **InboundHTTPPublicNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **InboundHTTPSPublicNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **InboundPrivateNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **InboundSSHPublicNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **InternetGateway** - `AWS::EC2::InternetGateway`
 * **NATDevice** - `AWS::EC2::Instance`
 * **NATIPAddress** - `AWS::EC2::EIP`
 * **NATSecurityGroup** - `AWS::EC2::SecurityGroup`
 * **OutBoundPrivateNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **OutboundPublicNetworkAclEntry** - `AWS::EC2::NetworkAclEntry`
 * **PrivateNetworkAcl** - `AWS::EC2::NetworkAcl`
 * **PrivateRoute** - `AWS::EC2::Route`
 * **PrivateRouteTable** - `AWS::EC2::RouteTable`
 * **PrivateSubnet** - `AWS::EC2::Subnet`
 * **PrivateSubnetNetworkAclAssociation** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PrivateSubnetRouteTableAssociation** - `AWS::EC2::SubnetRouteTableAssociation`
 * **PublicNetworkAcl** - `AWS::EC2::NetworkAcl`
 * **PublicRoute** - `AWS::EC2::Route`
 * **PublicRouteTable** - `AWS::EC2::RouteTable`
 * **PublicSubnet** - `AWS::EC2::Subnet`
 * **PublicSubnetNetworkAclAssociation** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PublicSubnetRouteTableAssociation** - `AWS::EC2::SubnetRouteTableAssociation`
 * **SampleApplication** - `AWS::ElasticBeanstalk::Application`
 * **SampleApplicationVersion** - `AWS::ElasticBeanstalk::ApplicationVersion`
 * **SampleEnvironment** - `AWS::ElasticBeanstalk::Environment`
 * **VPC** - `AWS::EC2::VPC`
 * **WebServerInstanceProfile** - `AWS::IAM::InstanceProfile`
 * **WebServerRole** - `AWS::IAM::Role`
 * **WebServerRolePolicy** - `AWS::IAM::Policy`


##Outputs
 * **Bastion** - `{u'Ref': u'BastionIPAddress'}`
 * **URL** - `{u'Fn::Join': [u'', [u'http://', {u'Fn::GetAtt': [u'SampleEnvironment', u'EndpointURL']}]]}`


**Last Updated:** 2015-11-02 15:20:45.949994
