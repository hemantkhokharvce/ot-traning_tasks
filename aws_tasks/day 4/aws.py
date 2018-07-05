#!/usr/bin/env python
import boto3
import time
import sys
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


def stopInstances():

	for instance in ec2.instances.all():
		for tag in instance.tags:
			if tag['Key'] == 'Name':
				if tag['Value'] == 'nginx' or tag['Value'] == 'myapp' or tag['Value'] == 'mydb':
					client.stop_instances(InstanceIds=[instance.id], DryRun=False)
					instance.wait_until_stopped()
	startInstancesInSeries(3)

def startInstancesInSeries(i):
		for instance in ec2.instances.all():	
			for tag in instance.tags:
				if tag['Key'] == 'boot-order':
					if tag['Value'] == str(i):
						print str(i) 
						client.start_instances(InstanceIds=[instance.id], DryRun=False)
						instance.wait_until_running()
						instance.reload()
						print instance.state
						startInstancesInSeries(i-1)
						
		stopInstancesInSeries(1)

def stopInstancesInSeries(i):
	if str(i) <= '3':
		for instance in ec2.instances.all():	
			for tag in instance.tags:
				if tag['Key'] == 'boot-order':
					if tag['Value'] == str(i): 
						print str(i)
						client.stop_instances(InstanceIds=[instance.id], DryRun=False)
						instance.wait_until_stopped()
						instance.reload()
						print instance.state
						stopInstancesInSeries(i+1)
	else:
		sys.exit(0)
						
stopInstances()

