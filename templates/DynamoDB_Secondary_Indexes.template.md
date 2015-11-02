##Description
AWS CloudFormation Sample Template DynamoDB_Secondary_Indexes: Create a DynamoDB table with local and global secondary indexes. **WARNING** This template creates an Amazon DynamoDB table. You will be billed for the AWS resources used if you create a stack from this template.
##Parameters
 * **ReadCapacityUnits** - Provisioned read throughput
  * Default: `5`
  * Constraint: `must be between 5 and 10000`
 * **WriteCapacityUnits** - Provisioned write throughput
  * Default: `10`
  * Constraint: `must be between 5 and 10000`


##Resources
 * **TableOfBooks** - `AWS::DynamoDB::Table`


##Outputs
 * **TableName** - `{u'Ref': u'TableOfBooks'}`


**Last Updated:** 2015-11-02 15:20:44.629123
