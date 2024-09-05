z = torch.matmul(x,w)+b
print(z.requires_grad)

with torch.no_grad():
  z = torch.matmul(x,w)+b
print(z.requires_grad)

# Alternate Mwthod
z = torch.matmul(x,w)+b
z_det = z.detach()
print(z_det.requires_grad)
