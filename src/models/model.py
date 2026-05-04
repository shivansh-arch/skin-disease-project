import torch
import torch.nn as nn
import torchvision.models as models
from src.config.config import Config
from src.utils.logger import get_logger

# Init
config = Config()
logger = get_logger("model")


def get_model():
    """
    Loads pretrained EfficientNet and modifies it for our dataset
    """

    num_classes = config.get("model", "num_classes")

    logger.info(f"Initializing model with {num_classes} classes")

    # Load pretrained model
    model = models.efficientnet_b0(weights="IMAGENET1K_V1")

    # Freeze all layers
    for param in model.features[-2:].parameters():
        param.requires_grad = True

    # Replace classifier
    in_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(in_features, num_classes)

    logger.info("Model initialized successfully")

    return model