---
title : "Tạo Isolate Security Group"
date :  "2025-07-03" 
weight :  3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Tạo Security Group

1. Tiến hành cấu hình
- **Security Group name**, nhập `Isolated Security-Group`
- **Description**, nhập `Isolated Security Group` (Đây sẽ là SG dùng để cách ly các EC2 bị nghi nhiễm)
- **VPC** sẽ chọn VPC đã tạo

![SG](/images/2.prerequisite/Chuanbi-(12).png)
2. Cấu hình **Inbound Rules**
- **SSH** cổng 22 dùng để kết nối với máy local và source chọn My IP (Dùng để điều tra các EC2 bị nghi nhiễm)
- Chọn **Create Security Group**

![SG](/images/2.prerequisite/Chuanbi-(13).png)