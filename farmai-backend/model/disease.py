import numpy as np
import cv2
from io import BytesIO
from PIL import Image
from typing import Dict

# Mock model - replace with actual trained model
CLASS_NAMES = {
    0: 'Healthy',
    1: 'Powdery Mildew',
    2: 'Leaf Rust',
    3: 'Bacterial Blight',
    4: 'Leaf Spot'
}

TREATMENTS = {
    'Healthy': "No treatment needed. Maintain current practices.",
    'Powdery Mildew': "Apply sulfur-based fungicide. Improve air circulation.",
    'Leaf Rust': "Apply fungicide containing propiconazole. Remove infected leaves.",
    'Bacterial Blight': "Apply copper-based bactericide. Avoid overhead irrigation.",
    'Leaf Spot': "Apply chlorothalonil or mancozeb. Remove affected leaves."
}

def predict_disease(image_bytes: bytes) -> Dict:
    try:
        img = Image.open(BytesIO(image_bytes))
        img = np.array(img)
        
        if img.shape[-1] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
            
        img = cv2.resize(img, (256, 256))
        img = img / 255.0
        
        # Mock prediction - replace with actual model prediction
        mock_pred = [0.1, 0.7, 0.1, 0.05, 0.05]  # Example: 70% Powdery Mildew
        class_idx = np.argmax(mock_pred)
        confidence = float(mock_pred[class_idx])
        
        disease = CLASS_NAMES.get(class_idx, 'Unknown')
        
        return {
            "disease": disease,
            "confidence": confidence,
            "treatment": TREATMENTS.get(disease, "Consult local agricultural expert.")
        }
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")