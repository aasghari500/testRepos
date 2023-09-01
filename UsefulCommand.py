import torch
import numpy as np

npa  = np.array([1., 2., 3.])

m2 = torch.from_numpy(npa)
m2 = m2.to(torch.float32)                   
#m  = torch.tensor([[1., 2., 3.],  [4., 5., 6.]])
print (m2.dtype)