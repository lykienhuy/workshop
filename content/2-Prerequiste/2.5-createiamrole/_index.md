---
title : "Create Role for Lambda"
date : "2025-07-03"
weight : 5
chapter : false
pre : " <b> 2.5 </b> "
---

### Create Role for Lambda

In this step, we will create a Role for Lambda. This Role will be assigned the following policies:

- `AmazonEC2FullAccess`
- `AWSLambda_FullAccess`
- `AWSLambdaBasicExecutionRole`
- `CloudWatchEventsFullAccess`

{{% notice warning %}}
In practice, IAM settings always apply the Least Privilege principle (only granting minimum permissions to perform its specific function). But since this is a lab, we will use IAM FullAccess for simplicity.
{{% /notice %}}

1. Access the **IAM** interface
- Select **Roles**
- Select **Create role**

{{< img src="/images/2.prerequisite/Chuanbi-(18).png" alt="EC2" >}}

2. In the **Trusted entity type** interface
- Select **AWS service**
- Select **Lambda**
- Select **Next**

{{< img src="/images/2.prerequisite/Chuanbi-(19).png" alt="EC2" >}}

3. In the **Add permissions** interface
- Search for **AmazonEC2FullAccess**
- Select **AmazonEC2FullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(21).png" alt="EC2" >}}

- Search for **AWSLambda_FullAccess**
- Select **AWSLambda_FullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(20).png" alt="EC2" >}}

- Search for **AWSLambdaBasicExecutionRole**
- Select **AWSLambdaBasicExecutionRole**

{{< img src="/images/2.prerequisite/Chuanbi-(22).png" alt="EC2" >}}

- Search for **CloudWatchEventsFullAccess**
- Select **CloudWatchEventsFullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(23).png" alt="EC2" >}}

4. In the **Name, review, create** section
- Set **Role name** to `Lambda_Role`
- Set **Description** to `Allows Lambda functions to call AWS services on your behalf`

{{< img src="/images/2.prerequisite/Chuanbi-(24).png" alt="EC2" >}}

5. Select **Create role**

{{< img src="/images/2.prerequisite/Chuanbi-(25).png" alt="EC2" >}}