# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:49:59 2023

@author: USER
"""

import pymysql

dbsetting = {
    
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456789',
    'db':'web',
    'port':3306,
    'charset':'utf8'
      
    
    }


conn = pymysql.connect(**dbsetting)