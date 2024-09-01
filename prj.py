import pandas as pd 
import datetime 
import os 
import time 
from pathlib import Path 
import pysftp 
import xlsxwriter as xw 
import unlzw3 
import warnings 
import paramiko as pa
from getpass import getpass 
warnings.filterwarnings('ignore','.*Failed to load HostKeys.*') 

print("#########################\n")
hostname = input("\nEnter Hostname: ") 
uid = input("\nEnter Username Id: ") 
pwd = getpass("\nEnter Password: ") 
getpth = input("Enter path of files:")
putpth = input("Enter final folder:")
ftot = 0 
excep = [] 
dirp = '/home/qkcra/DataWareHouse' 
codes = [] 
years = [] 
 
def getstate(): 
  rpth = f'{getpth}' 
  cnopts = pysftp.CnOpts() 
  cnopts.hostkeys = None  
  with pysftp.Connection(host = hostname,username=uid,password=pwd,cnopts=cnopts) as sftp: 
    sftp.get(rpth,'states.txt') 
 
def getfile(a,b): 
  rpth = f'{putpth}'+f'/{a}/{b}/output_{a}.out.Z' 
  cnopts = pysftp.CnOpts() 
  cnopts.hostkeys = None  
  with pysftp.Connection(host = hostname,username=uid,password=pwd,cnopts=cnopts) as sftp: 
    sftp.get(rpth,f'{a}/{b}.out.Z') 
 
def putfile(a,lpth): 
  rpth = f'{putpth}'+f'/{a}/{a}.xlsx' 
  cnopts = pysftp.CnOpts() 
  cnopts.hostkeys = None  
  with pysftp.Connection(host = hostname,username=uid,password=pwd,cnopts=cnopts) as sftp: 
    sftp.put(lpth,rpth) 
  
 
 
pd.options.display.float_format = '{:.2f}'.format 
 
a = [] 
x = [] 
no = [] 
year = [] 
inp = [] 
 
assign=dict() 
for i in range(9): 
    assign[i+4] = i+10 
for i in range(3): 
    assign[i+1] = i+19 
 
def time_convert(sec): 
    mins = sec // 60 
    sec = sec % 60 
    hours = mins // 60 
    mins = mins % 60 
    return "Time Lapsed = {0} hours   {1} minutes   {2} seconds".format(int(hours),int(mins),round(sec,2)) 
 
 
 
def getcode(): 
    cnopts = pysftp.CnOpts() 
    cnopts.hostkeys = None  
    with pysftp.Connection(host = hostname,username=uid,password=pwd,cnopts=cnopts) as sftp: 
        file = sftp.listdir(dirp) 
        for f in file: 
            if f.isdigit(): 
                codes.append(f) 
                foname = sftp.listdir(dirp +"/"+ f) 
                for y in foname: 
                    if y not in years: 
                        years.append(y) 
 
 
getcode() 