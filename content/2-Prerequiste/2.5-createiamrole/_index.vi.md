---
title : "Tạo Role cho Lambda"
date :  "2025-07-03" 
weight : 5
chapter : false
pre : " <b> 2.5 </b> "
---

### Tạo Role cho Lambda

Trong bước này chúng ta sẽ tiến hành tạo Role cho Lambda. Trong Role này sẽ được gán các policy như sau:

- `AmazonEC2FullAccess`
- `AWSLambda_FullAccess`
- `AWSLambdaBasicExecutionRole`
- `CloudWatchEventsFullAccess`

{{% notice warning %}}
Thực tế các thiết lập IAM luôn được áp dụng nguyên tắc Least Privilege (Chỉ được cấp quyền tối thiểu để thực hiện đúng chức năng của nó). Nhưng đây là bài lab nên ta sẽ áp dụng IAM FullAccess cho đơn giản.
{{% /notice %}}

1. Truy cập giao diện **IAM**
- Chọn **Roles**
- Chọn **Create role**

{{< img src="/images/2.prerequisite/Chuanbi-(18" alt="EC2" >}}.png)

2. Trong giao diện **Trusted entity type**
- Chọn **AWS service**
- Chọn **Lambda**
- Chọn **Next**

{{< img src="/images/2.prerequisite/Chuanbi-(19" alt="EC2" >}}.png)

3. Trong giao diện **Add permissions**
- Tìm **AmazonEC2FullAccess**
- Chọn **AmazonEC2FullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(21" alt="EC2" >}}.png)

- Tìm **AWSLambda_FullAccess**
- Chọn **AWSLambda_FullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(20" alt="EC2" >}}.png)

- Tìm **AWSLambdaBasicExecutionRole**
- Chọn **AWSLamdaBasicExecutionRole**

{{< img src="/images/2.prerequisite/Chuanbi-(22" alt="EC2" >}}.png)

- Tìm **CloudWatchEventsFullAccess**
- Chọn **CloudWatchEventsFullAccess**

{{< img src="/images/2.prerequisite/Chuanbi-(23" alt="EC2" >}}.png)

4. Trong phần **Name, review, create**
- **Role name** là `Lambda_Role`
- **Description** là `Allows Lambda functions to call AWS services on yor behalf`

{{< img src="/images/2.prerequisite/Chuanbi-(24" alt="EC2" >}}.png)

5. Chọn **Create role**

{{< img src="/images/2.prerequisite/Chuanbi-(25" alt="EC2" >}}.png)