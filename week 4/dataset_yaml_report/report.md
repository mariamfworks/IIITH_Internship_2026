# Custom Dataset & YAML Explanation

This dataset was created using Label Studio.

Dataset contains:
- 2 classes → person, car
- Images labeled manually using bounding boxes

YOLO label format:
<class_id> <x_center> <y_center> <width> <height>

Values are normalized between 0 and 1.

dataset.yaml contains:
- dataset path
- train and validation split
- class names mapping
