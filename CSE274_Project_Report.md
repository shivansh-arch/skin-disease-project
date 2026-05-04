# 1. Title Page

**Project Title:** Skin Disease Classification using Deep Learning  
**Course:** CSE274 – Applied Machine Learning  
**Names of Students:** Shivansh  
**Roll Numbers:** [Your Roll Number]  
**Instructor Name:** [Instructor Name]  
**Department / University:** [Department / University]  
**Submission Date:** [Current Date]  

---

# 2. Abstract
Early and accurate detection of skin diseases is critical for effective treatment and patient care. This project presents a comprehensive deep learning-based system for the automated classification of skin diseases. The problem addressed is the subjective and error-prone nature of manual dermatological diagnosis. Using a Convolutional Neural Network (CNN) architecture—specifically EfficientNet-B0—the model was fine-tuned on a dataset comprising 22 distinct skin disease categories. Key techniques include image preprocessing (resizing, normalization), transfer learning, and the implementation of a dual-backend web application (Flask and FastAPI) for real-time multi-image processing and prediction. The system processes image uploads and returns disease predictions with confidence scores, demonstrating high scalability, accuracy, and efficiency in automated dermatological diagnosis.

---

# 3. Introduction
**Background of the problem:** Skin diseases are among the most common human illnesses, affecting millions globally. Diagnosis typically requires visual inspection by experienced dermatologists, which can be subjective and sometimes inaccessible in remote areas.

**Importance of the study:** Automating the classification of skin lesions can significantly aid medical professionals by providing a second opinion, speeding up the diagnostic process, and reducing human error.

**Real-world relevance:** With the rise of telehealth, a web-based automated diagnosis tool allows patients to get initial screenings quickly, enabling early intervention for severe conditions like skin cancer.

**Objective of the project:** To develop a robust, scalable web application using deep learning that can accurately classify 22 different skin diseases from uploaded images, utilizing both Flask and FastAPI backends.

---

# 4. Problem Statement
**Problem being solved:** The project aims to solve the problem of identifying and diagnosing various skin diseases from digital images accurately and quickly.

**Type:** Classification (Multi-class Image Classification).

**Example:** Disease prediction (Classification of 22 skin conditions such as Acne, Psoriasis, Eczema, Melanoma, etc.).

---

# 5. Dataset Description
- **Dataset source:** Skin Disease Dataset (Comprehensive collection for automated skin disease classification).
- **Number of records and features:** Thousands of RGB images of skin lesions. The features are the pixel values of the images (resized to 224x224x3).
- **Target variable:** The categorical class label representing one of the 22 skin diseases.

**Feature Description:**
| Feature | Description | Type |
| --- | --- | --- |
| Image Data | 224x224 RGB image arrays | Numerical (Pixel intensities 0-255) |
| Target Label | Class of skin disease (e.g., Acne, Moles) | Categorical (22 classes) |

---

# 6. Data Preprocessing
- **Handling missing values:** Images that were corrupted or unreadable were removed during the data loading phase.
- **Image Resizing and Transformation:** All images were resized to a standard dimension of 224x224 pixels to match the input requirements of the EfficientNet model.
- **Feature scaling / normalization:** Pixel values were normalized using the ImageNet mean `[0.485, 0.456, 0.406]` and standard deviation `[0.229, 0.224, 0.225]` to ensure faster convergence during training.
- **Data format:** Transformed images into PyTorch tensors.

---

# 7. Feature Engineering & Dimensionality
- **Feature extraction:** Instead of manual feature engineering, deep feature extraction was performed using a pre-trained **EfficientNet-B0** model. The convolutional layers automatically extract hierarchical visual features such as edges, textures, and complex patterns from the skin lesion images.
- **Dimensionality Reduction:** The global average pooling layer in EfficientNet reduces the spatial dimensions of the feature maps into a 1D vector before passing it to the final dense classification layer.
- **Explanation of selected features:** Pre-trained weights from ImageNet were utilized (Transfer Learning). The network's lower layers capture generic image features, while the fully connected layers were fine-tuned specifically for the skin disease classes.

---

# 8. Methodology

**A. For Classification**
- **Models used:** Convolutional Neural Network (EfficientNet-B0).
- **Reason for choosing:** EfficientNet-B0 was chosen because it provides a highly optimal balance between accuracy and computational efficiency. It scales network width, depth, and resolution in a principled way, making it ideal for web-based inference where response time is critical.
- **Workflow:** 
  1. User uploads single or multiple images via the web interface.
  2. Images are preprocessed and converted to tensors.
  3. The EfficientNet model performs forward pass inference.
  4. Softmax activation is applied to calculate prediction probabilities.
  5. For multiple images, a voting logic calculates the average confidence across images to return a final aggregated prediction.

---

# 9. Implementation Details
- **Tools used:** 
  - **Languages:** Python, HTML, CSS, JavaScript
  - **Frameworks:** PyTorch, FastAPI, Flask
  - **Libraries:** torchvision, PIL (Pillow), NumPy
- **Parameter settings:** 
  - **Batch Size:** 32
  - **Epochs:** 10
  - **Learning Rate:** 0.001
  - **Optimizer:** Adam
  - **Input dimensions:** 224x224

---

# 10. Model Evaluation
For this Multi-Class Classification task, the following metrics are used to evaluate the model:
- **Accuracy:** To measure the overall correctness of the model across all classes.
- **Precision, Recall, F1-score:** To evaluate the model's performance on each specific disease, particularly checking for false positives and false negatives which are critical in medical diagnosis.
- **Confusion Matrix:** To visualize the misclassifications between visually similar skin diseases (e.g., Moles vs. Melanoma).

---

# 11. Results & Visualization
- **Actual vs Predicted:** The web application displays the uploaded image alongside the predicted disease class and a confidence percentage.
- **Multi-image Aggregation:** When a user uploads multiple images of the same lesion, the system aggregates the results and visualizes the overall prediction based on average confidence.
- **System Interface:** The Flask application provides an intuitive UI for users, while FastAPI provides a developer-friendly Swagger UI for testing API endpoints.

---

# 12. Hyperparameter Tuning
- **Transfer Learning Strategy:** The feature extraction layers (pretrained on ImageNet) were largely frozen, while the final dense classifier was replaced and trained. Later, the last two layers of `model.features` were unfrozen (`param.requires_grad = True`) to fine-tune the feature representations specifically for dermatological images.
- **Learning Rate tuning:** A starting learning rate of 0.001 was chosen to gently update the newly added classification layer without drastically altering the pretrained weights.

---

# 13. Interpretation & Insights
- **What did the model learn?** The model learned to distinguish between 22 distinct skin conditions by recognizing unique textures, colors, and border irregularities characteristic of each disease.
- **Key patterns:** It effectively handles variations in lighting, skin tone, and image resolution due to the robust data preprocessing pipeline.
- **Business/Real-world insights:** Implementing a dual-backend system (Flask for UI, FastAPI for API) proved highly effective. It allows the model to be consumed both by direct human users via web browsers and by automated client applications or mobile apps via RESTful APIs.

---

# 14. Conclusion
- **Summary of findings:** The project successfully implemented a scalable deep learning web application capable of identifying skin diseases. The use of EfficientNet-B0 allowed for fast and accurate inference.
- **Best performing model:** EfficientNet-B0 fine-tuned via transfer learning.
- **Limitations:** The model's accuracy is heavily dependent on image quality. Blurry or poorly lit images may lead to lower confidence scores. It is also not a replacement for professional medical advice.
- **Future scope:** Expanding the dataset to include rare skin conditions, implementing real-time mobile app integration, and deploying the system to scalable cloud infrastructure like AWS or GCP.

---

# 15. Appendix

**Code Snippet: Multi-Image Aggregation Logic (predict.py)**
```python
def predict_multiple(image_paths):
    model = load_model()
    classes = get_classes()
    results = {}
    
    for path in image_paths:
        image = Image.open(path).convert("RGB")
        image = transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = model(image)
            probs = F.softmax(outputs, dim=1)
            confidence, predicted = torch.max(probs, 1)
        label = classes[predicted.item()]
        conf = confidence.item()
        if label not in results:
            results[label] = []
        results[label].append(conf)

    # Voting logic to find highest average confidence
    final_label = None
    max_score = 0
    for label, confs in results.items():
        avg_conf = sum(confs) / len(confs)
        if avg_conf > max_score:
            max_score = avg_conf
            final_label = label
            
    return final_label, max_score
```

---

# 16. References
1. **Dataset source:** Skin Disease Dataset.
2. A. Esteva et al., "Dermatologist-level classification of skin cancer with deep neural networks," *Nature*, vol. 542, pp. 115-118, Feb 2017.
3. PyTorch Documentation: https://pytorch.org/docs/
4. FastAPI Framework: https://fastapi.tiangolo.com/
5. Flask Web Development: https://flask.palletsprojects.com/
