from src.models.predict import predict

label, conf = predict("your_image.jpg")
print(f"Prediction: {label} ({conf*100:.2f}%)")