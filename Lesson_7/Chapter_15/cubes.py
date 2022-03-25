import matplotlib.pyplot as plt

#plot 1
cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
ax1 = plt.subplot(1,2,1) 
ax1.plot(inputVal,cubed,ls = 'dashdot', c = 'blue', marker = '*')
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()


#plot 2
pow = []
for num in inputVal:
    pow.append(num**2) 
ax2 = plt.subplot(1,2,2)    
plt.style.use("seaborn-dark-palette")
ax2.plot(inputVal,pow)#,ls = 'dotted', c = 'red', lw = "5.0"
plt.title("Numbers Raised")
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("Fun With Numbers", c = 'purple', fontfamily = "Times New Roman", fontsize = 22)
plt.show()