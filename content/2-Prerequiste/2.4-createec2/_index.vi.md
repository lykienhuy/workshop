---
title : "Tạo EC2 Instance"
date :  "2025-07-03" 
weight : 4
chapter : false
pre : " <b> 2.4 </b> "
---

#### Tạo EC2 Instance

1. Truy cập **EC2**
- Chọn **Instances** 
- Chọn **Launch Instances**

{{< img src="/images/2.prerequisite/Chuanbi-(14).png" alt="EC2" >}}

2. Cấu hình **EC2**
- **Name** là `EC2`
- **Number of instances** là **2**
- **AMI** chọn **Amazon Linux**
- **Instance type** chọn là **t2.micro**

{{< img src="/images/2.prerequisite/Chuanbi-(15).png" alt="EC2" >}}

3. Cấu hình **Network**
- **VPC** chọn VPC đã tạo
- **Subnet** Chọn **public-subnet**
- Chọn **Select existing security group**
- Chọn **Security-Group**
- Bấm **Launch instance**

{{< img src="/images/2.prerequisite/Chuanbi-(16).png" alt="EC2" >}}

4. Sau khi tạo xong 2 EC2 Instance thì ta tiến hành đổi tên thành:
- `Compromised_EC2` (EC2 đang bị nghi nhiễm)
- `Malicious_EC2` (EC2 bị nhiễm và có trong Threat List)

{{< img src="/images/2.prerequisite/Chuanbi-(17).png" alt="EC2" >}}