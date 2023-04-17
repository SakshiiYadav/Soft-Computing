import math
bias = float(input("Enter the value for bias:"))
n = int(input("Enter the number of input neurons:"))
print("bias value is",bias)
print("U decided to go with",n,"input neurons")
weights=[]
inputs=[]
for i in range (0,n):
    a=float(input("Enter input value"))
    inputs.append(a)
    b=float(input("Enter weight value"))
    weights.append(b)
print("Weights are :")
print(weights)
print("Inputs are :")
print(inputs)
net_input = bias
for i in range(0,n):
    net_input = net_input + (weights[i]*inputs[i])
print("Net Input is :",net_input)
#Calculating output using binary
#sigmoidal activation function
binary_op=1/(1+(math.exp(-net_input)))
print("output using binary sigmoidal activation function",
     round(binary_op,3))
#Calculating output using binary
#sigmoidal activation function
bipolar_op=-1+(2/(1+(math.exp(-net_input))))
print("output using bipolar sigmoidal activation function",
     round(bipolar_op,3))
