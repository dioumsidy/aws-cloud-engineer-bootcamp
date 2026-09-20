\# Week 4 — Python for Cloud Engineering



\## Overview



Week 4 of my AWS Cloud Engineer Bootcamp focuses on learning Python for cloud engineering, system administration, troubleshooting, and automation.



The goal of this week is not to become a full-time Python developer. The goal is to build enough Python knowledge to understand scripts, automate repetitive tasks, collect system information, make decisions from system data, and eventually interact with AWS services programmatically.



During this week, I progressed from basic Python syntax to building a working system health monitoring script that collects real metrics from my computer.



\---



\## Learning Objectives



By the end of the Python fundamentals section, I learned how to:



\- Write and execute Python scripts

\- Work with variables and data types

\- Accept user input

\- Make decisions with conditional statements

\- Use Boolean logic

\- Store multiple values in lists

\- Organize structured data with dictionaries

\- Process multiple objects with loops

\- Create reusable functions

\- Use parameters, arguments, and return values

\- Read, write, and append files

\- Handle expected errors with exceptions

\- Import built-in and third-party Python modules

\- Generate timestamps

\- Collect real system information

\- Analyze CPU, memory, and disk utilization

\- Generate system health reports

\- Save monitoring results to log files

\- Troubleshoot common Python errors



\---



\# 1. Python Fundamentals



\## Variables and Data Types



I practiced storing information in variables.



Example:



```python

server\_name = "cloud-web-server"

service = "Apache"

port = 80

cpu\_usage = 42.5

monitoring\_enabled = True

```



The main data types used were:



| Type | Example | Purpose |

|---|---|---|

| `str` | `"Apache"` | Text |

| `int` | `80` | Whole numbers |

| `float` | `42.5` | Decimal numbers |

| `bool` | `True` | True/False values |



I also practiced using f-strings to create readable output:



```python

print(f"Server: {server\_name}")

print(f"Port: {port}")

```



\---



\# 2. User Input and Type Conversion



Python's `input()` function allows a program to receive information from a user.



Example:



```python

server = input("Enter server name: ")

port = int(input("Enter port: "))

cpu\_usage = float(input("Enter CPU usage: "))

```



I learned that `input()` normally returns a string, so values may need to be converted with functions such as:



```python

int()

float()

```



\---



\# 3. Conditional Logic



I used `if`, `elif`, and `else` to allow programs to make decisions.



Example:



```python

if cpu\_usage >= 80:

&#x20;   print("CRITICAL")

elif cpu\_usage >= 60:

&#x20;   print("WARNING")

else:

&#x20;   print("NORMAL")

```



This introduced an important monitoring concept:



```text

CPU >= 80%       → CRITICAL

CPU >= 60%       → WARNING

CPU below 60%    → NORMAL

```



\---



\# 4. Boolean Logic



I practiced:



\- `and`

\- `or`

\- `not`



Example:



```python

if service\_running and port == 80 and cpu\_usage < 80:

&#x20;   print("Server is healthy")

```



Boolean logic is useful when multiple conditions must be evaluated before an automated decision is made.



\---



\# 5. Lists



Lists allow multiple related values to be stored together.



Example:



```python

servers = \[

&#x20;   "web-server-01",

&#x20;   "web-server-02",

&#x20;   "database-server",

&#x20;   "monitoring-server"

]

```



I practiced:



```python

servers\[0]

len(servers)

servers.append("backup-server")

```



I also learned that Python list indexes begin at `0`.



\---



\# 6. Loops



A `for` loop allows Python to perform the same operation on multiple objects.



Example:



```python

for server in servers:

&#x20;   print(server)

```



I combined loops with conditional statements:



```python

for server in servers:

&#x20;   if server == "database-server":

&#x20;       print(f"{server}: DATABASE SERVER")

&#x20;   else:

&#x20;       print(f"{server}: GENERAL SERVER")

```



This introduced an important automation pattern:



```text

List

&#x20; ↓

Loop

&#x20; ↓

Condition

&#x20; ↓

Action

```



\---



\# 7. Dictionaries



Dictionaries store information using key-value pairs.



Example:



```python

server = {

&#x20;   "name": "cloud-web-server",

&#x20;   "state": "running",

&#x20;   "private\_ip": "10.0.1.25",

&#x20;   "port": 80,

&#x20;   "cpu": 42.5

}

```



Values can be accessed using their keys:



```python

print(server\["name"])

print(server\["cpu"])

```



This is useful for representing cloud resources because one server can have many properties.



\---



\# 8. Lists of Dictionaries



I combined lists and dictionaries to represent multiple servers.



```python

servers = \[

&#x20;   {"name": "web-server-01", "state": "running", "cpu": 25},

&#x20;   {"name": "web-server-02", "state": "running", "cpu": 65},

&#x20;   {"name": "database-server", "state": "running", "cpu": 88},

&#x20;   {"name": "backup-server", "state": "stopped", "cpu": 0}

]

```



I then processed the servers using a loop:



```python

for server in servers:

&#x20;   print(server\["name"])

```



This structure is important because cloud APIs commonly return collections of structured resource information.



\---



\# 9. Functions



Functions allow reusable blocks of code to be created.



Example:



```python

def check\_server(name, state, cpu):

&#x20;   print(f"Checking: {name}")



&#x20;   if state == "stopped":

&#x20;       print("ALERT: Server is stopped!")

&#x20;   elif cpu >= 80:

&#x20;       print("Status: CRITICAL")

&#x20;   elif cpu >= 60:

&#x20;       print("Status: WARNING")

&#x20;   else:

&#x20;       print("Status: NORMAL")

```



I learned the difference between a parameter and an argument.



```python

def show\_service(service):

```



`service` is the \*\*parameter\*\*.



```python

show\_service("Apache")

```



`"Apache"` is the \*\*argument\*\*.



\---



\# 10. `return` vs `print()`



One important concept was understanding the difference between displaying a value and returning a value.



```python

print("NORMAL")

```



displays information.



```python

return "NORMAL"

```



sends information back to the part of the program that called the function.



Example:



```python

def check\_cpu(cpu):

&#x20;   if cpu >= 80:

&#x20;       return "CRITICAL"

&#x20;   elif cpu >= 60:

&#x20;       return "WARNING"

&#x20;   else:

&#x20;       return "NORMAL"



status = check\_cpu(65)

print(status)

```



\---



\# 11. File Handling



I practiced creating, reading, and updating files.



\## Write



```python

with open("cpu-report.txt", "w") as file:

&#x20;   file.write("CPU report")

```



\## Read



```python

with open("cpu-report.txt", "r") as file:

&#x20;   report = file.read()

```



\## Append



```python

with open("cpu-report.txt", "a") as file:

&#x20;   file.write("New monitoring result\\n")

```



I learned:



```text

r → Read

w → Write/replace

a → Append

```



Append mode is especially useful for log files because previous information is preserved.



\---



\# 12. Exception Handling



I practiced handling expected errors with `try` and `except`.



Example:



```python

try:

&#x20;   cpu\_usage = float(input("Enter CPU usage: "))

except ValueError:

&#x20;   print("ERROR: CPU usage must be a number.")

else:

&#x20;   print(f"CPU usage is: {cpu\_usage}%")

finally:

&#x20;   print("CPU check completed.")

```



I also handled missing files:



```python

try:

&#x20;   with open("cpu-report.txt", "r") as file:

&#x20;       report = file.read()

except FileNotFoundError:

&#x20;   print("ERROR: CPU report was not found.")

```



This prevents expected problems from immediately terminating a script.



\---



\# 13. Python Modules



Modules allow existing Python functionality to be reused instead of building everything from scratch.



Example:



```python

import os



current\_directory = os.getcwd()

print(current\_directory)

```



I learned to think of a module as a toolbox containing useful functions.



\---



\# 14. Date and Time



I used Python's `datetime` module to timestamp monitoring information.



```python

from datetime import datetime



current\_time = datetime.now()

formatted\_time = current\_time.strftime("%Y-%m-%d %H:%M:%S")

```



Example output:



```text

2026-09-20 14:57:07

```



Timestamps are important when working with monitoring systems and logs because engineers need to know when an event occurred.



\---



\# 15. Collecting Real System Information



Instead of using only hard-coded values, I began collecting real information from the operating system.



Using the `platform` module:



```python

import platform



hostname = platform.node()

operating\_system = platform.system()

os\_release = platform.release()

```



This provides information about the computer running the script.



\---



\# 16. System Monitoring with `psutil`



I installed and used the third-party `psutil` Python package.



Installation:



```powershell

python -m pip install psutil

```



CPU utilization:



```python

cpu\_usage = psutil.cpu\_percent(interval=1)

```



Memory utilization:



```python

memory\_usage = psutil.virtual\_memory().percent

```



Disk utilization on Windows:



```python

disk\_usage = psutil.disk\_usage("C:\\\\").percent

```



This moved the project from simulated monitoring to collecting real system metrics.



\---



\# 17. System Health Logic



I created a reusable function for evaluating resource utilization:



```python

def check\_usage(usage):

&#x20;   if usage >= 80:

&#x20;       return "CRITICAL"

&#x20;   elif usage >= 60:

&#x20;       return "WARNING"

&#x20;   else:

&#x20;       return "NORMAL"

```



The same function can evaluate multiple resources:



```python

cpu\_status = check\_usage(cpu\_usage)

memory\_status = check\_usage(memory\_usage)

disk\_status = check\_usage(disk\_usage)

```



This demonstrated why functions are useful: one piece of logic can be reused instead of rewriting the same conditions multiple times.



\---



\# 18. Overall System Health



The program also determines the overall health of the system.



```python

if (

&#x20;   cpu\_status == "CRITICAL"

&#x20;   or memory\_status == "CRITICAL"

&#x20;   or disk\_status == "CRITICAL"

):

&#x20;   overall\_status = "CRITICAL"



elif (

&#x20;   cpu\_status == "WARNING"

&#x20;   or memory\_status == "WARNING"

&#x20;   or disk\_status == "WARNING"

):

&#x20;   overall\_status = "WARNING"



else:

&#x20;   overall\_status = "NORMAL"

```



The highest-severity resource determines the overall system status.



Example:



```text

CPU:     NORMAL

Memory:  CRITICAL

Disk:    NORMAL



Overall System Status: CRITICAL

```



\---



\# 19. System Health Monitor Project



The main Python fundamentals project for Week 4 is:



\## `system\_monitor.py`



The program follows this workflow:



```text

Computer

&#x20;  ↓

Collect System Metrics

&#x20;  ↓

CPU / Memory / Disk

&#x20;  ↓

check\_usage()

&#x20;  ↓

NORMAL / WARNING / CRITICAL

&#x20;  ↓

Determine Overall Health

&#x20;  ↓

Generate Timestamped Report

&#x20;  ↓

Terminal + Log File

```



Example output:



```text

=== SYSTEM HEALTH REPORT ===

Time: 2026-09-20 14:57:07

Hostname: SidyLaptop

Operating System: Windows

OS Release: 11

CPU Usage: 5.3% - NORMAL

Memory Usage: 85.1% - CRITICAL

Disk Usage: 48.4% - NORMAL

Overall System Status: CRITICAL

```



The project demonstrates the automation pattern:



> \*\*Collect → Analyze → Decide → Report → Save\*\*



\---



\# 20. Troubleshooting Lessons



Troubleshooting was an important part of Week 4.



\## RecursionError



I accidentally called a function from inside itself without a stopping condition.



This caused:



```text

RecursionError: maximum recursion depth exceeded

```



The solution was to separate responsibilities:



```text

Function → Check one server

Loop     → Process multiple servers

```



\---



\## Function Name Collision



I created a function:



```python

def check\_usage(usage):

```



and later accidentally attempted to reuse the same name for a list:



```python

check\_usage = \[...]

```



This would replace the function reference.



The lesson was to use descriptive and unique variable names.



\---



\## File Path Troubleshooting



When running the system monitor from the wrong directory, Python returned:



```text

\[Errno 2] No such file or directory

```



I verified the current directory and inspected the project structure before correcting the command.



From the Week 4 directory:



```powershell

python .\\system\_monitor.py

```



This reinforced an important troubleshooting process:



```text

Read error

&#x20;  ↓

Identify failure layer

&#x20;  ↓

Verify current directory

&#x20;  ↓

Verify file path

&#x20;  ↓

Correct path

&#x20;  ↓

Retest

```



\---



\# 21. Git and GitHub Practices



Week 4 work is stored in the bootcamp GitHub repository.



Useful Git commands:



```powershell

git status

git diff

git diff --staged

git add

git commit

git push

git log --oneline

git ls-files

```



Before committing files, I verify what Git is tracking and review staged changes.



Generated logs and sensitive files should not normally be committed.



Example `.gitignore` entries:



```gitignore

\_\_pycache\_\_/

\*.pyc

.venv/

venv/

\*.log

.env

\*.pem

```



Security rule:



> Never commit AWS access keys, secret access keys, passwords, private keys, or other credentials to GitHub.



\---



\# Key Lessons from Python Fundamentals



Python became easier to understand when I stopped thinking about individual commands and started thinking about the complete workflow.



```text

INPUT / DATA

&#x20;    ↓

VARIABLES

&#x20;    ↓

LISTS / DICTIONARIES

&#x20;    ↓

LOOPS

&#x20;    ↓

FUNCTIONS

&#x20;    ↓

CONDITIONS

&#x20;    ↓

DECISION

&#x20;    ↓

OUTPUT / LOG

```



For cloud engineering, the same pattern can eventually become:



```text

AWS API

&#x20;  ↓

Python / boto3

&#x20;  ↓

Collect AWS Resource Data

&#x20;  ↓

Analyze

&#x20;  ↓

Make Decision

&#x20;  ↓

Automate Action

&#x20;  ↓

Log Result

```



\---



\# Week 4 Progress



\## Completed



\- \[x] Python syntax and variables

\- \[x] Data types

\- \[x] User input

\- \[x] Conditional statements

\- \[x] Boolean logic

\- \[x] Lists

\- \[x] Dictionaries

\- \[x] Loops

\- \[x] Functions

\- \[x] Parameters and arguments

\- \[x] Return values

\- \[x] File handling

\- \[x] Exception handling

\- \[x] Modules

\- \[x] `datetime`

\- \[x] `platform`

\- \[x] `psutil`

\- \[x] Real CPU monitoring

\- \[x] Real memory monitoring

\- \[x] Real disk monitoring

\- \[x] System health classification

\- \[x] Overall system health

\- \[x] Timestamped reports

\- \[x] Log file generation

\- \[x] Python troubleshooting

\- \[x] System Health Monitor project



\## Next



\- \[ ] AWS SDK for Python (`boto3`)

\- \[ ] Connect Python to AWS

\- \[ ] Read AWS resource information

\- \[ ] EC2 automation

\- \[ ] S3 automation

\- \[ ] Week 4 AWS automation project



\---



\# Engineering Takeaway



The most important lesson from Week 4 is that Python can turn repetitive operational work into automation.



Instead of manually checking information and making the same decision repeatedly, a script can:



```text

Collect

&#x20;  ↓

Analyze

&#x20;  ↓

Decide

&#x20;  ↓

Act

&#x20;  ↓

Report

```



The next step is to apply this same pattern to AWS using `boto3`.

