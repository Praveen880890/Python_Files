import argparse


ap = argparse.ArgumentParser()

ap.add_argument("-a","--fo",required = True,
                help="First Operand")
ap.add_argument("-b","--so",required = True,
                help = "Second Operand")

args = vars(ap.parse_args())

a = int(args["fo"])
b= int(args["so"])
print(a,b)
