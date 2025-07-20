---
title : "Automated Security Scanning System using GuardDuty and Lambda function"
date :  "2025-07-03" 
weight : 1 
chapter : false
---
# Automated Security Scanning System using GuardDuty and Lambda function

### Overview

 In this lab, you will learn the basic concepts and practice with Amazon GuardDuty and Lambda function

![ConnectPrivate](/images/Guardduty.drawio.png) 
#### Amazon GuardDuty
**Amazon GuardDuty** is a fully managed threat detection service by AWS. It helps you monitor and protect AWS resources such as IAM accounts, EC2, S3, Lambda... from malicious or unauthorized behaviors.

#### Lambda Function
**Lambda Function** is a serverless computing service that helps you run code without managing servers.

#### Amazon CloudWatch
**Amazon CloudWatch** is a monitoring and observability service in AWS, allowing you to
collect, track, and analyze logs, metrics, and events from AWS services and applications. It helps trigger Lambda, EC2 Auto Scaling, or send notifications via SNS.

#### Amazon EventBridge
**Amazon EventBridge** is a fully managed event bus service that helps connect AWS services, SaaS applications, or custom applications through real-time events.

#### Amazon S3 Bucket
**Amazon S3** is AWS's flexible, durable, and infinitely scalable object storage service. An S3 Bucket is a container for objects such as files, images, videos, backup data, system logs.

#### Amazon SNS
**Amazon SNS** is a fully managed pub/sub (publish/subscribe) messaging service by AWS. It allows you to send automated notifications from systems, applications, or AWS services to multiple recipients (subscribers).
### Content

 1. [Introduction](1-introduce/)
 2. [Preparation](2-Prerequiste/)
 3. [Create S3 Bucket](3-s3/)
 4. [Activate GuardDuty](4-guardduty/)
 5. [Lambda function](5-lambdafunction/)
 6. [EventBridge](6-eventbridge/)
 7. [SNS](7-sns/)
 8. [Test Results](8-test/)
 9. [Clean up resources](9-clean/)