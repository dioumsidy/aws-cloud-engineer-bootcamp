\# AWS Two-Tier VPC Architecture Lab



\## Project Overview



I designed and deployed a custom AWS VPC to demonstrate public and private subnet architecture, routing, Internet connectivity, network security, Linux administration, and systematic troubleshooting.



\## Architecture



\- VPC: `10.0.0.0/16`

\- Public Subnet: `10.0.1.0/24`

\- Private Subnet: `10.0.2.0/24`



\### Traffic Flow



Internet users reach the public EC2 instance through an Internet Gateway.



The private EC2 instance does not have a public IPv4 address.



Private resources can communicate with other resources inside the VPC through the local VPC route.



When outbound Internet access is required, the private subnet can route traffic through a NAT Gateway located in the public subnet.



\## AWS Services



\- Amazon VPC

\- Amazon EC2

\- Internet Gateway

\- NAT Gateway

\- Elastic IP

\- Route Tables

\- Security Groups

\- Network ACLs



\## Linux Technologies



\- Amazon Linux

\- Apache HTTP Server

\- systemd

\- Bash

\- Linux file permissions

\- Linux networking commands



\## Networking Concepts



\- IPv4 addressing

\- CIDR

\- Subnetting

\- Public and private subnets

\- Routing

\- Default routes

\- TCP/IP

\- DNS

\- NAT

\- Security Groups

\- Network ACLs



\## Routing



\### Public Route Table



\- `10.0.0.0/16 -> local`

\- `0.0.0.0/0 -> Internet Gateway`



\### Private Route Table



\- `10.0.0.0/16 -> local`

\- `0.0.0.0/0 -> NAT Gateway`



\## Security



The public web server allows HTTP traffic on TCP port 80.



SSH administrative access is restricted rather than being exposed to the entire Internet.



The private EC2 instance does not require a public IPv4 address.



Security Groups are used as stateful resource-level firewalls.



Network ACLs provide stateless subnet-level filtering.



\## Linux Troubleshooting Commands



I used the following commands to validate and troubleshoot the environment:



```bash

ip addr

ip route

sudo ss -lntp

curl http://localhost

getent hosts example.com

sudo systemctl status httpd

sudo journalctl -u httpd

ls -l

