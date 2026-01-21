import boto3
import os

BUCKET_NAME = "api-monitor-logs-rayyan-001"
REGION = "ap-south-1"
FILE_NAME = "user_report.txt"
def upload_to_aws():
    # 1. Initialize the S3 Robot
    s3 = boto3.client('s3', region_name=REGION)

    print(f"--- STARTING CLOUD SYNC ---")

    # 2. Check if the file actually exists locally
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} not found. Run your spy-bot first!")
        return

    # 3. Create the Bucket 
    try:
        print(f"Creating Bucket: {BUCKET_NAME}...")
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print("Bucket created successfully.")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print("Bucket already exists (and belongs to you). Proceeding...")
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return

    # 4. Upload the File
    try:
        print(f"Uploading {FILE_NAME}...")
        # upload_file
        s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
        print(f"SUCCESS! File uploaded to S3.")
        print(f"View it here: https://s3.console.aws.amazon.com/s3/buckets/{BUCKET_NAME}")
    except Exception as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    upload_to_aws()