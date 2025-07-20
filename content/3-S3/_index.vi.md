---
title : "Tạo S3 Bucket"
date :  "2025-07-03" 
weight : 3 
chapter : false
pre : " <b> 3. </b> "
---
### Tổng quan
Trong bước này, chúng ta sẽ tạo một S3 Bucket dùng để lưu trữ các IP của EC2 độc hại (Threat list).
{{% notice info %}}
GuardDuty sẽ dựa theo file mà ta đã upload lên để lọc.
{{% /notice %}}

![S3](/images/S3.png)
### Nội dung
- [Tạo S3 Bucket](3.1-creates3/) 
- [Tải Threat list lên S3](3.2-uploadthreatlist/)