import numpy as np
vector=np.linspace(1,20,15,dtype=int)
print(vector)
reshape=vector.reshape((3,5))
print(reshape)
reshape[np.where(reshape == np.max(reshape,axis=1,keepdims=True))] = 0
print("Result:\n",reshape)