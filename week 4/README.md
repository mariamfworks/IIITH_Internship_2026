# WEEK 4 TASKS — YOLO DATASET UNDERSTANDING

## What YAML file contains

Example `dataset.yaml`:

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: person
  1: car
  2: bicycle
```

### YOLO label format

Each image has a `.txt` file:

```
class x_center y_center width height
```

(all normalized 0–1)

---

## Create Custom Dataset using Label Studio

### Install label-studio (separate venv)

```bash
python3 -m venv label_env
source label_env/bin/activate
pip install label-studio
label-studio start
```

---

## Dataset Creation Steps (IMPORTANT)

1. Extract 600 images (10 fps from 1-min video)

```bash
ffmpeg -i custom_video.mp4 -vf fps=10 custom_frames/frame_%04d.jpg
```

2. Split dataset

```
100 → train
40 → val
rest → test
```

3. Label train + val using Label Studio

4. Create files:

```
dataset.yaml
train.txt
val.txt
labels/
images/
```

---
