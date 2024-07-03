seq_modules = nn.Sequential(
  flatten,
  layer1.
  nn.ReLU(),
  nn.Linear(20, 10)
)
input_image = torch.rand(3,28,28)
logits = seq_modules(input_image)
