import boto3
import sys 

try:
    session = boto3.Session()
    credentials = session.get_credentials()
    region = session.region_name

    
    if not credentials:
        print("ERROR: No credentials found. Check ~/.aws/credentials")
        sys.exit(1)

    print(f"Credentials Found. Region: {region}")

  
    print("Contacting AWS Identity Service...")
    iam = boto3.client('iam')
    user = iam.get_user()
    
    username = user['User']['UserName']
    user_id = user['User']['UserId']
    
    print(f"\n[SUCCESS] Authentication Confirmed.")
    print(f"User: {username}")
    print(f"ID:   {user_id}")

except Exception as e:
    print("\n[FAILURE] Could not connect to AWS.")
    print(f"Error Message: {e}")