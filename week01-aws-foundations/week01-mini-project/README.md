\# Week 1 Mini Project

\## Cloud Operations Web Server



\### Objective



Deploy and monitor a secure Linux web server in AWS using EC2, IAM, S3, and CloudWatch.



\### Technologies



\- Amazon EC2

\- Amazon S3

\- AWS IAM

\- Amazon CloudWatch

\- Amazon Linux

\- Apache

\- SSH

\- Git

\- GitHub



\## Troubleshooting Exercise



\### Incident



Users were unable to access the website.



\### Investigation



I tested the application locally using:



`curl http://localhost`



I checked Apache using:



`sudo systemctl status httpd`



I checked listening TCP ports using:



`sudo ss -lntp`



\### Root Cause



The Apache HTTP service was stopped.



\### Resolution



I started Apache using:



`sudo systemctl start httpd`



\### Verification



I verified:



\- Apache was active.

\- TCP port 80 was listening.

\- localhost returned the webpage.

\- The website was reachable externally.

