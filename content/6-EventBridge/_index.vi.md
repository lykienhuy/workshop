---
title : "EventBridge"
date :  "2025-07-03" 
weight : 6 
chapter : false
pre : " <b> 6. </b> "
---

#### Cấu hình EventBridge
1. Vào giao diện **Amazon EventBridge**
- Chọn **EventBridge Rule**
- Chọn **Create rule**

{{< img src="/images/6.eventbridge/EventBridge-(1).png" alt="EventBridge" >}}

2. Tiến hành cấu hình
- **Name** đặt là `EventBridge-Lambda`
- **Description** đặt là `EventBridge from GuardDuty to Lambda`
- Chọn **Next**

{{< img src="/images/6.eventbridge/EventBridge-(2).png" alt="EventBridge" >}}

3. Cấu hình **Event**
- Chọn **Other**
- Chọn **Custom pattern (JSON editor)**

{{< img src="/images/6.eventbridge/EventBridge-(3).png" alt="EventBridge" >}}

4. Tiến hành paste đoạn này JSON vào **Event pattern**
```
{
  "source": ["aws.guardduty"],
  "detail-type": ["GuardDuty Finding"],
  "detail": {
    "severity": [4, 5, 6, 7, 8],
    "resource": {
      "resourceType": ["Instance"]
    }
  }
}
```
{{% notice note %}}
Ta sẽ bắt những Finding từ GuardDuty có mức độ severity là: 4, 5, 6, 7, 8. Và chỉ bắt các Finding từ các Instance
{{% /notice %}}

{{< img src="/images/6.eventbridge/EventBridge-(4).png" alt="EventBridge" >}}

5. Chọn **Target** cho **rule**
- **Target types** chọn là **AWS Service**
- **Select a target** chọn là **Lambda function**
- **Target location** chọn là **Target in this account**
- **Function** chọn là **Auto-Isolate-Lambda**

{{< img src="/images/6.eventbridge/EventBridge-(5).png" alt="EventBridge" >}}

6. Tiếp tục chọn **Next**

{{< img src="/images/6.eventbridge/EventBridge-(6).png" alt="EventBridge" >}}

7. Chọn **Create rule**

{{< img src="/images/6.eventbridge/EventBridge-(7).png" alt="EventBridge" >}}