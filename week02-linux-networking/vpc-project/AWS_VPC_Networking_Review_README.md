# AWS VPC Networking Review

This README documents the AWS networking concepts reviewed during the bootcamp and explains how the pieces work together in a practical VPC architecture.

## Topics Covered

- AWS VPC architecture
- Public and private subnets
- Routing and route tables
- Internet Gateway
- NAT Gateway
- Security Groups
- Network ACLs
- EC2-to-RDS communication
- Public web traffic flow
- Private outbound Internet traffic
- Troubleshooting methodology

---

# 1. AWS VPC Architecture

An **Amazon VPC (Virtual Private Cloud)** is a logically isolated network in AWS.

Example:

```text
VPC: 10.0.0.0/16
```

The VPC acts as the main network boundary that contains resources such as:

- EC2 instances
- RDS databases
- Subnets
- Route tables
- Security Groups
- Network ACLs
- Internet Gateways
- NAT Gateways

A VPC by itself does **not** automatically provide Internet access.

```text
AWS Region
   |
   v
+--------------------------------------+
| VPC 10.0.0.0/16                      |
|                                      |
| Public Subnets                       |
| Private Subnets                      |
| Route Tables                         |
| Security Groups                      |
| Network ACLs                         |
| EC2                                  |
| RDS                                  |
+--------------------------------------+
```

---

# 2. Public and Private Subnets

A VPC is divided into smaller IP networks called **subnets**.

Example design:

```text
VPC 10.0.0.0/16

├── Public Subnet
│   10.0.1.0/24
│
├── Private Subnet
│   10.0.2.0/24
│
└── Private Subnet
    10.0.3.0/24
```

A subnet is not public simply because it is named `public`.

Its routing and resource configuration determine whether it has a public Internet path.

## Public Subnet

A public subnet normally has a default route to an Internet Gateway:

```text
Destination      Target
10.0.0.0/16      local
0.0.0.0/0        Internet Gateway
```

Typical public-subnet resources include:

- Public EC2 web servers
- Internet-facing load balancers
- Bastion hosts
- NAT Gateways

For an EC2 instance to be directly reachable over IPv4 from the Internet, it normally also needs a public IPv4 address and appropriate security rules.

## Private Subnet

A private subnet does not have a direct default route to an Internet Gateway.

Typical private resources include:

- Databases
- Internal application servers
- Backend services
- Private EC2 instances

Example:

```text
Private Subnet
10.0.2.0/24

    |
    +--> Private EC2
    |
    +--> RDS
```

---

# 3. Internet Gateway

An **Internet Gateway (IGW)** provides a VPC with a path to the Internet.

```text
Internet
   |
   v
Internet Gateway
   |
   v
VPC
```

Attaching an Internet Gateway to a VPC does not automatically make all resources public.

A public EC2 instance commonly needs:

1. A subnet associated with a route table containing `0.0.0.0/0 -> IGW`
2. A public IPv4 address
3. Security Group rules that allow the required traffic
4. Applicable NACL rules
5. A working service listening on the expected port

Example path:

```text
Internet
   |
   v
Internet Gateway
   |
   v
Public Route Table
0.0.0.0/0 -> IGW
   |
   v
Public Subnet
   |
   v
EC2
```

---

# 4. Routing and Route Tables

A **route table** tells AWS where network traffic should go.

A route contains:

```text
Destination -> Target
```

Example public route table:

```text
Destination      Target
10.0.0.0/16      local
0.0.0.0/0        igw-xxxxxxxx
```

## Local Route

Every VPC route table contains a local route for communication inside the VPC.

Example:

```text
10.0.0.0/16 -> local
```

This allows resources in different subnets of the same VPC to communicate privately, assuming the security controls permit the traffic.

Example:

```text
EC2
10.0.1.x
   |
   | VPC local routing
   v
RDS
10.0.2.x
```

An Internet Gateway or NAT Gateway is not needed for this same-VPC private path.

## Default Route

The IPv4 route:

```text
0.0.0.0/0
```

means:

> Match any IPv4 destination that does not have a more specific route.

For a public subnet:

```text
0.0.0.0/0 -> Internet Gateway
```

For a private subnet that requires outbound IPv4 Internet access:

```text
0.0.0.0/0 -> NAT Gateway
```

---

# 5. Route Table Associations

Creating a route table is not enough.

The subnet must be associated with the correct route table.

```text
Public Subnet
     |
     v
Public Route Table
     |
     +--> 0.0.0.0/0 -> Internet Gateway
```

```text
Private Subnet
     |
     v
Private Route Table
     |
     +--> 0.0.0.0/0 -> NAT Gateway
```

During troubleshooting, always verify:

```text
Subnet
   |
   v
Associated Route Table
   |
   v
Routes
```

A common configuration mistake is creating the correct route table but associating the subnet with a different one.

---

# 6. Security Groups

A **Security Group** is a stateful firewall associated with an AWS resource or its network interface.

Security Groups contain allow rules.

Example rules for a public EC2 web server:

```text
Inbound

SSH
TCP 22
Source: Administrator IP

HTTP
TCP 80
Source: 0.0.0.0/0
```

Traffic examples:

```text
Administrator
    |
    | TCP 22
    v
EC2
```

```text
Internet Users
    |
    | TCP 80
    v
EC2 Apache
```

## RDS Security Group

For a private MariaDB RDS database, a stronger rule is:

```text
Type: MariaDB/MySQL
Protocol: TCP
Port: 3306
Source: EC2 application Security Group
```

Instead of:

```text
TCP 3306
Source: 0.0.0.0/0
```

Architecture:

```text
EC2 Application Security Group
          |
          | TCP 3306
          v
RDS Database Security Group
          |
          v
RDS MariaDB
```

This follows the principle of least privilege.

---

# 7. Security Groups Are Stateful

Security Groups are **stateful**.

If a connection is allowed, the return traffic for that connection is automatically recognized.

Example:

```text
EC2:50000 ------> RDS:3306
EC2:50000 <------ RDS:3306
```

A separate inbound rule on EC2 is not needed just for the return packet of the established connection.

This is different from Network ACL behavior.

---

# 8. Network ACLs

A **Network ACL (NACL)** is a stateless firewall associated with a subnet.

| Feature | Security Group | Network ACL |
|---|---|---|
| Scope | Resource / ENI | Subnet |
| Stateful | Yes | No |
| Allow rules | Yes | Yes |
| Deny rules | No explicit deny rules | Yes |
| Evaluation | All applicable rules | Lowest numbered matching rule first |
| Return traffic | Automatically recognized | Must be allowed |

Example NACL rules:

```text
Rule 100
ALLOW TCP 80
Source: 0.0.0.0/0

Rule 110
ALLOW TCP 443
Source: 0.0.0.0/0

Rule *
DENY everything else
```

The first matching numbered rule determines the result.

---

# 9. Ephemeral Ports and NACLs

A TCP client normally uses a temporary source port.

Example EC2-to-RDS connection:

```text
EC2 source port: 50000
RDS destination port: 3306
```

Request:

```text
50000 ---> 3306
```

Response:

```text
3306 ---> 50000
```

Because NACLs are stateless, the applicable rules need to allow both the request and the return traffic.

This is one reason overly restrictive custom NACLs can cause confusing connectivity problems.

---

# 10. NAT Gateway

A **NAT Gateway** allows resources in a private subnet to initiate outbound IPv4 connections to the Internet without making those private resources directly reachable from the Internet.

Example use case:

```text
Private EC2
    |
    | sudo dnf update
    v
Internet
```

Traffic path:

```text
Private EC2
    |
    v
Private Route Table
0.0.0.0/0 -> NAT Gateway
    |
    v
NAT Gateway
Public Subnet
    |
    v
Internet Gateway
    |
    v
Internet
```

The important direction is:

```text
Private Resource ---> Internet
```

A NAT Gateway does not turn a private EC2 instance into a directly reachable public server.

---

# 11. NAT Gateway Placement

A NAT Gateway is placed in a **public subnet**.

The NAT Gateway itself needs a route through the Internet Gateway.

```text
PUBLIC SUBNET
10.0.1.0/24

   NAT Gateway
       |
       v
Internet Gateway
       |
       v
Internet


PRIVATE SUBNET
10.0.2.0/24

Private EC2
    |
    v
Private Route Table
0.0.0.0/0 -> NAT Gateway
```

---

# 12. Public vs Private Subnets

| Public Subnet | Private Subnet |
|---|---|
| Direct default route to IGW | No direct default route to IGW |
| Can host publicly reachable resources | Used for internal resources |
| Public IPv4 may be assigned | Usually no public IPv4 |
| Example: web server | Example: database |
| Direct Internet path possible | NAT can provide outbound IPv4 |

Easy memory rule:

```text
Public Subnet:
0.0.0.0/0 -> IGW
```

```text
Private Subnet with outbound Internet:
0.0.0.0/0 -> NAT Gateway
```

---

# 13. Bootcamp VPC Architecture

The bootcamp architecture follows this general design:

```text
                           INTERNET
                              |
                              v
                       Internet Gateway
                              |
             +----------------+----------------+
             |                                 |
             |        VPC 10.0.0.0/16          |
             |                                 |
      PUBLIC SUBNET                    PRIVATE SUBNET
      10.0.1.0/24                     10.0.2.0/24
             |                                 |
        +----+----+                       Private
        |   EC2   |                       workload
        | Apache  |
        +----+----+
             |
             | TCP 3306 + TLS
             v
       PRIVATE DB TIER
       10.0.2.0/24
       10.0.3.0/24
             |
             v
       +-----------+
       |    RDS    |
       |  MariaDB  |
       +-----------+
```

The RDS DB subnet group uses private subnets in different Availability Zones.

---

# 14. Public Website Traffic Flow

When a user visits a public EC2 web server:

```text
Browser
   |
   | HTTP TCP 80
   v
Internet
   |
   v
Internet Gateway
   |
   v
Route Table
   |
   v
Public Subnet / NACL
   |
   v
EC2 Security Group
   |
   v
EC2
   |
   v
Linux
   |
   v
Apache TCP 80
```

Each layer must work.

If:

```bash
curl http://localhost
```

works on EC2 but the website is unreachable from the Internet, the application may already be healthy.

Investigate the external path:

```text
Security Group
Network ACL
Route Table
Internet Gateway
Public IP
DNS
```

---

# 15. EC2-to-RDS Traffic Flow

The private database project uses this path:

```text
EC2
Public Subnet
   |
   | TCP 3306
   v
EC2 Security Group
   |
   v
VPC Local Route
10.0.0.0/16 -> local
   |
   v
Private DB Subnet
   |
   v
RDS Security Group
Allow TCP 3306
from application SG
   |
   v
MariaDB
   |
   v
TLS
   |
   v
Database Authentication
   |
   v
Database Authorization
```

For this same-VPC private connection:

```text
Internet Gateway: NOT required
NAT Gateway:      NOT required
```

---

# 16. Private EC2-to-Internet Traffic Flow

A private EC2 instance that needs software updates can use:

```text
Private EC2
    |
    v
Private Route Table
0.0.0.0/0 -> NAT Gateway
    |
    v
NAT Gateway
Public Subnet
    |
    v
Public Route Table
0.0.0.0/0 -> Internet Gateway
    |
    v
Internet Gateway
    |
    v
Internet
```

---

# 17. Routing vs Security Groups

These components solve different problems.

## Routing asks:

> Where should the packet go?

Example:

```text
0.0.0.0/0 -> Internet Gateway
```

## Security Group asks:

> Is this connection allowed?

Example:

```text
TCP 80
Source: 0.0.0.0/0
```

You need both valid routing and valid security rules.

A correct route with a blocked Security Group still fails.

A permissive Security Group with no valid route also fails.

---

# 18. Troubleshooting Public Web Access

Recommended troubleshooting order:

```text
Application
    |
    v
Linux Service
    |
    v
Listening Port
    |
    v
Security Group
    |
    v
Network ACL
    |
    v
Route Table
    |
    v
Internet Gateway
    |
    v
Public IP / DNS
```

Useful Linux commands:

```bash
sudo systemctl status httpd
curl http://localhost
sudo ss -lntp
ip addr
ip route
getent hosts example.com
```

Do not randomly restart or reconfigure infrastructure before collecting evidence.

---

# 19. Troubleshooting EC2-to-RDS

Use the following mental path:

```text
RDS Endpoint
    |
    v
DNS
    |
    v
TCP 3306
    |
    v
Security Path
    |
    v
MariaDB
    |
    v
TLS
    |
    v
Authentication
    |
    v
Authorization
```

## If TCP 3306 fails

Investigate:

- DNS
- RDS endpoint and port
- EC2 and RDS VPC placement
- Security Groups
- NACLs
- Routing

## If TCP 3306 succeeds but MariaDB says `Access denied`

Investigate:

- Username
- Password
- MariaDB user/host definition
- Database grants

Do not change the Security Group just because login failed when TCP connectivity is already proven.

## If MariaDB says insecure transport is prohibited

Investigate TLS.

Example secure connection:

```bash
mariadb   -h RDS-ENDPOINT   -P 3306   -u DATABASE-USER   -p   --ssl
```

---

# 20. Recommended VPC Build Order

A practical build sequence is:

```text
1. Create VPC
       |
       v
2. Create public and private subnets
       |
       v
3. Create and attach Internet Gateway
       |
       v
4. Create public route table
       |
       v
5. Add 0.0.0.0/0 -> IGW
       |
       v
6. Associate public subnet
       |
       v
7. Configure Security Groups
       |
       v
8. Launch public EC2
       |
       v
9. Create NAT Gateway if private outbound Internet is needed
       |
       v
10. Create private route table
       |
       v
11. Add 0.0.0.0/0 -> NAT Gateway
       |
       v
12. Associate private subnet
       |
       v
13. Review NACLs
       |
       v
14. Launch private resources
       |
       v
15. Test
       |
       v
16. Monitor and document
```

For RDS:

```text
Private Subnet AZ-1
         +
Private Subnet AZ-2
         |
         v
DB Subnet Group
         |
         v
Amazon RDS
         |
         v
DB Security Group
TCP 3306 from Application Security Group
```

---

# 21. Key Engineering Takeaways

## VPC

The main private network boundary.

## Subnet

A smaller IP network inside the VPC.

## Route Table

Determines where traffic goes.

## Internet Gateway

Provides a path between public VPC resources and the Internet.

## NAT Gateway

Allows private resources to initiate outbound IPv4 Internet connections.

## Security Group

Stateful resource-level firewall.

## Network ACL

Stateless subnet-level firewall.

---

# 22. Final Mental Model

## Public application traffic

```text
Internet
   |
   v
Internet Gateway
   |
   v
Route Table
   |
   v
Subnet / NACL
   |
   v
Security Group
   |
   v
EC2
   |
   v
Linux
   |
   v
Application
```

## Private database traffic

```text
EC2
   |
   v
Security Controls
   |
   v
VPC Local Routing
   |
   v
RDS Security Group
   |
   v
TCP 3306
   |
   v
TLS
   |
   v
MariaDB Authentication
   |
   v
SQL Authorization
```

## Private outbound Internet traffic

```text
Private Resource
   |
   v
Private Route Table
   |
   v
NAT Gateway
   |
   v
Public Subnet
   |
   v
Internet Gateway
   |
   v
Internet
```

---

# Engineering Principle

> Follow the packet path, collect evidence, identify the failing layer, make one controlled change, verify the result, and document what happened.

This same troubleshooting method applies to AWS networking, Linux, applications, databases, and future automation work.
