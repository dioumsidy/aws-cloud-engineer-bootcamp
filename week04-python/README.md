\# Week 4 — Python for Cloud Engineering



\## Overview



Week 4 focuses on learning Python for cloud engineering and automation.



The goal is not to become a full-time Python software developer, but to understand enough Python to build automation scripts, work with system data, troubleshoot scripts, and eventually interact with AWS services programmatically.



\## Concepts Learned



\- Variables

\- Strings, integers, floats, and Booleans

\- User input

\- if / elif / else

\- Boolean logic: and, or, not

\- Lists

\- Dictionaries

\- for loops

\- Functions

\- Parameters and arguments

\- return values

\- File handling

\- Exception handling

\- Python modules

\- datetime

\- platform

\- Third-party Python packages

\- psutil

\- System monitoring automation



\## System Health Monitor



The main Python fundamentals project is a system-health monitoring script.



The script collects real system information including:



\- Hostname

\- Operating system

\- OS release

\- CPU utilization

\- Memory utilization

\- Disk utilization



The script then classifies resource usage as:



\- NORMAL: below 60%

\- WARNING: 60% to 79%

\- CRITICAL: 80% or higher



It also determines an overall system health status.



\## Automation Flow



Collect → Analyze → Decide → Report → Save



The program:



1\. Collects system metrics using `psutil`.

2\. Uses a Python function to evaluate resource utilization.

3\. Determines health status.

4\. Creates a timestamped health report.

5\. Displays the report in the terminal.

6\. Saves the report to a log file.



\## Python Packages



Install psutil:



```powershell

python -m pip install psutil

