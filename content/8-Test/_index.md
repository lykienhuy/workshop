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

{{< img src="/images/8.test/Test-(1" alt="Test" >}}.png)

2. Proceed to connect via SSH to **Compromised_EC2**

{{< img src="/images/8.test/Test-(2" alt="Test" >}}.png)

3. Perform an update
```
sudo yum update -y
```
{{< img src="/images/8.test/Test-(3" alt="Test" >}}.png)

4. Proceed to **ping** the IPv4 address of **Malicious_EC2** which is in the Threat list of **GuardDuty**

{{< img src="/images/8.test/Test-(4" alt="Test" >}}.png)

5. If this message appears, it indicates that **Lambda** is working
{{< img src="/images/8.test/Test-(5" alt="Test" >}}.png)

6. Check the **EC2** instance
- See if the EC2 has been stopped
- Check if it has been isolated to the **Isolated-Security-Group**

{{< img src="/images/8.test/Test-(6" alt="Test" >}}.png)

{{< img src="/images/8.test/Test-(7" alt="Test" >}}.png)

7. Check the **Finding** from **GuardDuty**
- Select **Findings**
- You will see a notification that "**EC2 is connecting to an IP in the Threat list**"
- The Severity level is **Medium**

{{< img src="/images/8.test/Test-(8" alt="Test" >}}.png)

8. Click on the detected **Finding** to view details
{{< img src="/images/8.test/Test-(9" alt="Test" >}}.png)

9. Check your Email for notifications

{{< img src="/images/8.test/Test-(10" alt="Test" >}}.png)