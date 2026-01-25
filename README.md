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
![Architecture Diagram of Project 1](https://github.com/user-attachments/assets/f5535c47-4c11-4af7-bf04-db7d662064b8)


---

## _Screenshots_



### _1) Tagged EBS Volume (`Backup: True`)_
<img width="1916" height="822" alt="Screenshot 1" src="https://github.com/user-attachments/assets/54011cf0-959b-47af-a0cc-2eb7be19e503" />


### _2) Lambda Function (Code + Configuration)_
<img width="1918" height="862" alt="Screenshot 2" src="https://github.com/user-attachments/assets/12b44aed-61be-41d4-847a-0da3f5f513c3" />


### _3) EventBridge Schedule Rule (Cron)_
<img width="1900" height="827" alt="Screenshot 3" src="https://github.com/user-attachments/assets/bf0edf64-bbb5-489f-8363-8612b63205f7" />


### _4) Snapshots Created in EC2 Console_
<img width="1917" height="866" alt="Screenshot 4" src="https://github.com/user-attachments/assets/e3badf2e-d9b0-486c-ac83-07e940be97f0" />






---




---

## _Notes / Future Improvements_ 
- Add snapshot **retention** (delete snapshots older than _N_ days).
- Add **SNS notifications** for failure alerts.
- Copy snapshots to another region for **cross-region DR**.
- Implement **AWS Backup Vault** + lifecycle policies for centralized governance.













