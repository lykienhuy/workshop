---
title : "Tạo Security Group"
date :  "2025-07-03" 
weight :  2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Tạo Security Group

1. Truy cập **VPC**
- Chọn **Security Group**
- Chọn **Create Security Group**

{{< img src="/images/2.prerequisite/Chuanbi-(8).png" alt="SG" >}}

2. Tiến hành cấu hình
- **Security Group name**, nhập `Security-Group`
- **Description**, nhập `Normal Security Group` (Đây sẽ là SG để các EC2 hoạt động bình thường)
- **VPC** sẽ chọn VPC đã tạo
- Bấm vào **Add rule**

{{< img src="/images/2.prerequisite/Chuanbi-(9).png" alt="SG" >}}
3. Cấu hình **Inbound Rules**
- **SSH** cổng 22 dùng để kết nối với máy local và source chọn My IP

- **HTTP** cổng 80 và source là Anywhere IPv4

- **HTTPS** cổng 443 và source là Anywhere IPv4

{{< img src="/images/2.prerequisite/Chuanbi-(10).png" alt="SG" >}}
4. Chọn **Create Security Group**

{{< img src="/images/2.prerequisite/Chuanbi-(11).png" alt="SG" >}}