---
title : "Clean up resources"
date : "2025-07-03"
weight : 9
chapter : false
pre : "<b>9. </b>"
---

We will take the following steps to delete the resources we created in this exercise.

#### Delete EC2 Instance
- Access the **EC2 Management Console**
- In the left navigation bar, select **Instances**
- Select all **EC2 Instances** related to this lab
- Select **Actions**
- Select **Terminate**

![Clean](/images/9.clean/Clear-(1).png)

#### Delete Security Group
- Open the **Amazon VPC Console**
- Select **Security Groups** from the left navigation bar
- Select the **Security Group** related to this lab
- Click on **Actions**, select **Delete security group**
- Click on **Delete** to confirm

![Clean](/images/9.clean/Clear-(2).png)

#### Delete VPC
- Access the VPC Management Console
- In the left navigation bar, select **Your VPCs**
- Select the **VPC** related to this lab
- Select **Action**
- Select **Delete VPC**
- Type **delete** in the empty field
- Select **Delete**

![Clean](/images/9.clean/Clear-(3).png)

#### Delete S3 Bucket
1. Empty S3 Bucket
- Access **AWS S3**
- In the Bucket name list, select the bucket related to this lab
- Select **Empty**
- In the **Empty bucket** page, confirm and select **Empty**

2. Delete S3 Bucket
- Access **AWS S3**
- Select the **S3 bucket** related to this lab
- Select **Delete**
- Enter the **S3** name and select **Delete bucket**

![Clean](/images/9.clean/Clear-(6).png)

![Clean](/images/9.clean/Clear-(7).png)

#### Delete Threat list IP in GuardDuty
- Access **GuardDuty**
- Select **Settings/Lists**
- Select the **Threat list** created in this lab
- Select **Actions/Delete**
![Clean](/images/9.clean/Clear-(8).png)

#### Delete EventBridge Rule
- Access **EventBridge**
- Select **Rule**
- Select the **Rule** created in this lab
- Select **Actions**
- Enter **delete**

![Clean](/images/9.clean/Clear-(9).png)

#### Delete Lambda function
- Access **AWS Lambda**
- Select the **Functions** related to this lab
- Select **Delete**
- Enter **confirm**

![Clean](/images/9.clean/Clear-(10).png)

#### Delete SNS Topic
- Access **Amazon SNS**
- Select **Topics**
- Select the **Topics** created in this lab
- Select **Delete**
- Enter **delete me**

![Clean](/images/9.clean/Clear-(11).png)