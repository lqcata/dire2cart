#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Convert direc coordiation to cartesian Writen By Qiang 
import subprocess

subprocess.call('rm POSCAR_C -f', shell = True)

file_read = open('POSCAR', 'r')

line = file_read.readlines()
a1 = float(line[2].split()[0])
a2 = float(line[3].split()[0])
a3 = float(line[4].split()[0])
b1 = float(line[2].split()[1])
b2 = float(line[3].split()[1])
b3 = float(line[4].split()[1])
z1 = float(line[2].split()[2])
z2 = float(line[3].split()[2])
z3 = float(line[4].split()[2])

num_atoms = sum([int(x) for x in line[6].split()])

x_cartesian = []
y_cartesian = []
z_cartesian = []
tf = []

start_num = 9 # With Selected T T T, coordination starts from line 9
if 'S' not  in line[7]: 
    start_num = 8 # without Selected, No  T T T , coordination starts from line 8 

for i in range(start_num, num_atoms + start_num):
    x_cartesian.append(float(line[i].split()[0]) * a1 + float(line[i].split()[1]) * a2 + float(line[i].split()[2]) * a3)
    y_cartesian.append(float(line[i].split()[0]) * b1 + float(line[i].split()[1]) * b2 + float(line[i].split()[2]) * b3)
    z_cartesian.append(float(line[i].split()[0]) * z1 + float(line[i].split()[1]) * z2 + float(line[i].split()[2]) * z3)
    if len(line[i].split()) > 3:   # if  T T T exist, there are more than 3 elements in the list line[i].split()
        tf.append((line[i].split()[3]))
    else:
        tf.append(' ')   # if there is no T T T, use space instead. 

file_out = open('POSCAR_C', 'a')

for i in range(0,7):
    file_out.write(line[i].rstrip() + '\n')  # first 7 lines are kept the same 

if 'S' in line[7]:
    file_out.write(line[7].rstrip()+ '\n')  # if  T T T exists, write the Selective line 
file_out.write('Cartesian' + '\n')          # Coordination system is Cartesian now. 

for i in range(0,len(x_cartesian)):
    file_out.write("%+-3.10f   %+-3.10f   %+-3.10f   %s %s %s\n"  
    %(x_cartesian[i], y_cartesian[i], z_cartesian[i], tf[i], tf[i], tf[i]))

file_read.close()
file_out.close()

print 'POSCAR with Cartesian Coordiations is named as POSCAR_C'
