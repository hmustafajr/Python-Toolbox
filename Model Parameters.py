print("Model structure: ", model, "\n\n")
for name, param in model.named_parameters():
  print(f"Layer: {name} | Size : {param.size()} | Values : {param[2]} \n")
