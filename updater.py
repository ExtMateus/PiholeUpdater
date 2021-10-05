#!/usr/bin/env python

import paramiko
import sys
import os

clear = lambda: os.system('clear')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip = ""
username = ""
password = ""
comandos = ["sudo apt update", "pihole -up", "pihole -g"]

def outputLines(ssh_stdout):
    output = ""
    for line in ssh_stdout:
        output = output + line
    print(output, end="\n")

def execComandos():
    for com in comandos:
        print("Comando: ", com)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(com)
        ssh_stdout = ssh_stdout.readlines()
        outputLines(ssh_stdout)

try:
    clear()
    ssh.connect(ip,username=username,password=password)
    execComandos()
    print("Sucesso!")

except Exception as e:
    sys.stderr.write("SSH connection error: {0}".format(e))
