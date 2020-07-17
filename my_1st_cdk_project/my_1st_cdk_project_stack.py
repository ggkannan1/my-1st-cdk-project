from aws_cdk import (
    aws_s3 as _s3,
    core
)

class My1StCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "mybucketid",
            bucket_name="my1stcdkbucket2020",
            versioned=False,
            encryption=_s3.BucketEncryption.KMS_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )