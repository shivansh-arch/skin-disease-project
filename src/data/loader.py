import os
from torchvision import datasets
from torch.utils.data import DataLoader
from src.data.preprocess import get_transforms
from src.config.config import Config
from src.utils.logger import get_logger

# Initialize
config = Config()
logger = get_logger("data_loader")


def get_dataloaders():
    """
    Returns train and validation dataloaders
    """

    train_path = os.path.join(config.get("paths", "processed_data"), "train")
    val_path = os.path.join(config.get("paths", "processed_data"), "val")

    logger.info(f"Loading training data from: {train_path}")
    logger.info(f"Loading validation data from: {val_path}")

    # Check if paths exist
    if not os.path.exists(train_path):
        logger.error(f"Train path not found: {train_path}")
        raise FileNotFoundError(f"Train path not found: {train_path}")

    if not os.path.exists(val_path):
        logger.error(f"Validation path not found: {val_path}")
        raise FileNotFoundError(f"Validation path not found: {val_path}")

    # Datasets
    train_dataset = datasets.ImageFolder(
        root=train_path,
        transform=get_transforms(train=True)
    )

    val_dataset = datasets.ImageFolder(
        root=val_path,
        transform=get_transforms(train=False)
    )

    logger.info(f"Classes found: {train_dataset.classes}")
    logger.info(f"Training samples: {len(train_dataset)}")
    logger.info(f"Validation samples: {len(val_dataset)}")

    # DataLoaders
    train_loader = DataLoader(
        train_dataset,
        batch_size=config.get("training", "batch_size"),
        shuffle=True,
        num_workers=0
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=config.get("training", "batch_size"),
        shuffle=False,
        num_workers=0
    )

    return train_loader, val_loader