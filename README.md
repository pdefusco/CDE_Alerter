# CDE Alerter

## Objective

CDE is the Cloudera Data Engineering Service, a containerized managed service for Large Scale Batch Pipelines with Spark featuring Airflow and Iceberg.

The CDE Alerter is a Python script that can be used to monitor jobs in a CDE Virtual Cluster. It allows you to implement a set of rules to notify a set of recipients in case of a particular event. The Alerter relies on cde_python, a custom Python wrapper for the CDE API.

## Requirements

In order to use the script you need to have:
* A CDE Virtual Cluster (Azure, AWS and Private Cloud ok).
* A Virtual Machine or local computer that has the ability to reach the CDE Virtual Cluster where your CDE Jobs are running.
* Python 3.6 or above.
* A gmail account with 2-step authentication and an App password.
* No script code changes are required.

## Instructions

#### Step 0: Project setup

Clone this GitHub repository to your local machine or the VM where you will be running the script.

```
mkdir ~/Documents/CDE_Alerter
cd ~/Documents/CDE_Alerter
git clone https://github.com/pdefusco/CDE_Alerter.git
```

Alternatively, if you don't have GitHub create a folder on your local computer; navigate to [this URL](https://github.com/pdefusco/CDE_Alerter.git) and download the files.

#### Step 1: Create a Python Virtual Environment and Install Requirements

Although a Python Virtual Environment is optional, it is highly recommended. To create one and install requirements execute the following commands:

```
#Create
python3 -m venv venv

#Activate
source venv/bin/activate

#Install single package
pip install pandas

#Install requirements
pip install requirements.txt
```

#### Step 2: Run the script

Before you can run the script you will need:
* The CDE JOBS API URL for the intended CDE Virtual Cluster you want to monitor.
* The Gmail APP password (not just the account login password). If you need help setting this up for the first time:
  1. Recommended: [Create a New Gmail Account](https://support.google.com/mail/answer/56256?hl=en)
  2. [Enable 2-step Authentication and Create an App Password](https://www.youtube.com/watch?v=hXiPshHn9Pw)
* The CDP User and Password you will authenticate into the CDE Virtual Cluster with.

Before you can run the script you should have the following parameters ready:


To run the script,
