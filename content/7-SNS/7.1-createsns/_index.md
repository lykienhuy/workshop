---
title : "Create SNS Topic"
date : "2025-07-03"
weight : 1
chapter : false
pre : " <b> 7.1 </b> "
---

#### Create SNS Topic
1. Access the **Amazon SNS** interface
- Select **Topics**
- Select **Create topic**

![SNS](/images/7.sns/SNS-(1).png)

2. In the **Create topic** interface
- Select **Standard** for **Type**
- Set **Name** to `Lambda_SNS`
- Set **Display name** to `SNS Topic`

![SNS](/images/7.sns/SNS-(2).png)

3. Click **Create topic**

![SNS](/images/7.sns/SNS-(3).png)

4. After creation, click **Create subscription**

![SNS](/images/7.sns/SNS-(4).png)

5. Create a **Subscription**
- For **Topic ARN**, select the ARN of **Lambda_SNS**
- For **Protocol**, select **email** (Send via email)
- For **Endpoint**, enter the email address to receive notifications (Can be your own email)

![SNS](/images/7.sns/SNS-(5).png)

6. Select **Create subscription**

![SNS](/images/7.sns/SNS-(6).png)

7. Check your **Email** to **confirm subscription**
![SNS](/images/7.sns/SNS-(7).png)
![SNS](/images/7.sns/SNS-(8).png)