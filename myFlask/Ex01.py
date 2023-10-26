# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:51:02 2023

@author: USER
"""

from flask import Flask,request,render_template
import db


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def mynews():
    return 'It is News'


@app.route('/product')
def allproduct():
    
    sql = "select * from product where platform='Pchome' order by id desc limit 30"
    cursor = db.conn.cursor()  # 建立資料庫物件資料集
    cursor.execute(sql)  # 執行sql語法
    db.conn.commit() #馬上生效
    
    res = cursor.fetchall()  # 從 cursor資料集中抓取所有的資料
    
    
    sql = "select * from product where platform='Yahoo' order by id desc limit 30"
    cursor = db.conn.cursor()  # 建立資料庫物件資料集
    cursor.execute(sql)  # 執行sql語法
    db.conn.commit() #馬上生效
    
    res2 = cursor.fetchall()  # 從 cursor資料集中抓取所有的資料    
    
    
    return render_template('product.html',**locals())


@app.route('/foods')
def tvbsfoods():
    
    sql = "select * from foods order by id desc"
    cursor = db.conn.cursor()  # 建立資料庫物件資料集
    cursor.execute(sql)  # 執行sql語法
    db.conn.commit() #馬上生效
    
    res = cursor.fetchall()  # 從 cursor資料集中抓取所有的資料
    
    
    return render_template('foods.html',result = res)


app.run()