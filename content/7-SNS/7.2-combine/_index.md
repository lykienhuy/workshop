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

![Combine](/images/7.sns/Combine-(1).png)

2. In the **Add trigger** interface
- Select **EventBridge** for **Trigger configuration**
- Select **Existing rule** for **Rule**

![Combine](/images/7.sns/Combine-(2).png)

3. Click **Add** to add the trigger

![Combine](/images/7.sns/Combine-(3).png)

4. Next, select **Add destination**

![Combine](/images/7.sns/Combine-(4).png)

5. In the **Destination configuration** interface
- Select **On success** for **Condition**
- Select **SNS topic** for **Destination type**
- Click **Save**
![Combine](/images/7.sns/Combine-(5).png)

6. Verify the **Lambda** environment

![Combine](/images/7.sns/Combine-(6).png)