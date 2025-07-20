---
title : "EventBridge"
date : "2025-07-03"
weight : 6
chapter : false
pre : " <b> 6. </b> "
---

#### Configure EventBridge
1. Go to the **Amazon EventBridge** interface
- Select **EventBridge Rule**
- Select **Create rule**

{{< img src="/images/6.eventbridge/EventBridge-(1" alt="EventBridge" >}}.png)

2. Proceed with configuration
- Set **Name** to `EventBridge-Lambda`
- Set **Description** to `EventBridge from GuardDuty to Lambda`
- Select **Next**

{{< img src="/images/6.eventbridge/EventBridge-(2" alt="EventBridge" >}}.png)

3. Configure **Event**
- Select **Other**
- Select **Custom pattern (JSON editor)**

{{< img src="/images/6.eventbridge/EventBridge-(3" alt="EventBridge" >}}.png)

4. Paste this JSON into **Event pattern**
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
We will capture Findings from GuardDuty with severity levels: 4, 5, 6, 7, 8. And only capture Findings from Instances
{{% /notice %}}

{{< img src="/images/6.eventbridge/EventBridge-(4" alt="EventBridge" >}}.png)

5. Select **Target** for the **rule**
- Select **AWS Service** for **Target types**
- Select **Lambda function** for **Select a target**
- Select **Target in this account** for **Target location**
- Select **Auto-Isolate-Lambda** for **Function**

{{< img src="/images/6.eventbridge/EventBridge-(5" alt="EventBridge" >}}.png)

6. Continue by selecting **Next**

{{< img src="/images/6.eventbridge/EventBridge-(6" alt="EventBridge" >}}.png)

7. Select **Create rule**

{{< img src="/images/6.eventbridge/EventBridge-(7" alt="EventBridge" >}}.png)