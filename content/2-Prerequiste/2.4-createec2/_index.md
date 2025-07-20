---
title : "Create EC2 Instance"
date : "2025-07-03"
weight : 4
chapter : false
pre : " <b> 2.4 </b> "
---

#### Create EC2 Instance

1. Access **EC2**
- Select **Instances** 
- Select **Launch Instances**

![EC2](/images/2.prerequisite/Chuanbi-(14).png)

2. Configure **EC2**
- Set **Name** to `EC2`
- Set **Number of instances** to **2**
- Select **Amazon Linux** for **AMI**
- Select **t2.micro** for **Instance type**

![EC2](/images/2.prerequisite/Chuanbi-(15).png)

3. Configure **Network**
- Select the created VPC for **VPC**
- Select **public-subnet** for **Subnet**
- Select **Select existing security group**
- Select **Security-Group**
- Click **Launch instance**

![EC2](/images/2.prerequisite/Chuanbi-(16).png)

4. After creating 2 EC2 Instances, rename them to:
- `Compromised_EC2` (EC2 suspected of being infected)
- `Malicious_EC2` (EC2 that is infected and included in the Threat List)

![EC2](/images/2.prerequisite/Chuanbi-(17).png)