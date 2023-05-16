# Thai Rice Grading DNN

## TODO:
* Add description of the projects.
* Add Development steps
* Add Wiki



# Process List:
* Gather Images
* Camera and Image Callibration
* Auto Tagging & Image Processing
* Model Training
* Application Development


## Calibration
### Description
Calibrate the images to make it consistent among all cameras and most image angles.
### Input
```bash
├── images/
│   ├── camera1/
│   │   ├── calibration_params.txt  # output
│   │   ├── rice_5/
│   │   │   ├── *.png
...
│   ├── camera2/
...
```
### Output
```bash
├── calibrated_images/
│   ├── rice_5/
│   │   ├── *.png
...
```


## Semi-Auto Tagging
### Description
Tag image class automatically via YOLO.
### Input
```bash
├── calibrated_images/
│   ├── rice_5/
│   │   ├── *.png
...
```
### Output
```bash
├── calibrated_images/
│   │   ├── rice_5/
│   │   │   ├── *.png
│   │   │   ├── *.txt  # (tags/labels in YOLO format)
...
```


## Model Training
### Description
Tag image class automatically via YOLO.
### Input
```bash
├── calibrated_images/
│   │   ├── rice_5/
│   │   │   ├── *.png
│   │   │   ├── *.txt  # (tags/labels in YOLO format)
...
```
other yolo inputs
Train/test/validate params


### Output
*.weights



## Application Development
### Description
The app must be able to do camera callibration for each camera/device.
### Input
```bash
*.weights
```
...

### Output
*.weights

### Main Components
1. Image input (via camera or image folder)
2. Camera Callibration
3. Image Processing (including distortion correction)
4. YOLO Model

### UI for displaying
1. An input image
2. An undistorted Image
3. A predicted image and results
4. Other info for Debugging purpose (statistics, time)
