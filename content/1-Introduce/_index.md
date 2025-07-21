---
title : "Introduction"
date :  "2025-07-03" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
{{< img src="/images/guardduty2.drawio.png" alt="Introduce" >}} 
#### Workflow

***1: Malicious Traffic from Compromised EC2 to Malicious EC2***

The suspected compromised EC2 instance establishes an outbound connection to another EC2 instance with an EIP listed in the threat list (Malicious EC2). This behavior indicates potential attacks (such as port scanning, brute force attempts, malware, etc.)

***2: GuardDuty checks the Threat List***

GuardDuty uses the Threat IP List, which includes IP addresses from an S3 Bucket (Threat List) provided by the administrator.
When an EIP is detected in this list, GuardDuty generates a Finding (security threat detection event).

***3: Finding is sent to Amazon EventBridge***

The detection event (Finding) from GuardDuty is automatically sent to an EventBridge Rule if it matches certain conditions (e.g., type = Recon:EC2/PortScan, "severity": [4, 5, 6, 7, 8], etc.)

***4: EventBridge triggers Lambda Function***

Lambda is invoked by EventBridge to perform automated response actions.
The Lambda logic includes:
- Identifying the InstanceId of the suspected compromised EC2
- Stopping the EC2 Instance to prevent data exploitation
- Changing the Security Group of that Instance to an Isolated Security Group (SG that limits or blocks all traffic)

***5: Lambda isolates the Compromised EC2***

After being assigned the Isolated Security Group, the suspected compromised EC2 can no longer communicate externally.
This helps prevent further spread or exploitation.

***6: Lambda sends alerts via SNS***

After successful isolation, Lambda sends alert information to Amazon SNS.
SNS sends an email to the administrator including logs and notification that the EC2 has been successfully isolated to a different Security Group.