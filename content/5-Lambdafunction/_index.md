---
title : "Lambda function"
date :  "2025-07-03" 
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---
#### Create Lambda function
1. Select **Create a function**

{{< img src="/images/5.lambdafunction/Lambda-(1).png" alt="Lambda" >}}

2. In the **Create function** interface
- Select **Author from scratch**
- Set **Function name** to `Auto_Isolate_Lambda`
- Select **Python 3.13** for **Runtime**

{{< img src="/images/5.lambdafunction/Lambda-(2).png" alt="Lambda" >}}

3. Select **Create function**

{{< img src="/images/5.lambdafunction/Lambda-(3).png" alt="Lambda" >}}

4. After creating the environment
- Select **Code**

{{< img src="/images/5.lambdafunction/Lambda-(4).png" alt="Lambda" >}}

5. In the **Code Source** interface
- Add this code (Remember to replace with your **Isolated-Security Group ID**)
- After adding the code, proceed to **Deploy**

```
import boto3
import json
from botocore.exceptions import ClientError

# Initialize the EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        # Log the incoming event to see its structure
        print(f"Received event: {json.dumps(event)}")
        
        # Extract instance ID from the event details
        if 'detail' in event and 'resource' in event['detail'] and 'instanceDetails' in event['detail']['resource']:
            instance_id = event['detail']['resource']['instanceDetails']['instanceId']
        else:
            # Return an error if the event structure is unexpected
            return {
                'statusCode': 400,
                'body': json.dumps("Error: Event structure is not as expected.")
            }
        
        # Isolate the instance by modifying its security group
        response_sg = ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=['sg-01234abcd5678efgh']  # Replace with your IsolatedSecurityGroup ID
        )
        print(f"Instance {instance_id} isolated: {response_sg}")
        
        # Stop the compromised instance
        response_stop = ec2.stop_instances(
            InstanceIds=[instance_id]
        )
        print(f"Instance {instance_id} stopped: {response_stop}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Instance {instance_id} successfully isolated and stopped.")
        }
    
    except ClientError as e:
        print(f"Error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
```

{{< img src="/images/5.lambdafunction/Lambda-(5).png" alt="Lambda" >}}

6. Proceed to grant permissions for **Lambda**
- Select **Configuration**
- Select **Edit**

{{< img src="/images/5.lambdafunction/Lambda-(6).png" alt="Lambda" >}}

7. In the **Existing role** section
- Select **Lambda_Role**
- Select **Save**

{{< img src="/images/5.lambdafunction/Lambda-(7).png" alt="Lambda" >}}

8. Proceed to test Lambda
- Select **Test**
- Enter **test** for Event Name
- Click **Save**

{{< img src="/images/5.lambdafunction/Lambda-(8).png" alt="Lambda" >}}

9. If the result appears as shown below, it's successful

{{< img src="/images/5.lambdafunction/Lambda-(9).png" alt="Lambda" >}}