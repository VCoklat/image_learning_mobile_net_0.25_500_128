#!/usr/bin/python

import os, sys
import time

# Open a file testing deteksi makanan di atas lantai
path = "../../test_image/food/10"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
   os.system('python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=../../test_image/food/10/'+file) #menjalankan label_image.py di dalam folder scripts dengan grafik yang digunakan adalah di dalam tf_files/retrained_graph.pb
   

# Open a file
path = "../../test_image/water/10"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
   os.system('python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=../../test_image/water/10/'+file)
   

# Open a file
path = "../../test_image/clean/10"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
   os.system('python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=../../test_image/clean/10/'+file)
   

# Open a file
path = "../../test_image/dirty/10"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
   os.system('python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=../../test_image/dirty/10/'+file)
   
