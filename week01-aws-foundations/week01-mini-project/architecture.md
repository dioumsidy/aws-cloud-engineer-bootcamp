&#x20;                   INTERNET USERS

&#x20;                          │

&#x20;                     HTTP TCP/80

&#x20;                          │

&#x20;                          ▼

&#x20;                   Security Group

&#x20;                          │

&#x20;                          ▼

&#x20;                    Amazon EC2

&#x20;                          │

&#x20;                    Amazon Linux

&#x20;                          │

&#x20;                       Apache

&#x20;                          │

&#x20;              ┌───────────┴───────────┐

&#x20;              │                       │

&#x20;              ▼                       ▼

&#x20;          IAM Role                CloudWatch

&#x20;              │                     Metrics

&#x20;              │

&#x20;         Read-only S3

&#x20;              │

&#x20;              ▼

&#x20;         Amazon S3

&#x20;              │

&#x20;              ▼

&#x20;       project-info.txt





Administrator PC

&#x20;      │

&#x20;  SSH TCP/22

&#x20;      │

&#x20;      ▼

&#x20;Security Group

&#x20;      │

&#x20;      ▼

&#x20;     EC2

