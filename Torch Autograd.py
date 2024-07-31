%matplotlib inline
import torch

x = torch.ones(5) # input tensor
y = torch.zeros(3) # expected output
w = torch.randn( 5, 3, requires_grad=True)
b = torch.rand( 3, requires_grad=True)
z = torch.natmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z,y)
