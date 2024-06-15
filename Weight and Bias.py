#The nn.Linear module randomly initializes the weights and bias for each layer and internally stores the values in Tensors
print(f"First Linear weights: {model.linear_relu_stack[0].weight} \n")
print(f"First Linear biases: {model.linear_relu_stack[0].bais} \n")
