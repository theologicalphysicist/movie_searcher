#_ PYTHON LIBRARIES
import json, os, sys

#_ EXTERNAL
import boto3

from logger import getLogger, printJSON


LAMBDA_LOGGER = getLogger("LAMBDA")


def handler(event, context):

    LAMBDA_LOGGER.debug("INSIDE LAMBDA")
    LAMBDA_LOGGER.debug(event)

    try: 
        AWS_SESSION: boto3.Session = boto3.Session() #* load boto3 session
        S3_CLIENT = AWS_SESSION.client("s3") #* load S3 client
        BUCKETS: list[dict] = S3_CLIENT.list_buckets()["Buckets"] #* get all buckets
        aleph_objects: list = []
        ratings_csv: str = ""
        
        for bucket in BUCKETS:
            if bucket["Name"] == os.environ["S3_BUCKET"]:
                aleph_objects = S3_CLIENT.list_objects_v2(Bucket=bucket["Name"])["Contents"]
        
                ratings_csv_res = S3_CLIENT.get_object(
                    Bucket=bucket["Name"],
                    Key="IMDb ratings.csv"
                )
                ratings_csv = str(ratings_csv_res["Body"].read())

        return {
            "statusCode": 200,
            "body": {
            }
        }
    except Exception as e:
        LAMBDA_LOGGER.error(e)

        return {
            "statusCode": 500,
            "body": f"INTERNAL LAMBDA ERROR: {e}"
        }



    # EVENT_FILE_OBJ = open("./events/event1.json", "r")
    # EVENT_DATA = json.load(EVENT_FILE_OBJ)
    # EVENT_FILE_OBJ.close()


    # LAMBDA_LOGGER.debug(event["first_name"])
    # LAMBDA_LOGGER.debug(event["last_name"])
    # LAMBDA_LOGGER.debug(context)


# LAMBDA_LOGGER.info(handler("test", "here"))