---
title : "Test Results"
date : "2025-07-03"
weight : 8
chapter : false
pre : "<b>8. </b>"
---
#### Test Results

To determine if Lambda is working properly, we will create a simple Finding to see how Lambda responds.

1. We will check if the 2 EC2 instances we created are in the **Security-Group** (they should not be in the **Isolated-Security-Group**)

![Test](/images/8.test/Test-(1).png)

2. Proceed to connect via SSH to **Compromised_EC2**

![Test](/images/8.test/Test-(2).png)

3. Perform an update
```
sudo yum update -y
```
![Test](/images/8.test/Test-(3).png)

4. Proceed to **ping** the IPv4 address of **Malicious_EC2** which is in the Threat list of **GuardDuty**

![Test](/images/8.test/Test-(4).png)

5. If this message appears, it indicates that **Lambda** is working
![Test](/images/8.test/Test-(5).png)

6. Check the **EC2** instance
- See if the EC2 has been stopped
- Check if it has been isolated to the **Isolated-Security-Group**

![Test](/images/8.test/Test-(6).png)

![Test](/images/8.test/Test-(7).png)

7. Check the **Finding** from **GuardDuty**
- Select **Findings**
- You will see a notification that "**EC2 is connecting to an IP in the Threat list**"
- The Severity level is **Medium**

![Test](/images/8.test/Test-(8).png)

8. Click on the detected **Finding** to view details
![Test](/images/8.test/Test-(9).png)

9. Check your Email for notifications

![Test](/images/8.test/Test-(10).png)