---
title : "Tạo SNS Topic"
date :  "2025-07-03" 
weight : 1 
chapter : false
pre : " <b> 7.1 </b> "
---

#### Tạo SNS Topic
1. Truy cập giao diện **Amazon SNS**
- Chọn **Topics**
- Chọn **Create topic**

{{< img src="/images/7.sns/SNS-(1" alt="SNS" >}}.png)

2. Trong giao diện **Create topic**
- **Type** chọn là **Standard**
- **Name** đặt là `Lambda_SNS`
- **Display name** đặt là `SNS Topic`

{{< img src="/images/7.sns/SNS-(2" alt="SNS" >}}.png)

3. Bấm **Create topic**

{{< img src="/images/7.sns/SNS-(3" alt="SNS" >}}.png)

4. Sau khi tạo xong thì bấm **Create subscription**

{{< img src="/images/7.sns/SNS-(4" alt="SNS" >}}.png)

5. Tạo **Subscription** 
- **Topic ARN** thì ta sẽ chọn ARN của **Lambda_SNS** 
- **Protocol** thì ta chọn là **email** (Gửi qua email)
- **Endpoint** ta sẽ nhập email nhận thông báo vào (Có thể là email của mình)

{{< img src="/images/7.sns/SNS-(5" alt="SNS" >}}.png)

6. Chọn **Create subscription**

{{< img src="/images/7.sns/SNS-(6" alt="SNS" >}}.png)

7. Check **Email** để **confirm subscription**
{{< img src="/images/7.sns/SNS-(7" alt="SNS" >}}.png)
{{< img src="/images/7.sns/SNS-(8" alt="SNS" >}}.png)