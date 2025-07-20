---
title : "Upload Threat list to S3"
date : "2025-07-03"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

#### Upload Threat list to S3
We will assume that **Malicious_EC2** is a malicious EC2 instance, and no connections should be allowed to this EC2. Because if connected, there is a high risk of infection.

1. We will add the IP address of this EC2 to the Threat list by:
- Selecting **Malicious_EC2**
- Copying the **Public IPv4 address** of this EC2

{{< img src="/images/3.S3/S3-(6" alt="S3" >}}.png)

2. Create a **txt file**
- Name it `ThreatList.txt`
- Paste the IP of the malicious EC2 into that **txt file**

{{< img src="/images/3.S3/S3-(7" alt="S3" >}}.png)

3. Upload that **txt file** to **S3**

{{< img src="/images/3.S3/S3-(8" alt="S3" >}}.png)

{{< img src="/images/3.S3/S3-(9" alt="S3" >}}.png)

4. After successful upload, copy the **Object URL**

{{< img src="/images/3.S3/S3-(10" alt="S3" >}}.png)