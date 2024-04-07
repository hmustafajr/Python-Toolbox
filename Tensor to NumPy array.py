t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()

#Example output
t: tensor([1., 1., 1., 1., 1.])
n: [1. 1. 1. 1. 1.]

# a change in the tensor reflects in the NumPy array.
t.add_(1)
print(f"t: {t}")
print(f"n: {n}"()

# Example output
t: tensor([2., 2., 2., 2., 2.])
n: [2. 2. 2. 2. 2.]
