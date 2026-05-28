# WEEK 3 TASKS — Semantic Segmentation

## Run YOLO Segmentation

```python
from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

results = model.predict(
    source="Week1/frames_30fps",
    save=True
)
```

Output folder:

```
runs/segment/predict/
```

---

## Convert segmented images → video

```bash
ffmpeg -framerate 30 -i runs/segment/predict/frame_%04d.jpg -c:v libx264 segmented_video.mp4
```

---

## Stack 3 videos vertically (Raw + Detect + Segment)

```bash
ffmpeg -i raw.mp4 -i detected.mp4 -i segmented.mp4 \
-filter_complex "[0:v][1:v][2:v]vstack=inputs=3" \
-an stacked_output.mp4
```

Add new music:

```bash
ffmpeg -i stacked_output.mp4 -i music.mp3 -c:v copy -c:a aac final_stacked.mp4
```

---
