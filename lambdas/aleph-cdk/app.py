#!/usr/bin/env python3
#_ PYTHON INTERNAL & EXTERNAL LIBRARIES
import builtins
import os, dotenv
import typing

#_ AWS LIBRARIES
import aws_cdk
from aws_cdk import (
    Duration,
    Environment,
    IStackSynthesizer,
    PermissionsBoundary,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_ecr as ecr,
    aws_lambda,
    aws_iam as iam,
    CfnOutput
    # aws_sqs as sqs,
)

from constructs import Construct


dotenv.load_dotenv(dotenv_path="./.env.production", verbose=True)


class AlephCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #_ BUCKET
        ALEPH_BUCKET = s3.Bucket(scope=self, id="aleph-bucket", versioned=True)
        s3deploy.BucketDeployment(
            scope=self, 
            id="aleph-objects", 
            sources=[s3deploy.Source.asset("../assets")],
            destination_bucket=ALEPH_BUCKET,
            memory_limit=512
        )

        #_ LAMBDA
        ALEPH_LAMBDA = aws_lambda.Function(
            scope=self,
            id="aleph-lambda",
            code=aws_lambda.Code.from_asset("code-stack/code.zip"),
            architecture=aws_lambda.Architecture.X86_64,
            handler="main.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_10,
            function_name="aleph_handler",
            role=iam.Role.from_role_arn(
                scope=self,
                id="aleph-lambda-role",
                role_arn=os.environ["ROLE_ARN"]
            ),
            environment={
                "S3_BUCKET": os.environ["S3_BUCKET"]
            },
            memory_size=512,
            timeout=Duration.seconds(10)
        )
        ALEPH_LAMBDA_URL = ALEPH_LAMBDA.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE
        )
        CfnOutput(self, "aleph-lambda-url", value=ALEPH_LAMBDA_URL.url) #* print out function url


class AlephContainerStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ECR_IMAGE = aws_lambda.EcrImageCode.from_asset_image(
            directory="container-stack"
        )

        ALEPH_CONTAINER_LAMBDA = aws_lambda.Function(
            scope=self,
            id="aleph-container-lambda",
            code=ECR_IMAGE,
            handler=aws_lambda.Handler.FROM_IMAGE,
            runtime=aws_lambda.Runtime.FROM_IMAGE,
            environment={
                "S3_BUCKET": os.environ["S3_BUCKET"]
            },
            role=iam.Role.from_role_arn(
                scope=self,
                id="aleph-lambda-role",
                role_arn=os.environ["ROLE_ARN"]
            ),

            memory_size=512,
            timeout=Duration.seconds(10)
        )
        ALEPH_CONTAINER_LAMBDA_URL = ALEPH_CONTAINER_LAMBDA.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE
        )
        CfnOutput(self, "aleph-lambda-url", value=ALEPH_CONTAINER_LAMBDA_URL.url) #* print out function url


app = aws_cdk.App()
AlephCdkStack(
    app, 
    "AlephCdkStack",
    env=aws_cdk.Environment(account=os.environ["AWS_ACCOUNT_ID"], region=os.environ["AWS_REGION_NAME"]),
)
AlephContainerStack(
    app,
    "AlephContainerStack",
    env=aws_cdk.Environment(account=os.environ["AWS_ACCOUNT_ID"], region=os.environ["AWS_REGION_NAME"]),
)
app.synth()
