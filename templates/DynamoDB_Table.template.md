##Description
AWS CloudFormation Sample Template DynamoDB_Table: This template demonstrates the creation of a DynamoDB table.  **WARNING** This template creates an Amazon DynamoDB table. You will be billed for the AWS resources used if you create a stack from this template.
## Insert

This is an insert into the automatically generated documentation.

**Feel free to use Markdown!**

Use this type of file to insert more details on a template that can't fit into the usual description. Feel free to use images to document the architecture your template deploys.
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

