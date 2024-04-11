import torch
from torch_geometric.utils import dense_to_sparse
if __name__ == "__main__":
  
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(device)
    print('hello world')