# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:27:16 2023

@author: USER
"""
"""
前台要求request
倒轉到網頁render_template
"""

import db
from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')



@app.route('/product')

def allproduct():
    
    sql = "select * from product where platform='Pchome' order by id desc limit(30)"
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchall()    


   
    sql = "select * from product where platform='Yahoo' order by id desc limit(30)"
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res2 = cursor.fetchall()    
    return render_template('product.html',**locals())

#local 裡面的變數全部都丟 用於兩個以上的result要傳送

@app.route('/foods')

def tvbsfoods():
    
    sql = 'select * from foods order by id desc'
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    result = cursor.fetchall()    
    return render_template('foods.html',result=result)

app.run()


