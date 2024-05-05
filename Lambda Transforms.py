target_transform = Lambda(lambda y: torch.zeros(
  10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))
