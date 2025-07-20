---
title : "Upload Threat list lên S3"
date :  "2025-07-03" 
weight : 2 
chapter : false
pre : " <b> 3.2. </b> "
---

#### Tải Threat list lên S3
Ta sẽ giả sử **Malicious_EC2** là một EC2 độc hại, không được cho bất cứ kết nối nào đến với EC2 này. Vì nếu kết nối sẽ có nguy cơ bị lây nhiễm rất cao.

1. Ta sẽ đưa đại chỉ IP của EC2 này vào Threat list bằng cách:
- Chọn **Malicious_EC2**
- Copy **Public IPv4 address** của EC2 này

{{< img src="/images/3.S3/S3-(6).png" alt="S3" >}}

2. Tạo 1 **file txt**
- Đặt tên là `ThreatList.txt`
- Paste IP của EC2 độc hại vào **file txt** đó

{{< img src="/images/3.S3/S3-(7).png" alt="S3" >}}

3. Tiến hành Upload **file txt** đó lên **S3**

{{< img src="/images/3.S3/S3-(8).png" alt="S3" >}}

{{< img src="/images/3.S3/S3-(9).png" alt="S3" >}}

4. Sau khi Upload thành công thì tiến hành Copy **Object URL**

{{< img src="/images/3.S3/S3-(10).png" alt="S3" >}}