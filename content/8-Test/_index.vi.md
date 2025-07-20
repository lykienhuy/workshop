---
title : "Kiểm tra kết quả"
date : "2025-07-03"
weight : 8
chapter : false
pre : "<b>8. </b>"
---
#### Kiểm tra kết quả

Để biết được Lambda có hoạt động hay không thì ta sẽ tiến hành tạo một Finding đơn giản để xem phản ứng của Lambda như thế nào

1. Ta sẽ kiểm tra xem 2 EC2 ta đã tạo có phải nằm trong **Security-Group** không ( không được nằm trong **Isolated-Security-Group**)

![Test](/images/8.test/Test-(1).png)

2. Tiến hành kết nối SSH với **Compromised_EC2**

![Test](/images/8.test/Test-(2).png)

3. Tiến hành Update
```
sudo yum update -y
```
![Test](/images/8.test/Test-(3).png)

4. Tiến hành **ping** vào IPv4 của **Malicious_EC2** đang nằm trong Threat list của **GuardDuty**

![Test](/images/8.test/Test-(4).png)

5. Nếu hiện thông báo này thì chứng tỏ **Lambda** đã hoạt động
![Test](/images/8.test/Test-(5).png)

6. Tiến hành kiểm tra **EC2**
- Xem EC2 đã tắt chưa
- Đã cách ly sang **Isolated-Security-Group** chưa

![Test](/images/8.test/Test-(6).png)

![Test](/images/8.test/Test-(7).png)

7. Kiểm tra **Finding** từ **GuardDuty**
- Chọn **Findings**
- Ta sẽ thấy có dòng thông báo là "**EC2 đang kết nối với một IP nằm trong Threat list**""
- Mức độ Severity là **Medium**

![Test](/images/8.test/Test-(8).png)

8. Bấm vào **Finding** vừa phát hiện để xem chi tiết
![Test](/images/8.test/Test-(9).png)

9. Kiểm tra Email để xem thông báo

![Test](/images/8.test/Test-(10).png)