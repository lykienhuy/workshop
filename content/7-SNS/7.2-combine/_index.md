---
title : "Combine with Lambda"
date : "2025-07-03"
weight : 2
chapter : false
pre : " <b> 7.2 </b> "
---

#### Combine components with Lambda
1. Access the **Lambda** interface
- Return to the Lambda environment we created earlier
- Select **Add trigger**

{{< img src="/images/7.sns/Combine-(1).png" alt="Combine" >}}

2. In the **Add trigger** interface
- Select **EventBridge** for **Trigger configuration**
- Select **Existing rule** for **Rule**

{{< img src="/images/7.sns/Combine-(2).png" alt="Combine" >}}

3. Click **Add** to add the trigger

{{< img src="/images/7.sns/Combine-(3).png" alt="Combine" >}}

4. Next, select **Add destination**

{{< img src="/images/7.sns/Combine-(4).png" alt="Combine" >}}

5. In the **Destination configuration** interface
- Select **On success** for **Condition**
- Select **SNS topic** for **Destination type**
- Click **Save**
{{< img src="/images/7.sns/Combine-(5).png" alt="Combine" >}}

6. Verify the **Lambda** environment

{{< img src="/images/7.sns/Combine-(6).png" alt="Combine" >}}