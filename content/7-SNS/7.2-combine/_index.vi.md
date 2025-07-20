---
title : "Kết hợp với Lambda"
date :  "2025-07-03" 
weight : 2 
chapter : false
pre : " <b> 7.2 </b> "
---

#### Kết hợp các thành phần với Lambda
1. Truy cập giao diện **Lambda**
- Vào lại môi trường Lambda lúc nãy đã tạo
- Chọn **Add trigger**

{{< img src="/images/7.sns/Combine-(1).png" alt="Combine" >}}

2. Trong giao diện **Add trigger**
- **Trigger configuration** chọn là **EventBridge**
- **Rule** chọn là **Existing rule**

{{< img src="/images/7.sns/Combine-(2).png" alt="Combine" >}}

3. Bấm **Add** để tiến hành thêm trigger

{{< img src="/images/7.sns/Combine-(3).png" alt="Combine" >}}

4. Tiếp theo chọn **Add destination**

{{< img src="/images/7.sns/Combine-(4).png" alt="Combine" >}}

5. Trong giao diện **Destination configuration** 
- **Condition** thì chọn là **On success**
- **Destination type** thì ta chọn là **SNS topic**
- Chọn **Save**
{{< img src="/images/7.sns/Combine-(5).png" alt="Combine" >}}

6. Kiểm tra lại môi trường **Lambda** 

{{< img src="/images/7.sns/Combine-(6).png" alt="Combine" >}}
