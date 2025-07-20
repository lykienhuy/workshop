---
title : "Create S3 Bucket"
date : "2025-07-03"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---
### Overview
In this step, we will create an S3 Bucket used to store IPs of malicious EC2 instances (Threat list).
{{% notice info %}}
GuardDuty will filter based on the file we have uploaded.
{{% /notice %}}

![S3](/images/S3.png)
### Content
- [Create S3 Bucket](3.1-creates3/) 
- [Upload Threat list to S3](3.2-uploadthreatlist/)