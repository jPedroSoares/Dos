from subprocess import Popen, PIPE
import time

process = []

while True:
        process.append(Popen('telnet ismycomputeron.com 80', shell=True, stdout=PIPE))
        time.sleep(0.1)

# nmap -pn <ip>
