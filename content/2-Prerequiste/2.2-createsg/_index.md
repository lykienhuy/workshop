---
title : "Create Security Group"
date : "2025-07-03"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Create Security Group

1. Access **VPC**
- Select **Security Group**
- Select **Create Security Group**

![SG](/images/2.prerequisite/Chuanbi-(8).png)

2. Proceed with configuration
- For **Security Group name**, enter `Security-Group`
- For **Description**, enter `Normal Security Group` (This will be the SG for EC2 instances to operate normally)
- For **VPC** select the VPC you created
- Click on **Add rule**

![SG](/images/2.prerequisite/Chuanbi-(9).png)
3. Configure **Inbound Rules**
- **SSH** port 22 used to connect with local machine and select My IP for source

- **HTTP** port 80 and source is Anywhere IPv4

- **HTTPS** port 443 and source is Anywhere IPv4

![SG](/images/2.prerequisite/Chuanbi-(10).png)
4. Select **Create Security Group**

![SG](/images/2.prerequisite/Chuanbi-(11).png)