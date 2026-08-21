# EC2 Web Server Lab

## Objective

Deploy a Linux web server using Amazon EC2.

## Technologies

- AWS EC2
- Amazon Linux
- SSH
- Apache HTTP Server
- Security Groups
- Git
- GitHub

## Architecture

Windows PC
→ Internet
→ AWS Security Group
→ EC2
→ Linux
→ Apache
→ Website

## Network Rules

- SSH TCP/22 restricted to my IP
- HTTP TCP/80 allowed for the public demo website

## Linux Commands

`whoami`

`hostname`

`ip addr`

`ip route`

`sudo dnf install httpd -y`

`sudo systemctl start httpd`

`sudo systemctl enable httpd`

`sudo systemctl status httpd`

`curl http://localhost`

## Troubleshooting Exercise

I stopped Apache intentionally.

Symptom:
Website became unavailable.

Root cause:
Apache service was stopped.

Resolution:
Started Apache and verified the service and webpage.