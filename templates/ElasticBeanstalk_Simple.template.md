##Description
AWS CloudFormation Sample Template ElasticBeanstalk_Simple: Configure and launch an AWS Elastic Beanstalk application that connects to an Amazon RDS database instance. Monitoring is setup on the database. **WARNING** This template creates one or more Amazon EC2 instances and an Amazon Relational Database Service database instance. You will be billed for the AWS resources used if you create a stack from this template.
## Insert

This is an insert into the automatically generated documentation.

**Feel free to use Markdown!**

Use this type of file to insert more details on a template that can't fit into the usual description. Feel free to use images to document the architecture your template deploys.
##Parameters
 * **DBPassword** - Test database admin account password
  * Constraint: `must contain only alphanumeric characters.`
 * **DBUser** - Test database admin account name
  * Constraint: `must begin with a letter and contain only alphanumeric characters.`
 * **OperatorEMail** - EMail address to notify if there are any operational issues
  * Constraint: `must be a valid email address.`

##Conditions
 * **Is-EC2-Classic** - `{u'Fn::Not': [{u'Condition': u'Is-EC2-VPC'}]}`
 * **Is-EC2-VPC** - `{u'Fn::Or': [{u'Fn::Equals': [{u'Ref': u'AWS::Region'}, u'eu-central-1']}, {u'Fn::Equals': [{u'Ref': u'AWS::Region'}, u'cn-north-1']}]}`

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
 * **AlarmTopic** - `AWS::SNS::Topic`
 * **CPUAlarmHigh** - `AWS::CloudWatch::Alarm`
 * **DBEC2SecurityGroup** - `AWS::EC2::SecurityGroup`
 * **DBSecurityGroup** - `AWS::RDS::DBSecurityGroup`
 * **InstanceSecurityGroup** - `AWS::EC2::SecurityGroup`
 * **SampleApplication** - `AWS::ElasticBeanstalk::Application`
 * **SampleApplicationVersion** - `AWS::ElasticBeanstalk::ApplicationVersion`
 * **SampleConfigurationTemplate** - `AWS::ElasticBeanstalk::ConfigurationTemplate`
 * **SampleDB** - `AWS::RDS::DBInstance`
 * **SampleEnvironment** - `AWS::ElasticBeanstalk::Environment`
 * **WebServerInstanceProfile** - `AWS::IAM::InstanceProfile`
 * **WebServerRole** - `AWS::IAM::Role`
 * **WebServerRolePolicy** - `AWS::IAM::Policy`

##Outputs
 * **URL** - `{u'Fn::Join': [u'', [u'http://', {u'Fn::GetAtt': [u'SampleEnvironment', u'EndpointURL']}]]}`

