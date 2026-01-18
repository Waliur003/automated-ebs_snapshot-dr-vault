import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # 1. Find all volumes with the tag Backup=True
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'tag:Backup', 'Values': ['True']}]
    )['Volumes']
    
    for vol in volumes:
        vol_id = vol['VolumeId']
        description = f"Automated backup for {vol_id} on {datetime.datetime.now()}"
        
        # 2. Create the snapshot
        snapshot = ec2.create_snapshot(VolumeId=vol_id, Description=description)
        print(f"Created snapshot: {snapshot['SnapshotId']} for volume: {vol_id}")
        
    return {"status": "success"}