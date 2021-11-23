# AWS MemoryDB CloudFormation template

CloudFormation template that allows you to embed and deploy a MemoryDB cluster as nested stack in your other CloudFormation templates.

## What is AWS MemoryDB?

MemoryDB is an in-memory, Redis compatible, multi-AZ database. MemoryDB leverages a distributed transaction log to durably store data across multiple AZs, meaning if a node or the entire cluster goes down, there's no data loss.

## Usage examples

Take a look at the [how-to-use.yaml](example/how-to-use.yaml) if you want to see an example stack using this template.

### memorydb.yaml

Template URL: `https://aws-memorydb-cf-template.s3.eu-central-1.amazonaws.com/memorydb.yaml`

```
MemoryDBCluster:
    Type: AWS::CloudFormation::Stack
    Properties:
        TemplateURL: !Ref MemoryDbTemplateUrl
        TimeoutInMinutes: 20
        Parameters:
        Name: !Join ["-", ["test", "example", "db"]]
        NodeType: db.t4g.small
        SubnetIds: subnet-0cc31430175210b69,subnet-0f4c2b2d24dc5ff59,subnet-0f432d0eb9e49811f
```

[![](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=memorydb-stack&templateURL=https://aws-memorydb-cf-template.s3.eu-central-1.amazonaws.com/memorydb.yaml)

## Resources

| Name                                                                                                                                | Type     |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [AWS::MemoryDB::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html)         | resource |
| [AWS::MemoryDB::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html) | resource |
| [AWS::MemoryDB::ACL](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html)                 | resource |
| [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html)                     | resource |

## Parameters

| Name                 | Description                                    | Type           | Default      | Required |
| -------------------- | ---------------------------------------------- | -------------- | ------------ | :------: |
| Name                 | Name of the MemoryDB cluster.                  | `string`       | n/a          |   yes    |
| NodeType             | The cluster's on-demand node type.             | `string`       | db.t4g.small |    no    |
| Port                 | The port used by the cluster.                  | `number`       | 6379         |    no    |
| SubnetIds            | Subnets associated with cluster.               | `list(string)` | n/a          |    no    |
| SecurityGroupIds     | Security group names associated with cluster.  | `list(string)` | n/a          |    no    |
| ShardCount           | The number of shards in the cluster.           | `number`       | 1            |    no    |
| ReplicaPerShardCount | The number of replicas to apply to each shard. | `number`       | 0            |    no    |

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## Deployment

The [/template](template) directory is automatically synced with the S3 bucket when a commit to `main` is done.
