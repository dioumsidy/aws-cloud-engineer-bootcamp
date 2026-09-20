import platform
import psutil
from datetime import datetime


def check_usage(usage):
    if usage >= 80:
        return "CRITICAL"
    elif usage >= 60:
        return "WARNING"
    else:
        return "NORMAL"

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("C:\\").percent
hostname = platform.node()
operating_system = platform.system()
os_release = platform.release()


cpu_status = check_usage(cpu_usage)
memory_status = check_usage(memory_usage)
disk_status = check_usage(disk_usage)

if cpu_status == "CRITICAL" or memory_status == "CRITICAL" or disk_status == "CRITICAL":
    overall_status = "CRITICAL"

elif cpu_status == "WARNING" or memory_status == "WARNING" or disk_status == "WARNING":
    overall_status = "WARNING"

else:
    overall_status = "NORMAL"

report = (
    f"=== SYSTEM HEALTH REPORT ===\n"
    f"Time: {formatted_time}\n"
    f"Hostname: {hostname}\n"
    f"Operating System: {operating_system}\n"
    f"OS Release: {os_release}\n"
    f"CPU Usage: {cpu_usage}% - {cpu_status}\n"
    f"Memory Usage: {memory_usage}% - {memory_status}\n"
    f"Disk Usage: {disk_usage}% - {disk_status}\n"
    f"Overall System Status: {overall_status}\n"
)

print(report)

with open("system-health.log", "a") as file:
    file.write(report + "\n")

# print(f"CPU Usage: {cpu_usage}% - {cpu_status}")
# print(f"Memory Usage: {memory_usage}% - {memory_status}")
# print(f"Disk Usage: {disk_usage}% - {disk_status}")
# print(f"Hostname: {hostname}")
# print(f"Operating System: {operating_system}")
# print(f"OS Release: {os_release}")
