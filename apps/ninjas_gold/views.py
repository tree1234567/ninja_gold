# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):

    return render(request, 'ninjas_gold/index.html')

def gold(request):
    date_time = datetime.now()

    if 'amount' not in request.session.keys():
        request.session['amount'] = 0
    
    if 'log' not in request.session.keys():
        request.session['log'] = [] 
    

    if request.method == 'POST':

        request.session['place'] = request.POST['ninja']

        if request.session['place'] == "farm":
            gold_found = randint(10,20)
            request.session['amount'] += gold_found
            string = "you found "+ str(gold_found)+" gold coins at the farm.. time: " + str(date_time)
            request.session['log'].append(string)

        if request.session['place'] == "cave":
            gold_found = randint(5,10)
            request.session['amount'] += gold_found
            string = "you found "+ str(gold_found)+" gold coins in the cave.. time: " + str(date_time)
            request.session['log'].append(string)



        if request.session['place'] == "house":
            gold_found = randint(2,5)
            request.session['amount'] += gold_found
            string = "you found "+ str(gold_found)+" gold coins at the house.. time: " + str(date_time)
            request.session['log'].append(string)

        if request.session['place'] == "casino":
            gold_found = randint(-50,50)
            request.session['amount'] += gold_found
            if gold_found > 0:
                string = "you won "+ str(gold_found)+" gold coins at the casino.. time: " + str(date_time)
            if gold_found < 0:
                string = "you lost "+ str(gold_found*-1)+" gold coins at the casino.. time: " + str(date_time)
            request.session['log'].append(string)
            

        if request.session['place'] == 'reset':
            request.session['log'] = []
            request.session['amount'] = 0
            
        return redirect('/')