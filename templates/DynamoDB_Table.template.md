##Description
AWS CloudFormation Sample Template DynamoDB_Table: This template demonstrates the creation of a DynamoDB table.  **WARNING** This template creates an Amazon DynamoDB table. You will be billed for the AWS resources used if you create a stack from this template.
##Parameters
 * **HaskKeyElementName** - HashType PrimaryKey Name
  * Constraint: `must contain only alphanumberic characters`
 * **HaskKeyElementType** - HashType PrimaryKey Type
  * Default: `S`
  * Constraint: `must be either S or N`
 * **ReadCapacityUnits** - Provisioned read throughput
  * Default: `5`
  * Constraint: `must be between 5 and 10000`
 * **WriteCapacityUnits** - Provisioned write throughput
  * Default: `10`
  * Constraint: `must be between 5 and 10000`

##Resources
 * **myDynamoDBTable** - `AWS::DynamoDB::Table`

##Outputs
 * **TableName** - `{u'Ref': u'myDynamoDBTable'}`

