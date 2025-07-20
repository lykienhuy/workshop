---
title : "Giới thiệu"
date :  "2025-07-03" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
{{< img src="/images/Guardduty2.drawio.png" alt="Introduce" >}} 
#### Luồng hoạt động

***1: Traffic độc hại từ Compromised EC2 đến Malicious EC2***

EC2 bị nghi ngờ xâm nhập (Compromised EC2) thực hiện kết nối ra ngoài tới một EC2 có EIP nằm trong danh sách đe dọa (Malicious EC2). Đây là hành vi tiềm ẩn tấn công (ví dụ như scan cổng, brute force, malware, ...)

***2: GuardDuty kiểm tra Threat List***

GuardDuty sẽ sử dụng Threat IP List, trong đó có danh sách IP từ S3 Bucket (Threat List) do người điều hành cung cấp.
Khi phát hiện EIP nằm trong danh sách này, GuardDuty sinh ra một Finding (sự kiện phát hiện nguy cơ bảo mật )

***3: Finding được gửi đến Amazon EventBridge***

Sự kiện phát hiện (Finding) từ GuardDuty sẽ được tự động gửi vào EventBridge Rule nếu khớp điều kiện (ví dụ: type = Recon:EC2/PortScan,"severity": [4, 5, 6, 7, 8],...)

***4: EventBridge kích hoạt Lambda Function***

Lambda sẽ được EventBridge gọi để thực hiện hành động phản ứng tự động.
Logic bên trong Lambda gồm:
- Xác định InstanceId của EC2 bị nghi nhiễm
- Tiến hành ngừng EC2 Instance đó để tránh bị khai thác dữ liệu
- Thay đổi Security Group của Instance đó thành Isolated Security Group (SG giới hạn hoặc cấm toàn bộ lưu lượng) 

***5: Lambda tiến hành cách ly Compromised EC2***

Do đã được gán Isolated Security Group, EC2 bị nghi nhiễm sẽ không thể giao tiếp ra ngoài nữa.
Điều này giúp ngăn chặn lây lan hoặc tiếp tục khai thác.

***6: Lambda gửi cảnh báo qua SNS***

Sau khi cách ly xong, Lambda gửi thông tin cảnh báo đến Amazon SNS
SNS sẽ gửi Email đến người điều hành bao gồm log và thông báo đã cách ly thành công EC2 sang một Security Group khác
