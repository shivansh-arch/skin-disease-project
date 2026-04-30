from src.config.config import Config

config = Config()

print("Batch size:", config.get("training", "batch_size"))
print("Model name:", config.get("model", "name"))