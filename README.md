# AWS MemoryDB CloudFormation template

A library of CloudFormation template that allows you to embed and deploy a MemoryDB cluster as nested stacks in your CloudFormation template.

## What is AWS MemoryDB?

MemoryDB is an in-memory, Redis compatible, multi-AZ database. MemoryDB leverages a distributed transaction log to durably store data across multiple AZs, meaning if a node or the entire cluster goes down, there's no data loss.

## Usage examples

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
        NodeType: db.r6g.large
        SubnetIds: subnet-09d2d15449da1bd1d, subnet-03f0d954893yy57b1, subnet-0a65961be8520157b
```

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
| NodeType             | The cluster's on-demand node type.             | `string`       | db.r6g.large |    no    |
| Port                 | The port used by the cluster.                  | `number`       | 6379         |    no    |
| SubnetIds            | Subnets associated with cluster.               | `list(string)` | n/a          |    no    |
| SecurityGroupIds     | Security group names associated with cluster.  | `list(string)` | n/a          |    no    |
| ShardCount           | The number of shards in the cluster.           | `number`       | 1            |    no    |
| ReplicaPerShardCount | The number of replicas to apply to each shard. | `number`       | 0            |    no    |

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## Deployment

The `/template` directory is automatically synced with the S3 bucket defined under `s3.tf` when a commit to `main` is done.
