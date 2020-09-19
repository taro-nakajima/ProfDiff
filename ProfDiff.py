#Macro for 1D integration
#usage:  python Integrate1D_v1_3_2.py [list file name] [output file name]
import math
import sys
import numpy as np

args=sys.argv
if (len(args)<3):
	print("usage:  python ProfDiff.py [config file name] [output file name without ".txt"]")
	sys.exit()

FH = open(args[1],"r")

print("Input filename : %s" % args[1])
print("Output filename : %s" % args[2])

temp = FH.readline()
array = temp.split()
skipline = int(array[0])
print("skipline : %d" % skipline)

temp = FH.readline()
array = temp.split()
Index_X = int(array[0])
print("index of x : %d" % Index_X)

temp = FH.readline()
array = temp.split()
Index_Fx = int(array[0])
print("index of F(x) : %d" % Index_Fx)

temp = FH.readline()
array = temp.split()
Index_Fx_er = int(array[0])
print("index of F(x)_err : %d" % Index_Fx_er)

temp = FH.readline()
array = temp.split()
RN = int(array[0])
print("Initial run number : %d" % RN)

temp = FH.readline()
array = temp.split()
Mon1 = float(array[0])
Mon2 = float(array[1])
print("X range for integration : {0} to {1}".format(Mon1, Mon2))

print("----------------------------------------")

for line in FH:
	filenames=line.strip().split()
	print filenames[0]
	print filenames[1]
	file1_matrix=np.genfromtxt(filenames[0],delimiter='\t',skiprows=skipline)
	file2_matrix=np.genfromtxt(filenames[1],delimiter='\t',skiprows=skipline)

	outfile=args[2]+str(RN)+".txt"
	FH2=open(outfile,"w")
	FH2.write("#x  Int1  Int1_err  Int2  Int2_err  Int1-2  Int1-2_err\n")
	for ii in range(file1_matrix.shape[0]):
		IntSubt=file1_matrix[ii][Index_Fx]/Mon1 - file2_matrix[ii][Index_Fx]/Mon2
		IntSubt_err = math.sqrt(file1_matrix[ii][Index_Fx_er]**2.0/Mon1**2.0 + file2_matrix[ii][Index_Fx_er]**2.0/Mon2**2.0 )
		FH2.write("{0}  {1}  {2}  {3}  {4}  {5}  {6}\n".format(file1_matrix[ii][Index_X],file1_matrix[ii][Index_Fx],file1_matrix[ii][Index_Fx_er],file2_matrix[ii][Index_Fx],file2_matrix[ii][Index_Fx_er],IntSubt,IntSubt_err))
	FH2.close()

FH.close()
