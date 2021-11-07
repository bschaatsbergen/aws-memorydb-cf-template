# AWS MemoryDB CloudFormation templates

A library of CloudFormation templates that allows you to embed and deploy a MemoryDB cluster as nested stacks in your CloudFormation template.

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

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## Deployment

The `/templates` directory is automatically synced with the S3 bucket defined under `s3.tf` when a commit to `main` is done.
