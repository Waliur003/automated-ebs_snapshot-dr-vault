# Cloud Engineering Project 01: Automated EBS Snapshot & DR Vault

## _Overview_
This project implements an automated, event-driven **Disaster Recovery (DR)** solution on AWS. It uses **Amazon EventBridge** to trigger an **AWS Lambda** function on a schedule, which identifies and backs up critical **EBS volumes** based on **resource tags**.

---

## _The Problem_
In enterprise environments, manual backups are inconsistent and prone to human error. Without a standardized policy, businesses risk **data loss** or **overpaying for storage** by backing up non-essential resources.

---

## _The Solution_
- **Tag-Based Governance:** Only volumes with the tag **`Backup: True`** are snapshotted, ensuring cost-effective resource management.
- **Serverless Automation:** Uses **AWS Lambda** to eliminate the need for managing backup servers.
- **Operational Visibility:** Success/failure logs are automatically captured in **CloudWatch Logs**.

---

## _Tech Stack_
- **Compute:** AWS Lambda _(Python 3.12)_
- **Storage:** Amazon EBS _(Elastic Block Store)_
- **Trigger:** Amazon EventBridge _(CloudWatch Events)_
- **Security:** IAM _(Least Privilege Policies)_

---

## _Project Procedure_
I designed and implemented an automated disaster recovery solution to protect critical data volumes on AWS. Below is the step-by-step procedure followed:

### 1) _Resource Tagging Policy_
- Established a resource tagging policy.
- Applied the tag **`Backup: True`** to specific EBS volumes.
- Ensures the automation script only processes **critical** data.
- Prevents unnecessary snapshot storage costs.

### 2) _Least-Privilege IAM Role_
- Created a custom IAM policy with:
  - **`ec2:CreateSnapshot`**
  - **`ec2:DescribeVolumes`**
- Attached the policy to a dedicated **Lambda execution role**.
- Ensures secure, identity-driven access following **least privilege**.

### 3) _Python-Based Lambda Function_
- Developed a Python script using the **Boto3 SDK** to:
  - Filter EBS volumes by tag
  - Initiate snapshot creation
- Integrated error handling so that:
  - Successful backups are logged
  - Failed attempts are captured with details in logs

### 4) _Event-Driven Trigger (EventBridge)_
- Used **Amazon EventBridge** to configure a **Cron** schedule.
- Verified the system triggers automatically every **24 hours**.
- Requires **no manual intervention** after setup.

### 5) _Disaster Recovery Pipeline Verification_
- Performed manual tests to confirm snapshots appear in the **EC2 console**.
- Monitored **CloudWatch Logs** to verify:
  - Execution success/failure visibility
  - Runtime and memory usage stays within **AWS Free Tier** limits

---

## _Architecture Diagram_
<img width="1169" height="827" alt="image" src="https://github.com/user-attachments/assets/d4ea48b8-d638-43e4-a21a-3f83b53487eb" />

---

## _Screenshots_



### _1) Tagged EBS Volume (`Backup: True`)_
<img width="1916" height="822" alt="Screenshot 1" src="https://github.com/user-attachments/assets/d4f0e63e-ec6d-4126-988a-99eaecd5e154" />

### _2) Lambda Function (Code + Configuration)_
<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/f08188a7-e1c7-4bb4-a186-8bdee950f3d3" />

### _3) EventBridge Schedule Rule (Cron)_
<img width="1900" height="827" alt="image" src="https://github.com/user-attachments/assets/613efa25-6b29-49ba-b031-45da2071c1ae" />

### _4) Snapshots Created in EC2 Console_
<img width="1917" height="866" alt="image" src="https://github.com/user-attachments/assets/c12f966f-25cf-4854-92d7-1c56b589a952" />





---




---

## _Notes / Future Improvements_ 
- Add snapshot **retention** (delete snapshots older than _N_ days).
- Add **SNS notifications** for failure alerts.
- Copy snapshots to another region for **cross-region DR**.
- Implement **AWS Backup Vault** + lifecycle policies for centralized governance.








