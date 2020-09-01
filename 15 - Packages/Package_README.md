# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:16:46 2020

@author: aduzo
"""


Getting what someone else has created is via a package.
This is a published collection of modules How do you know what is available in a package is through experience
you can search python package index for a package or via internet

What we did:
- How we can work with our own modules
- How  we can work with external packages
- How we can setup a virtual environment

* Much of the applications we are creating is going to have some level of requirement for installing packages  e.g 
cognitive services, Flask, Django e.t.c we are going to be installing all of those various packages.

using colorama as an example
This is a little package that will help you easily change the color of 
text when you do your print.

# Installing packages
* Create the folder first (i  my folder name is "venv")
* We have a little utility called 'virtualenv' that we can use to do exactly that.

## Install a virtual environment (this installed globally)
pip install virtualenv

* Windows systems (Create that virtual environment) 
eitheruse python or py -3
- python -m venv <folder_name>
- py -3 -m venv <folder_name> 

-m ==grab a particular module ,  venv= virtual environment then specify the folder name

## Using virtual environments
* Windows systems
* cmd.exe
<folder_name>\Scripts\Activate.bat

* Powershell
- In the case of CurrentUser ExecutionPolicy not  RemoteSigned,
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser (https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7)

<folder_name>\Scripts\Activate.ps1


* bash shell
. ./<folder_name>/Scripts/activate


## Install the package
- After venv is activated in your powershell
Do the following
pip install colorama

* Install from a list of packages
pip install -r requirements.txt

* requirements.txt is in same directory as "venv" folder
* requirements.txt This is a text file containing list all of the
* packages that you will be using
colorama

Using pip like this will install the packages globally which cn result in a version issue.

Use a local install by utilizing a virtual environment
* Virtual Environment
This is a folder that have all the code that you need to run the application you are creating.

Meaning everything that i need i going to be installed into that folder then I'm able it.
