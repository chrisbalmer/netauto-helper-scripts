# coding: utf-8
import sys
import yaml
import paramiko
import base64
import time
import keychain
import re
import console

def connect_to_device(ssh):
	print "\n\nConnecting to device..."
	keys = ssh.get_host_keys()
	keys.add(hostname,'ssh-rsa',public_key)
	password = keychain.get_password(hostname,
	                                 username)
	ssh.connect(hostname,username=username,password=password)
	
	shell = ssh.invoke_shell()
	print "Connected to " + hostname + "."
	shell.send("term len 0\n")
	return shell

def send_command(shell, command):
	shell.send(command + "\n")
	time.sleep(1)
	output = shell.recv(10000)
	
	return output
		
def logout(shell):
	shell.send('logout\n')
	print '\nDisconnected from device\n'

console.clear()

# Load options
with open('devices.yaml', 'r') as file:
		device_list = yaml.load(file)

hostname = device_list['device1']['host']
public_key_string = device_list['device1']['public_key']
username = device_list['device1']['username']
public_key = paramiko.RSAKey(data=base64.b64decode(public_key_string))


# Prep the SSH connection
ssh = paramiko.SSHClient()
shell = connect_to_device(ssh)

print send_command(shell, 'reload\n')

logout(shell)

print '\n\nComplete!'
console.hud_alert('Complete!',duration=2)