---
title : "Dọn dẹp tài nguyên"
date : "2025-07-03"
weight : 9
chapter : false
pre : "<b>9. </b>"
---

Chúng ta sẽ tiến hành các bước sau để xóa các tài nguyên chúng ta đã tạo trong bài thực hành này
#### Xóa EC2 Instance
- Truy cập EC2 Management Console
- Trên thanh điều hướng bên trái, chọn Intances
- Chọn tất cả EC2 Instance liên quan tới bài lab
- Chọn Actions
- Chọn Terminate

![Clean](/images/9.clean/Clear-(1).png)

#### Xóa Security Group
- Mở Amazon VPC Console
- Chọn Security Groups từ thanh điều hướng bên trái
- Chọn Security Group liên quan đến bài lab
- Nhấp vào Actions, chọn Delete security group
- Nhấp vào Delete để xác nhận

![Clean](/images/9.clean/Clear-(2).png)

#### Xóa S3 Bucket
1. Empty S3 Bucket
- Truy cập AWS S3
- Trong danh sách Bucket name, chọn bucket liên quan bài lab
- Chọn Empty
- Trong trang Empty bucket, xác nhận và chọn Empty
2. Xóa S3 Bucket
- Truy cập vào AWS S3
- Chọn S3 bucket liên quan bài lab.
- Chọn Delete
- Điền tên S3 và chọn Delete bucket

![Clean](/images/9.clean/Clear-(6).png)

![Clean](/images/9.clean/Clear-(7).png)

#### Xóa Threat list IP trong GuardDuty
- Truy cập vào GuardDuty
- Chọn Settings/Lists
- Chọn Threat list đã tạo trong bài lab này
- Chọn Actions/Delete

![Clean](/images/9.clean/Clear-(8).png)

#### Xóa Rule EventBridge
- Truy cập vào EventBridge
- Chọn Rule
- Chọn Rule đã tạo trong bài lab này
- Chọn Actions
- Nhập delete

![Clean](/images/9.clean/Clear-(9).png)

#### Xóa Lambda function
- Truy cập vào AWS Lambda
- Chọn các Function liên quan bài lab
- Chọn Delete
- Nhập confirm

![Clean](/images/9.clean/Clear-(10).png)

#### Xóa SNS Topic
- Truy cập vào Amazon SNS
- Chọn Topics
- Chọn Topics đã tạo trong bài lab
- Chọn Delete
- Nhập delete me

![Clean](/images/9.clean/Clear-(11).png)