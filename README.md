# AWS RDS Instance Creation Script

This Python script automates the process of creating an RDS instance in AWS using Boto3. It includes the creation of a DB subnet group, an RDS instance, and a function to wait until the RDS instance becomes available.

## Prerequisites

- Python 3.x
- Boto3 library
- AWS credentials configured (using `aws configure` or environment variables)

## Setup

1. **Install Boto3**:
    ```bash
    pip install boto3
    ```

2. **Configure AWS Credentials**:
    Ensure your AWS credentials are configured properly. You can use the AWS CLI to configure them:
    ```bash
    aws configure
    ```

## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abid000007/aws-rds-creation-script.git
    cd aws-rds-creation-script
    ```

2. **Update the Script**:
    - Replace `'Add your Private Subnets'` with your actual private subnet IDs.
    - Replace `'your-sg'` with your actual security group ID.
    - Replace `'yourpassword'` with a strong password for the master user.

3. **Run the Script**:
    ```bash
    python create_rds_instance.py
    ```

## Script Details

- **create_db_subnet_group(rds_client, subnet_ids)**: This function creates a DB subnet group using the provided subnet IDs.
- **create_rds_instance(rds_client)**: This function creates an RDS instance with the specified parameters.
- **wait_for_rds_instance(rds_client, db_instance_identifier)**: This function waits until the RDS instance becomes available and prints its endpoint.

## Example

Here’s an example of how to update the script with your details:

```python
subnet_ids = [
    'subnet-0028654e9f13187db',
    'subnet-0d328f0a295778ef3'
]

response = create_db_subnet_group(rds_client, subnet_ids)
print(response)

response = create_rds_instance(rds_client)
print(response)

endpoint = wait_for_rds_instance(rds_client, 'my-rds-instance')
print(f'RDS instance created successfully! Endpoint DNS: {endpoint}')
