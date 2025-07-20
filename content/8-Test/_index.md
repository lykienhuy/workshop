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

{{< img src="/images/8.test/Test-(1).png" alt="Test" >}}

2. Proceed to connect via SSH to **Compromised_EC2**

{{< img src="/images/8.test/Test-(2).png" alt="Test" >}}

3. Perform an update
```
sudo yum update -y
```
{{< img src="/images/8.test/Test-(3).png" alt="Test" >}}

4. Proceed to **ping** the IPv4 address of **Malicious_EC2** which is in the Threat list of **GuardDuty**

{{< img src="/images/8.test/Test-(4).png" alt="Test" >}}

5. If this message appears, it indicates that **Lambda** is working
{{< img src="/images/8.test/Test-(5).png" alt="Test" >}}

6. Check the **EC2** instance
- See if the EC2 has been stopped
- Check if it has been isolated to the **Isolated-Security-Group**

{{< img src="/images/8.test/Test-(6).png" alt="Test" >}}

{{< img src="/images/8.test/Test-(7).png" alt="Test" >}}

7. Check the **Finding** from **GuardDuty**
- Select **Findings**
- You will see a notification that "**EC2 is connecting to an IP in the Threat list**"
- The Severity level is **Medium**

{{< img src="/images/8.test/Test-(8).png" alt="Test" >}}

8. Click on the detected **Finding** to view details
{{< img src="/images/8.test/Test-(9).png" alt="Test" >}}

9. Check your Email for notifications

{{< img src="/images/8.test/Test-(10).png" alt="Test" >}}