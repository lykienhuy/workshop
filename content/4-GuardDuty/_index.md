---
title : "Activate GuardDuty"
date : "2025-07-03"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

#### Activate GuardDuty
After we Enable GuardDuty, we will have the following interface

![GuardDuty](/images/4.guardduty/GuardDuty-(1).png)

#### Add Threat list to GuardDuty
1. Go to **Settings**
- Select **Lists**
- Select **Add a threat IP list**

![GuardDuty](/images/4.guardduty/GuardDuty-(2).png)

2. Add filter list for GuardDuty
- For **List name** we will name it `ThreatList`
- For **Location** we will paste the **Object URL** that we copied from S3
- For **List format** we will select **Plaintext**
- Select **Add list** to add the list

![GuardDuty](/images/4.guardduty/GuardDuty-(3).png)

3. After adding the list
- Select **Actions/Activate** to activate the added list

![GuardDuty](/images/4.guardduty/GuardDuty-(4).png)