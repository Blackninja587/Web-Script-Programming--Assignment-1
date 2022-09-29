# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:43:40 2021

@author: sambr
"""


#Trying to transfer to MIPS


t1 = float(input("Enter your height in cm: "))
t2 = float(input("Enter your weight in kg: "))

t1 = t1/100
t1 = t1**2
s0 = t2/t1

#print(s0)

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0

#UW
if s0 <= (18.4):
    s1 = 1
    if s1 == 1:
        print("You are underweight.")
        #j EXIT
    #if s1 != 1:
        #j  H

#H
if s0 <= (24.9):
    s2 = 1
    if s1 == 1:
        s2 = 0
    else:
        print("You are healthy.")
        #j EXIT
    #if s2 != 1:
        #j  OW

#OW
if s0 <= (29.9):
    s3 = 1
    if s1 == 1:
        s2 = 0
        s3 = 0
    elif s2 == 1:
        s3 = 0
    else:
        print("You are over weight.")
        #j EXIT
    #if s3 != 1:
        #j  SOW

#SOW
if s0 <= (34.9):
    s4 = 1
    if s1 == 1:
        s2 = 0
        s3 = 0
        s4 = 0
    elif s2 == 1:
        s3 = 0
        s4 = 0
    elif s3 == 1:
        s4 = 0
    else:
        print("You are severly over weight.")

#O
if s0 <= (39.9):
    s5 = 1
    if s1 == 1:
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0
    elif s2 == 1:
        s3 = 0
        s4 = 0
        s5 = 0
    elif s3 == 1:
        s4 = 0
        s5 = 0
    elif s4 == 1:
        s5 = 0
    else:
        print("You are obese.")

#CO
if 40 <= (s0):
    s6 = 1
    if s6 == 1:
        print("You are chronically obese.")


#slt $s0, $t6, $t3
#bne $s0, $zero, Loop
#beq $s0, $zero, Exit