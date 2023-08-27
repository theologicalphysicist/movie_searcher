#_ PYTHON LIBRARIES
import json, os, sys

#_ EXTERNAL
import boto3
import dotenv

#_ LOCAL
from logger import printJSON, getLogger


LAMBDA_LOGGER = getLogger("Lambda")


def handler(event, context):

    # LAMBDA_LOGGER.debug(os.environ.get("S3_BUCKET"))

    LAMBDA_LOGGER.debug(os.environ.get("S3_BUCKET"))

    return {
        "statusCode": 200,
        "body": {
            "s3Bucket": os.environ["S3_BUCKET"],
            "no": "aether"
        }
    }

    # try: 
    #     AWS_SESSION = boto3.Session(
    #         aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    #         aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    #         region_name=os.environ["AWS_REGION_NAME"]
    #     )

    #     S3_CLIENT = AWS_SESSION.client("s3")

    #     BUCKETS = S3_CLIENT.list_buckets()
    #     BUCKET_OBJETCS_RESPONSE = S3_CLIENT.list_objects_v2(Bucket=BUCKETS["Buckets"][0]["Name"])
    #     BUCKET_OBJETCS: list = BUCKET_OBJETCS_RESPONSE["Contents"]

    #     LAMBDA_LOGGER.debug(printJSON(BUCKETS))

    #     return printJSON({
    #         "statusCode": 200,
    #         "body": BUCKET_OBJETCS
    #     })
    # except Exception as e:
    #     LAMBDA_LOGGER.error(e)

    #     return printJSON({
    #         "statusCode": 500,
    #         "body": f"INTERNAL LAMBDA ERROR: {e}"
    #     })



    # EVENT_FILE_OBJ = open("./events/event1.json", "r")
    # EVENT_DATA = json.load(EVENT_FILE_OBJ)
    # EVENT_FILE_OBJ.close()


    # LAMBDA_LOGGER.debug(event["first_name"])
    # LAMBDA_LOGGER.debug(event["last_name"])
    # LAMBDA_LOGGER.debug(context)


# LAMBDA_LOGGER.info(handler("test", "here"))