# Week 5: Custom Model Training & Inference

## Overview
This phase demonstrates the complete workflow:
**Data Scaling → Model Training → Performance Evaluation → Inference Deployment**

---

## 1. Data Preprocessing (Scaling)

### Objective
Optimize training efficiency by reducing image size while preserving annotation accuracy.

### Method
All images were resized to a width of **384 pixels**, maintaining aspect ratio to ensure bounding box labels remain valid.

### Command Used
```bash
for i in *.jpg; do 
    ffmpeg -i "$i" -vf scale=384:-1 "scaled_$i"; 
done
```

### Output
- Scaled images saved as: `scaled_*.jpg`
- Reduced memory usage and faster training
- No changes required for `.txt` label files

---

## 2. Model Training

### Objective
Train a custom object detection model using the scaled dataset.

### Configuration
- **Framework:** Ultralytics YOLO
- **Base Model:** `yolov26-custom.pt` (pre-trained)
- **Image Size:** 384
- **Epochs:** 50
- **Dataset Config:** `dataset.yaml`

### Training Script
```python
from ultralytics import YOLO

# Load pre-trained model
model = YOLO('yolov26-custom.pt')

# Train model
model.train(
    data='dataset.yaml',
    epochs=50,
    imgsz=384,
    plots=True
)
```

### Output
- Training logs stored in: `runs/detect/train/`
- Generated files:
  - `results.png`
  - `confusion_matrix.png`
  - `weights/best.pt`
  - `weights/last.pt`

---

## 3. Performance Analysis

### Objective
Evaluate model performance and detect overfitting/underfitting.

### Metrics Monitored
- Training Loss
- Validation Loss
- Precision
- Recall
- mAP (Mean Average Precision)

### Output Files
- `results.png` → Training performance graph
- `confusion_matrix.png` → Class-wise evaluation

### Observations
- **Best Epoch:** [Insert your value]
- Stable validation loss observed
- No major overfitting detected

---

## 4. Inference & Testing

### Objective
Run predictions on unseen test data using trained weights.

### Inference Script
```python
from ultralytics import YOLO

# Load trained model
model = YOLO('runs/detect/train/weights/best.pt')

# Run inference
results = model.predict(
    source='datasets/test/images',
    save=True
)
```

### Output
- Predicted images saved in: `runs/detect/predict/`
- Images contain bounding boxes and confidence scores

---

## 5. Final Video Integration

### Objective
Combine outputs into a single comparative visualization.

### Command Used
```bash
ffmpeg -i raw.mp4 -i detect.mp4 -i segment.mp4 \
-filter_complex "[0:v][1:v][2:v]vstack=inputs=3" \
-an final_demo.mp4
```

### Output
- `final_demo.mp4` showing:
  - Raw video
  - Detection results
  - Segmentation results

---

## 6. Project Structure

```
Week_05/
│── README.md
│── dataset.yaml
│── weights/
│   └── best.pt
│── outputs/
│   ├── results.png
│   ├── confusion_matrix.png
│   └── final_demo.mp4
```

---

## 7. Key Takeaways

- High-quality annotations directly improve model accuracy
- Image scaling reduces training time significantly
- Successfully built an end-to-end ML pipeline
- Model outputs can be used for real-time automation systems

---
