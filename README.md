\# AWS Cloud Engineer Bootcamp



This repository documents my hands-on journey developing practical cloud engineering skills using AWS, Linux, networking, databases, Python, automation, infrastructure as code, containers, and CI/CD.



The goal of this bootcamp is to move beyond theory by building projects, troubleshooting real problems, documenting solutions, and developing the skills required to work with cloud infrastructure.



\---



\## Bootcamp Progress



| Week | Focus | Status |

|---|---|---|

| Week 1 | AWS Foundations | Completed |

| Week 2 | Linux, Networking, and AWS VPC | Completed |

| Week 3 | SQL and Amazon RDS | Completed |

| Week 4 | Python and AWS Automation | In Progress |

| Week 5 | Terraform and Ansible | Upcoming |

| Week 6 | Docker, Kubernetes, and Jenkins | Upcoming |

| Week 7 | Capstone Project | Upcoming |



\---



\# Skills Developed So Far



\## AWS



\- IAM

\- EC2

\- S3

\- CloudWatch

\- VPC

\- Security Groups

\- Network ACLs

\- Internet Gateway

\- NAT Gateway

\- Amazon RDS

\- IAM roles

\- AWS CLI

\- Public and private subnets



\## Linux



\- Linux file system navigation

\- File and directory management

\- File permissions

\- `chmod`

\- Users and groups

\- `sudo`

\- Process monitoring

\- Service management with `systemctl`

\- Linux networking commands

\- Log inspection

\- Apache web server administration



\## Networking



\- TCP/IP

\- IPv4

\- CIDR

\- Subnetting

\- Public and private IP addresses

\- DNS

\- DHCP

\- ARP

\- TCP and UDP

\- Ports

\- Routing

\- Default gateways

\- Security Groups

\- Network ACLs

\- Internet Gateway

\- NAT Gateway

\- Public and private subnet architecture

\- VPC routing

\- OSI model

\- Network troubleshooting



\## SQL and Databases



\- SQL

\- MariaDB

\- Relational databases

\- Tables

\- Rows and columns

\- Primary keys

\- Foreign keys

\- SELECT

\- INSERT

\- UPDATE

\- DELETE

\- WHERE

\- ORDER BY

\- GROUP BY

\- JOIN

\- LEFT JOIN

\- Aggregate functions

\- Database users

\- GRANT

\- Least privilege

\- Amazon RDS

\- Private database architecture

\- TLS-secured database connections



\## Python



\- Variables

\- Strings, integers, floats, and Booleans

\- User input

\- Conditional statements

\- Boolean logic

\- Lists

\- Dictionaries

\- Loops

\- Functions

\- Parameters and arguments

\- Return values

\- File handling

\- Exception handling

\- Python modules

\- `datetime`

\- `platform`

\- `psutil`

\- System monitoring

\- Log generation

\- Python troubleshooting



\## Git and GitHub



\- Git repositories

\- Staging

\- Commits

\- Branch basics

\- GitHub remote repositories

\- `git status`

\- `git diff`

\- `git add`

\- `git commit`

\- `git push`

\- `git log`

\- `.gitignore`

\- Project documentation with Markdown



\---



\# Week 1 - AWS Foundations



Week 1 introduced the core AWS services and cloud concepts used throughout the bootcamp.



\## Topics



\- Cloud computing fundamentals

\- AWS Regions and Availability Zones

\- Shared Responsibility Model

\- IAM users, groups, policies, and roles

\- Least privilege

\- EC2

\- Amazon Machine Images

\- Instance types

\- EBS

\- Security Groups

\- Public and private IP addresses

\- SSH

\- Apache web server

\- S3

\- Object storage

\- S3 permissions

\- IAM roles for EC2

\- CloudWatch metrics

\- CloudWatch alarms

\- Basic monitoring and troubleshooting



\## Project - Cloud Operations Web Server



Built and operated an EC2-based Linux web server.



Architecture:



```text

Internet

&#x20;  |

&#x20;  | HTTP :80

&#x20;  v

Security Group

&#x20;  |

&#x20;  v

EC2 - Amazon Linux

&#x20;  |

&#x20;  +---- Apache Web Server

&#x20;  |

&#x20;  +---- IAM Role

&#x20;           |

&#x20;           v

&#x20;           S3



EC2 ----> CloudWatch

```



The project included:



\- EC2 provisioning

\- Linux administration

\- Apache installation

\- Security Group configuration

\- S3 access through an IAM role

\- CloudWatch monitoring

\- Troubleshooting simulated failures



\---



\# Week 2 - Linux, Networking, and AWS VPC



Week 2 focused on understanding the operating system and networking layers underneath cloud infrastructure.



\## Linux



Practiced:



```text

pwd

ls

cd

mkdir

touch

cat

head

tail

less

grep

cp

mv

rm

chmod

chown

ps

top

systemctl

journalctl

```



Topics included:



\- Linux filesystem

\- Users and groups

\- File permissions

\- Processes

\- Services

\- Logs

\- Apache troubleshooting

\- Linux networking



\## Networking



Studied:



\- IP addressing

\- CIDR

\- Subnets

\- Routing

\- Default gateways

\- TCP

\- UDP

\- Ports

\- DNS

\- DHCP

\- ARP

\- OSI model

\- Public vs private networking



\## Project - AWS VPC Architecture



Built a multi-subnet AWS network.



```text

&#x20;                    Internet

&#x20;                       |

&#x20;                       v

&#x20;               Internet Gateway

&#x20;                       |

&#x20;               Public Route Table

&#x20;                       |

&#x20;                       v

&#x20;               Public Subnet

&#x20;                10.0.1.0/24

&#x20;                       |

&#x20;                      EC2

&#x20;                       |

&#x20;           +-----------+-----------+

&#x20;           |                       |

&#x20;           v                       v

&#x20;     Private Subnet          Private Subnet

&#x20;      10.0.2.0/24             10.0.3.0/24

&#x20;           |

&#x20;           v

&#x20;      Private Resources

```



The lab included:



\- Custom VPC

\- Public subnet

\- Private subnets

\- Route tables

\- Internet Gateway

\- NAT Gateway

\- Security Groups

\- Network ACLs

\- EC2 networking

\- Private-resource communication

\- Network troubleshooting



One of the main lessons was:



> A subnet is not public simply because it is called a public subnet. Its routing determines whether it has a direct path to an Internet Gateway.



\---



\# Week 3 - SQL and Amazon RDS



Week 3 introduced relational databases and database infrastructure in AWS.



\## SQL



Practiced:



```sql

SELECT

INSERT

UPDATE

DELETE

WHERE

ORDER BY

GROUP BY

JOIN

LEFT JOIN

```



Created relational tables using:



\- Primary keys

\- Foreign keys

\- Data types

\- Relationships

\- Constraints



Practiced database security using:



\- Database users

\- GRANT

\- Least privilege



\## Project - Private Amazon RDS Database



Built an architecture where an EC2 application server communicates with a private RDS MariaDB database.



```text

Internet

&#x20;  |

&#x20;  v

Internet Gateway

&#x20;  |

&#x20;  v

Public Subnet

&#x20;  |

&#x20;  v

EC2 Application Server

&#x20;  |

&#x20;  | TCP 3306 + TLS

&#x20;  v

RDS Security Group

&#x20;  |

&#x20;  v

Private RDS MariaDB

```



Security architecture:



```text

Internet

&#x20;  |

&#x20;  X

&#x20;  |

Direct RDS Access Blocked



EC2 Security Group

&#x20;  |

&#x20;  | TCP 3306

&#x20;  v

RDS Security Group

```



The RDS Security Group allows database traffic from the application Security Group instead of exposing port 3306 to the internet.



\## Troubleshooting



During the project, database connectivity was diagnosed in layers.



A TCP connectivity test showed port 3306 was reachable.



The database then returned a secure-transport error because TLS was required.



The successful connection used:



```bash

mariadb \\

&#x20; -h RDS-ENDPOINT \\

&#x20; -P 3306 \\

&#x20; -u USERNAME \\

&#x20; -p \\

&#x20; --ssl

```



This demonstrated an important troubleshooting principle:



```text

Network failure

&#x20;     !=

Authentication failure

&#x20;     !=

Authorization failure

&#x20;     !=

TLS failure

```



\---



\# Week 4 - Python for Cloud Engineering



Week 4 focuses on using Python for cloud engineering and automation.



\## Python Fundamentals - Completed



Topics completed:



\- Variables

\- Data types

\- User input

\- Conditional statements

\- Boolean logic

\- Lists

\- Dictionaries

\- Loops

\- Functions

\- Parameters and arguments

\- Return values

\- File handling

\- Exception handling

\- Modules

\- Date and time

\- Third-party Python packages

\- System information

\- System monitoring

\- Troubleshooting Python errors



\## Project - System Health Monitor



Built a Python program that collects real system metrics.



The program monitors:



\- CPU utilization

\- Memory utilization

\- Disk utilization

\- Hostname

\- Operating system

\- OS release



Architecture:



```text

Operating System

&#x20;      |

&#x20;      v

&#x20;Python + psutil

&#x20;      |

&#x20;      v

&#x20;Collect Metrics

&#x20;      |

&#x20;      +---- CPU

&#x20;      +---- Memory

&#x20;      +---- Disk

&#x20;      |

&#x20;      v

&#x20; check\_usage()

&#x20;      |

&#x20;      v

NORMAL / WARNING / CRITICAL

&#x20;      |

&#x20;      v

Overall System Status

&#x20;      |

&#x20;      +----------+

&#x20;      |          |

&#x20;      v          v

&#x20;   Terminal    Log File

```



Resource thresholds:



```text

Below 60%    -> NORMAL

60% - 79%    -> WARNING

80%+         -> CRITICAL

```



Example:



```text

=== SYSTEM HEALTH REPORT ===

Hostname: SidyLaptop

Operating System: Windows



CPU Usage: 5.3% - NORMAL

Memory Usage: 85.1% - CRITICAL

Disk Usage: 48.4% - NORMAL



Overall System Status: CRITICAL

```



The project demonstrates the automation workflow:



> Collect -> Analyze -> Decide -> Report -> Save



\## Week 4 Next Step



Python fundamentals are complete.



The next phase applies Python directly to AWS using the AWS SDK for Python (`boto3`).



Planned work:



\- Connect Python to AWS

\- Read AWS resource information

\- Work with EC2 programmatically

\- Work with S3 programmatically

\- Build a small AWS automation project



\---



\# Troubleshooting Methodology



A major focus of this bootcamp is learning how to troubleshoot infrastructure instead of immediately changing configurations.



My general troubleshooting process is:



```text

1\. Identify the symptom

&#x20;       |

&#x20;       v

2\. Determine the failing layer

&#x20;       |

&#x20;       v

3\. Collect evidence

&#x20;       |

&#x20;       v

4\. Test one hypothesis

&#x20;       |

&#x20;       v

5\. Make the smallest necessary change

&#x20;       |

&#x20;       v

6\. Retest

&#x20;       |

&#x20;       v

7\. Document the solution

```



Examples encountered during the bootcamp include:



\- SSH authentication failures

\- Security Group misconfiguration

\- Apache permission errors

\- DNS failures

\- VPC routing problems

\- Database connectivity failures

\- TLS requirements

\- SQL syntax errors

\- Python recursion errors

\- Python function/variable name collisions

\- Incorrect file paths



\---



\# Security Principles



Security is incorporated throughout the projects.



Practices include:



\- Least privilege

\- IAM roles instead of hard-coded AWS credentials

\- Private database architecture

\- Security Group references

\- TLS-secured database connections

\- S3 Block Public Access

\- Restricted SSH access

\- Avoiding public database exposure

\- Avoiding secrets in GitHub

\- Using `.gitignore` for generated or sensitive files



Never commit:



```text

AWS access keys

AWS secret access keys

Passwords

.pem private keys

.env files containing credentials

```



\---



\# Repository Structure



```text

aws-cloud-engineer-bootcamp/

|

+-- week01-aws-foundations/

|   +-- EC2, S3, IAM, CloudWatch labs

|

+-- week02-linux-networking/

|   +-- Linux labs

|   +-- Networking labs

|   +-- VPC project

|

+-- week03-sql/

|   +-- SQL labs

|   +-- RDS project

|

+-- week04-python/

|   +-- README.md

|   +-- system\_monitor.py

|   +-- Python learning exercises

|

+-- README.md

```



\---



\# Upcoming



\## Week 4 - AWS Automation



\- boto3

\- EC2 automation

\- S3 automation

\- AWS automation project



\## Week 5 - Infrastructure as Code and Automation



\- Terraform

\- Ansible



\## Week 6 - Containers and CI/CD



\- Docker

\- Kubernetes

\- Jenkins



\## Week 7 - Capstone



The final project will combine multiple technologies from the bootcamp into a documented cloud engineering solution.



\---



\# Engineering Goal



The purpose of this repository is to demonstrate continuous development toward cloud engineering through hands-on practice.



The focus is not only on knowing AWS services, but on understanding how the different layers work together:



```text

Application

&#x20;    |

Programming / Automation

&#x20;    |

Database

&#x20;    |

Operating System

&#x20;    |

Networking

&#x20;    |

Cloud Infrastructure

&#x20;    |

Security

&#x20;    |

Monitoring

```



Each week builds on the previous one to develop the troubleshooting, automation, networking, Linux, security, and AWS skills required for cloud engineering.

