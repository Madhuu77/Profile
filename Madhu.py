# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 03:44:44 2024

@author: Madhu
"""
class Customer:
    def __init__(self,name,email,phone):
        self.name=[]
        self.email=[]
        self.phone=[]
    def Register(self,n,e,p):
        self.name.insert(0,n)
        self.email.insert(0,e)
        self.phone.insert(0,p)
    def Update_name(self,n,new):
        self.name[n]=new
    def Update_email(self,e,new):
        self.email[e]=new
    def Update_phone(self,p,new):
        self.phone[p]=new
    def display(self):
        print("Name:",self.name)
        print("e-mail:",self.email)
        print("phone no.",self.phone)
user=Customer(name=[],email=[],phone=[])
user.Register("Madhu", "v8000m@gmail.com", 8618112973)
user.display()