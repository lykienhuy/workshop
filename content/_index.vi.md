---
title : "Automated Security Scanning System using GuardDuty and Lambda function"
date :  "2025-07-03" 
weight : 1 
chapter : false
---
# Hệ thống quét bảo mật tự động bằng GuardDuty và Lambda function

### Tổng quan

 Trong bài lab này, bạn sẽ tìm hiểu các khái niệm cơ bản và thực hành về Amazon GuardDuty và Lambda function

![ConnectPrivate](/images/Guardduty.drawio.png) 
#### Amazon GuardDuty
**Amazon GuardDuty** là một dịch vụ phát hiện mối đe dọa (threat detection) được quản lý hoàn toàn bởi AWS. Nó giúp bạn giám sát và bảo vệ tài nguyên AWS như tài khoản IAM, EC2, S3, Lambda... khỏi các hành vi độc hại hoặc trái phép. 

#### Lambda Function
**Lambda Function** là một dịch vụ điện toán không máy chủ (serverless) giúp bạn chạy mã nguồn mà không cần quản lý máy chủ.

#### Amazon CloudWatch
**Amazon CloudWatch** là một dịch vụ giám sát (monitoring) và quan sát hệ thống (observability) trong AWS, cho phép bạn
thu thập, theo dõi và phân tích log, metric và sự kiện từ các dịch vụ AWS và ứng dụng. Giúp kích hoạt Lambda, EC2 Auto Scaling, hoặc gửi thông báo qua SNS.

#### Amazon EventBridge
**Amazon EventBridge** là một dịch vụ bus sự kiện (event bus) được quản lý hoàn toàn, giúp kết nối các dịch vụ AWS, ứng dụng SaaS, hoặc ứng dụng tùy chỉnh thông qua các sự kiện theo thời gian thực.

#### Amazon S3 Bucket
**Amazon S3** là dịch vụ lưu trữ đối tượng (object storage) linh hoạt, bền vững và có thể mở rộng không giới hạn của AWS. Một S3 Bucket là nơi chứa các đối tượng như file, ảnh, video, dữ liệu backup, log hệ thống.

#### Amazon SNS
**Amazon SNS** là một dịch vụ nhắn tin pub/sub (publish/subscribe) được quản lý hoàn toàn bởi AWS. Nó cho phép bạn gửi thông báo tự động từ các hệ thống, ứng dụng hoặc dịch vụ AWS đến nhiều người nhận  (subscriber).
### Nội dung

 1. [Giới thiệu](1-introduce/)
 2. [Các bước chuẩn bị](2-prerequiste/)
 3. [Tạo S3 Bucket](3-s3/)
 4. [Kích hoạt GuardDuty](4-guardduty/)
 5. [Lambda function](5-lambdafunction/)
 6. [EventBridge](6-eventbridge/)
 7. [SNS](7-sns/)
 8. [Kiểm tra kết quả](8-test/)
 9. [Dọn dẹp tài nguyên](9-clean/)