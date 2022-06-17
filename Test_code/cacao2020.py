import numpy as np
setting={x:np.array([(x-1)//3,(x-1)%3]) for x in range(10)}
setting[0]=np.array([3,1])

print(setting)