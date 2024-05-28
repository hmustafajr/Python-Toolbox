class NeuralNetwork(nn.Module):
  def __init__(self):
    super(NeuralNetwork, self).__init__()
    self.flatten = nn.Flatten()
    self.linear_relu_stack = nn.Sequential(
        nn.linear(28*28, 512),
        nnReLu()
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 10),
        nn.ReLU()
    )
    def forward(self, x):
      x = self.flatten(x)
      logits = self.linear_relu_stack(x)
      return logits
      
# We create an instance of NeuralNetwork, and move it to the device, and print its structure.
model = NeuralNetwork().to(device)
print(model)

# To use the model, we pass it the input data. This executes the model's forward, along with some background operations.
# However, do not call model.forward() directly! Calling the model on the input returns a 10-dimensional tensor with raw predicted values for each class.
# We get the prediction densities by passing it through an instance of the nn.Softmax.

X = torch.rand(1, 28, 28, device=device)
logits = model(x)
pred_prob = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")
