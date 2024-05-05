from torchvision import datasets
from torchvision.transforms import ToTensor, Lamda
ds = datasets.FashionMNIST(
  root="data",
  train=True,
  download=True,
  transform=ToTensor(),
  target_transform=Lamda(lamda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y, value=1))
                        )
