import torchvision.transforms as transforms

def get_transforms(train=True):
    """
    Returns transformations for training and validation
    """

    if train:
        transform = transforms.Compose([
            transforms.Resize((224, 224)),              # Fix input size
            transforms.RandomHorizontalFlip(p=0.5),     # Augmentation
            transforms.RandomRotation(10),              # Slight rotation
            transforms.ToTensor(),                      # Convert to tensor
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],             # ImageNet mean
                std=[0.229, 0.224, 0.225]               # ImageNet std
            )
        ])
    else:
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    return transform