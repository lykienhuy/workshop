---
title : "Create Isolate Security Group"
date : "2025-07-03"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Create Security Group

1. Proceed with configuration
- For **Security Group name**, enter `Isolated Security-Group`
- For **Description**, enter `Isolated Security Group` (This will be the SG used to isolate suspected infected EC2 instances)
- For **VPC** select the VPC you created

{{< img src="/images/2.prerequisite/Chuanbi-(12" alt="SG" >}}.png)
2. Configure **Inbound Rules**
- **SSH** port 22 used to connect with local machine and select My IP for source (Used to investigate suspected infected EC2 instances)
- Select **Create Security Group**

{{< img src="/images/2.prerequisite/Chuanbi-(13" alt="SG" >}}.png)