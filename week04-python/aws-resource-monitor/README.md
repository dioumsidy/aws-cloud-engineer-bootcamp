\# AWS Cloud Resource Monitor



\## Overview



The AWS Cloud Resource Monitor is a Python automation project built as part of my AWS Cloud Engineer Bootcamp.



The project uses Python and Boto3 to communicate with AWS services, collect information about cloud resources, generate a resource report, save the report locally, and upload the report to Amazon S3.



\## Architecture



```text

&#x20;                   Python

&#x20;                      |

&#x20;                    Boto3

&#x20;                      |

&#x20;            +---------+---------+

&#x20;            |                   |

&#x20;            v                   v

&#x20;         Amazon EC2          Amazon S3

&#x20;            |                   |

&#x20;     Instance inventory      Bucket inventory

&#x20;            |                   |

&#x20;            +---------+---------+

&#x20;                      |

&#x20;                      v

&#x20;                Process Data

&#x20;                      |

&#x20;                      v

&#x20;               Generate Report

&#x20;                      |

&#x20;                      v

&#x20;            aws-resource-report.txt

&#x20;                      |

&#x20;                      v

&#x20;                 Amazon S3

&#x20;                      |

&#x20;                      v

&#x20;       reports/aws-resource-report.txt



Technologies Used

Python

Boto3

Amazon EC2

Amazon S3

AWS APIs

AWS CLI

Git

GitHub

Features



The automation:



Connects to AWS using Boto3

Retrieves EC2 instance information

Counts EC2 instances

Dynamically counts EC2 instance states

Retrieves S3 bucket information

Counts S3 buckets

Generates a timestamped AWS resource report

Saves the report locally

Uploads the generated report to Amazon S3

Handles AWS API errors using exception handling

Python Concepts Used



This project applies:



Variables

Strings

Dictionaries

Lists

Loops

Conditional statements

Functions

Return values

File handling

Exception handling

Python modules

datetime

Boto3

AWS API Operations

EC2



The project uses:



ec2.describe\_instances()



to retrieve EC2 instance information.



S3



The project uses:



s3.list\_buckets()



to retrieve S3 bucket information.



The generated report is uploaded using:



s3.upload\_file()

Example Report

=== AWS CLOUD RESOURCE REPORT ===



Time: YYYY-MM-DD HH:MM:SS



EC2

\---

Total Instances: 4

stopped: 4



S3

\--

Total Buckets: 3



Resource counts and states depend on the AWS environment at the time the script runs.



Security



AWS credentials are not stored inside the Python source code.



The project relies on the configured AWS authentication mechanism used by the AWS CLI/Boto3 credential provider chain.



Sensitive files such as .env, .pem, logs, and generated reports should not be committed to the repository.



IAM permissions should follow the principle of least privilege.



Troubleshooting



During development, several issues demonstrated important troubleshooting concepts.



Missing AWS Credentials



The AWS CLI initially could not locate credentials.



The authentication configuration was completed before attempting AWS API operations.



Boto3 Login Credential Dependency



Boto3 required an additional Botocore CRT dependency when using the AWS login credential provider.



Python NameError



After replacing separate running and stopped counters with a dynamic dictionary, an old reference to stopped\_count remained in the program.



The outdated code was removed so EC2 states could be dynamically counted using a dictionary.



Key Lessons



This project demonstrated that Boto3 automation follows a repeatable pattern:



Python

&#x20;  |

&#x20;  v

Boto3 Client

&#x20;  |

&#x20;  v

AWS API Request

&#x20;  |

&#x20;  v

AWS Response

&#x20;  |

&#x20;  v

Python Dictionary/List

&#x20;  |

&#x20;  v

Process Data

&#x20;  |

&#x20;  v

Take Action



Most of the automation logic uses standard Python concepts to process information returned by AWS APIs.



Project Outcome



The completed automation can inventory AWS EC2 and S3 resources, generate a timestamped report, save the report locally, and store a copy in Amazon S3.



This project demonstrates foundational cloud engineering skills in Python automation, AWS APIs, resource inventory, troubleshooting, security, and documentation.





One important thing: \*\*do not put your AWS account ID, login ARN, credentials, or other unnecessary account-specific information in the README.\*\*



\# 3. Move your script if necessary



Your `aws\_monitor.py` is currently directly under `week04-python`.



If you haven't moved it yet:



```powershell

Move-Item .\\aws\_monitor.py .\\aws-resource-monitor\\aws\_monitor.py

