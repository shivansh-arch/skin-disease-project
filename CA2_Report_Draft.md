**Deep Learning-Based Web Application for Multi-Image Skin Disease Classification**

**Author 1 Name**  
*Dept. of Computer Science*  
*University/Organization*  
City, Country  
email address or ORCID  

*Abstract*—**Early and accurate detection of skin diseases is critical for effective treatment and patient care. This paper presents a comprehensive web-based system for the automated classification of skin diseases using deep learning techniques. The proposed system integrates a robust machine learning model with both Flask and FastAPI backends, enabling scalable, real-time, multi-image processing. The application accepts image uploads, preprocesses the data, and returns disease predictions along with confidence scores. This paper details the system architecture, data preprocessing pipeline, and backend API design, demonstrating an accessible and efficient approach to automated dermatological diagnosis.**

*Keywords*—**Skin Disease Classification, Deep Learning, Convolutional Neural Networks, FastAPI, Flask, Image Processing**

I. INTRODUCTION
The accurate diagnosis of skin diseases relies heavily on visual inspection, which can be subjective and requires significant dermatological expertise. With the rapid advancement of computer vision and deep learning, automated image classification has emerged as a powerful tool to assist medical professionals. This project introduces a self-contained, web-based application designed to classify skin diseases from uploaded images. 

The primary contribution of this work is the development of a dual-interface web application (utilizing both Flask for user-facing interactions and FastAPI for high-performance backend routing) that seamlessly integrates a trained deep learning model. The system is capable of processing single and multiple image uploads simultaneously, providing rapid predictions and confidence metrics to the end user. The source code for this project is publicly available on GitHub at: https://github.com/shivansh-arch/skin-disease-project.

II. PROPOSED SYSTEM ARCHITECTURE
The architecture of the proposed system is divided into three main components: data preprocessing, the predictive modeling engine, and the web application programming interfaces (APIs).

*A. Data Preprocessing*
Before an image can be passed to the deep learning model, it must undergo standardized preprocessing to ensure consistency. As implemented in the `src/data/preprocess.py` module, incoming images are resized, normalized, and transformed into the appropriate tensor formats required by the model. This step is critical for maintaining high inference accuracy regardless of the original image source or resolution.

*B. Predictive Modeling Engine*
The core of the system is the classification model (`src/models/model.py` and `predict.py`). The model takes the preprocessed image data and extracts hierarchical visual features to determine the probability of various skin conditions. The inference engine is optimized to calculate both the predicted label and a confidence percentage, which provides transparency to the user regarding the model's certainty.

*C. Web Application Interfaces*
To ensure the model is accessible, two distinct backends were developed:
1) *Flask Application (`flask_app.py`):* Serves as the primary user interface, rendering HTML templates and handling form-based multi-file uploads directly from a web browser.
2) *FastAPI Application (`app/main.py` & `app/routes.py`):* Provides a modern, asynchronous RESTful API. This allows for high-throughput automated requests, returning structured JSON responses containing predictions, confidence scores, and the number of files processed.

III. EXPERIMENTAL SETUP
*A. Implementation Details*
The system is implemented in Python, utilizing standard machine learning libraries for model inference. The backend relies on `uvicorn` to serve the FastAPI application and the built-in Flask development server for the UI component. Uploaded files are temporarily stored in a `temp/` directory during processing and cleared post-inference to optimize storage.

*B. Testing and Validation*
Extensive unit testing was implemented to validate system components. Scripts such as `test_preprocessing.py`, `test_predict.py`, and `test_multi_upload.py` ensure that the data pipeline correctly transforms images and that the API endpoints handle concurrent file uploads without data loss or timeouts.

IV. RESULTS AND DISCUSSION
Preliminary testing of the API endpoints demonstrates that the system effectively processes multi-image payloads. When a user submits an array of images, the system successfully iterates through the files, saves them to the temporary directory, and executes the `predict_multiple` function. The resulting JSON response accurately reflects the aggregated predictions and confidence scores, proving the system's viability for real-world deployment.

V. CONCLUSION AND FUTURE WORK
This paper detailed the structure and implementation of a deep learning-based skin disease classification web application. By combining robust image preprocessing with dual FastAPI and Flask backends, the system provides a scalable solution for automated dermatological screening. Future work will focus on expanding the dataset to improve model accuracy across a wider array of rare skin conditions and deploying the application to a cloud infrastructure for public access.

ACKNOWLEDGMENT
The authors would like to thank their instructors and peers for their guidance and feedback during the development of this Continuous Assessment (CA2) project.

REFERENCES
[1] A. Esteva et al., "Dermatologist-level classification of skin cancer with deep neural networks," *Nature*, vol. 542, pp. 115-118, Feb 2017.
[2] "FastAPI framework, high performance, easy to learn, fast to code, ready for production," FastAPI. [Online]. Available: https://fastapi.tiangolo.com/
[3] "Flask: Web development, one drop at a time," Pallets Projects. [Online]. Available: https://flask.palletsprojects.com/
