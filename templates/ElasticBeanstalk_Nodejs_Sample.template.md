##Description
AWS CloudFormation Sample Template ElasticBeanstalk_Nodejs_Sample: Configure and launch the AWS Elastic Beanstalk sample application. **WARNING** This template creates one or more Amazon EC2 instances. You will be billed for the AWS resources used if you create a stack from this template.
##Parameters
 * **KeyName** - Name of an existing EC2 KeyPair to enable SSH access to the AWS Elastic Beanstalk instance
  * Constraint: `must be the name of an existing EC2 KeyPair.`


##Mappings
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


##Resources
 * **SampleApplication** - `AWS::ElasticBeanstalk::Application`
 * **SampleApplicationVersion** - `AWS::ElasticBeanstalk::ApplicationVersion`
 * **SampleConfigurationTemplate** - `AWS::ElasticBeanstalk::ConfigurationTemplate`
 * **SampleEnvironment** - `AWS::ElasticBeanstalk::Environment`
 * **WebServerInstanceProfile** - `AWS::IAM::InstanceProfile`
 * **WebServerRole** - `AWS::IAM::Role`
 * **WebServerRolePolicy** - `AWS::IAM::Policy`


##Outputs
 * **URL** - `{u'Fn::Join': [u'', [u'http://', {u'Fn::GetAtt': [u'SampleEnvironment', u'EndpointURL']}]]}`


**Last Updated:** 2015-11-02 15:20:45.774255
