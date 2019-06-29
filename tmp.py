from torchvision import transforms

import numpy as np
import torch


img = torch.arange(4).view(2, 2)
print(img)

height, width = img.shape[-2:]
img = img.flip(-1)

print(img)


