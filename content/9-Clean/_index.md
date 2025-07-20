---
title : "Clean up resources"
date : "2025-07-03"
weight : 9
chapter : false
pre : "<b>9. </b>"
---

We will proceed with the following steps to delete the resources we created in this lab
#### Delete EC2 Instance
- Access the EC2 Management Console
- On the left navigation bar, select Instances
- Select all EC2 Instances related to the lab
- Choose Actions
- Select Terminate

{{< img src="/images/9.clean/Clear-(1).png" alt="Clean" >}}

#### Delete Security Group
- Open the Amazon VPC Console
- Select Security Groups from the left navigation bar
- Select the Security Group related to the lab
- Click on Actions, select Delete security group
- Click Delete to confirm

{{< img src="/images/9.clean/Clear-(2).png" alt="Clean" >}}

#### Delete S3 Bucket
1. Empty S3 Bucket
- Access AWS S3
- In the Bucket name list, select the bucket related to the lab
- Select Empty
- On the Empty bucket page, confirm and select Empty
2. Delete S3 Bucket
- Access AWS S3
- Select the S3 bucket related to the lab
- Select Delete
- Enter the S3 name and select Delete bucket

{{< img src="/images/9.clean/Clear-(6).png" alt="Clean" >}}

{{< img src="/images/9.clean/Clear-(7).png" alt="Clean" >}}

#### Delete Threat list IP in GuardDuty
- Access GuardDuty
- Select Settings/Lists
- Select the Threat list created in this lab
- Select Actions/Delete

{{< img src="/images/9.clean/Clear-(8).png" alt="Clean" >}}

#### Delete EventBridge Rule
- Access EventBridge
- Select Rule
- Select the Rule created in this lab
- Select Actions
- Enter delete

{{< img src="/images/9.clean/Clear-(9).png" alt="Clean" >}}

#### Delete Lambda function
- Access AWS Lambda
- Select the Functions related to the lab
- Select Delete
- Enter confirm

{{< img src="/images/9.clean/Clear-(10).png" alt="Clean" >}}

#### Delete SNS Topic
- Access Amazon SNS
- Select Topics
- Select the Topics created in the lab
- Select Delete
- Enter delete me

{{< img src="/images/9.clean/Clear-(11).png" alt="Clean" >}}