import boto3
import time

def create_db_subnet_group(rds_client, subnet_ids):
    try:
        response = rds_client.create_db_subnet_group(
            DBSubnetGroupName='my-db-subnet-group1',
            DBSubnetGroupDescription='My DB Subnet Group',
            SubnetIds=subnet_ids,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MyDBSubnetGroup'
                },
            ]
        )
        return response
    except Exception as e:
        raise Exception(f"Error creating DB subnet group: {str(e)}")

def create_rds_instance(rds_client):
    try:
        response = rds_client.create_db_instance(
            DBInstanceIdentifier='my-rds-instance',
            AllocatedStorage=20,  # in GB
            DBInstanceClass='db.t3.micro',
            Engine='mysql',
            MasterUsername='admin',
            MasterUserPassword='yourpassword',
            DBName='mydatabase',
            VpcSecurityGroupIds=[
                'your-sg',  
            ],
            DBSubnetGroupName='my-db-subnet-group',
            MultiAZ=False,
            PubliclyAccessible=False,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MyRDSInstance'
                },
            ]
        )
        return response
    except Exception as e:
        raise Exception(f"Error creating RDS instance: {str(e)}")

def wait_for_rds_instance(rds_client, db_instance_identifier):
    while True:
        response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
        db_instances = response['DBInstances']
        if len(db_instances) > 0:
            db_instance = db_instances[0]
            status = db_instance['DBInstanceStatus']
            print(f"Current status: {status}")
            if status == 'available':
                endpoint = db_instance['Endpoint']['Address']
                print(f"RDS instance is available! Endpoint DNS: {endpoint}")
                return endpoint
        else:
            print("No DB instance found.")
        time.sleep(30)  # Wait for 30 seconds before checking again

def main():
    rds_client = boto3.client('rds')
    
    subnet_ids = [
        'Add your Private Subnets',  # Replace with your private subnet ID
        'Add your Private Subnets'   # Replace with your private subnet ID
    ]
    
    try:
        # Create DB Subnet Group
        create_db_subnet_group(rds_client, subnet_ids)
        
        # Create RDS Instance
        create_rds_instance(rds_client)
        
        # Wait for RDS instance to become available
        endpoint = wait_for_rds_instance(rds_client, 'my-rds-instance')
        
        print(f'RDS instance created successfully! Endpoint DNS: {endpoint}')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()
