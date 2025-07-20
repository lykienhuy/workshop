---
title : "Hệ thống Quét Bảo mật Tự động sử dụng GuardDuty và Lambda function"
date :  "2025-07-03" 
weight : 1 
chapter : false
---
# Hệ thống Quét Bảo mật Tự động sử dụng GuardDuty và Lambda function

### Tổng quan

 Trong bài thực hành này, bạn sẽ học các khái niệm cơ bản và thực hành với Amazon GuardDuty và Lambda function

{{< img src="/images/Guardduty.drawio.png" alt="ConnectPrivate" >}} 

#### Amazon GuardDuty
**Amazon GuardDuty** là dịch vụ phát hiện mối đe dọa được quản lý hoàn toàn bởi AWS. Nó giúp bạn giám sát và bảo vệ các tài nguyên AWS như tài khoản IAM, EC2, S3, Lambda... khỏi các hành vi độc hại hoặc trái phép.

#### Lambda Function
**Lambda Function** là dịch vụ điện toán không máy chủ giúp bạn chạy mã mà không cần quản lý máy chủ.

#### Amazon CloudWatch
**Amazon CloudWatch** là dịch vụ giám sát và quan sát trong AWS, cho phép bạn
thu thập, theo dõi và phân tích nhật ký, số liệu và sự kiện từ các dịch vụ và ứng dụng AWS. Nó giúp kích hoạt Lambda, EC2 Auto Scaling hoặc gửi thông báo qua SNS.

#### Amazon EventBridge
**Amazon EventBridge** là dịch vụ bus sự kiện được quản lý hoàn toàn giúp kết nối các dịch vụ AWS, ứng dụng SaaS hoặc ứng dụng tùy chỉnh thông qua các sự kiện thời gian thực.

#### Amazon S3 Bucket
**Amazon S3** là dịch vụ lưu trữ đối tượng linh hoạt, bền vững và có khả năng mở rộng vô hạn của AWS. S3 Bucket là một container chứa các đối tượng như tệp, hình ảnh, video, dữ liệu sao lưu, nhật ký hệ thống.

#### Amazon SNS
**Amazon SNS** là dịch vụ nhắn tin pub/sub (xuất bản/đăng ký) được quản lý hoàn toàn bởi AWS. Nó cho phép bạn gửi thông báo tự động từ hệ thống, ứng dụng hoặc dịch vụ AWS đến nhiều người nhận (người đăng ký).
### Nội dung

 1. [Giới thiệu](1-introduce/)
 2. [Chuẩn bị](2-Prerequiste/)
 3. [Tạo S3 Bucket](3-s3/)
 4. [Kích hoạt GuardDuty](4-guardduty/)
 5. [Lambda function](5-lambdafunction/)
 6. [EventBridge](6-eventbridge/)
 7. [SNS](7-sns/)
 8. [Kiểm tra Kết quả](8-test/)
 9. [Dọn dẹp tài nguyên](9-clean/)