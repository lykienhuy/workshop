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

{{< img src="/images/7.sns/SNS-(1).png" alt="SNS" >}}

2. In the **Create topic** interface
- Select **Standard** for **Type**
- Set **Name** to `Lambda_SNS`
- Set **Display name** to `SNS Topic`

{{< img src="/images/7.sns/SNS-(2).png" alt="SNS" >}}

3. Click **Create topic**

{{< img src="/images/7.sns/SNS-(3).png" alt="SNS" >}}

4. After creation, click **Create subscription**

{{< img src="/images/7.sns/SNS-(4).png" alt="SNS" >}}

5. Create a **Subscription**
- For **Topic ARN**, select the ARN of **Lambda_SNS**
- For **Protocol**, select **email** (Send via email)
- For **Endpoint**, enter the email address to receive notifications (Can be your own email)

{{< img src="/images/7.sns/SNS-(5).png" alt="SNS" >}}

6. Select **Create subscription**

{{< img src="/images/7.sns/SNS-(6).png" alt="SNS" >}}

7. Check your **Email** to **confirm subscription**
{{< img src="/images/7.sns/SNS-(7).png" alt="SNS" >}}
{{< img src="/images/7.sns/SNS-(8).png" alt="SNS" >}}