---
title : "Kích hoạt GuardDuty"
date :  "2025-07-03" 
weight : 4 
chapter : false
pre : " <b> 4. </b> "
---

#### Kích hoạt GuardDuty
Sau khi ta Enabled GuardDuty thì ta sẽ có giao diện như sau

![GuardDuty](/images/4.guardduty/GuardDuty-(1).png)

#### Tiến hành thêm Threat list vào GuardDuty
1. Vào **Settings**
- Chọn **Lists**
- Chọn **Add a threat IP list**

![GuardDuty](/images/4.guardduty/GuardDuty-(2).png)

2. Tiến hành thêm danh sách lọc cho GuardDuty
- **List name** ta sẽ đặt tên là `ThreatList`
- **Location** ta sẽ paste đoạn **Object URL** mà ta đã copy ở S3 vào
- **List format** ta sẽ chọn là **Plaintext**
-  Chọn **Add list** để tiến hành thêm danh sách

![GuardDuty](/images/4.guardduty/GuardDuty-(3).png)

3. Sau khi thêm danh sách
- Chọn **Actions/Activate** để kích hoạt danh sách đã thêm

![GuardDuty](/images/4.guardduty/GuardDuty-(4).png)
