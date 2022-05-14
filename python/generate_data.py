from random import random
# 50.874844 4.717616
# 50.874844, 4.707616

# get random values around x_center and y_center
x_center = 50.874844
y_center = 4.707616

with open('data.txt', 'w') as f:
    for i in range(5000):
        x = x_center + (random() - 0.5)/10
        y = y_center + (random() - 0.5)/10
        f.write(str(x) + " " + str(y))
        f.write('\n')
