
## **Katna**: Tool for automating common video keyframe extraction and Image Autocrop tasks

### Resources 
* Homepage and Reference: <https://keplervaani.com/katna/>

### Description
Katna automates the boring, error prone task of videos key/best frames extraction and manual time consuming task of image cropping.

Katna is divided into two modules namely video and image.

Video Module:
-------------
This module handles the task(s) related to key frame extraction.

Key-frames are defined as the representative frames of a video stream, the frames that provide the most accurate and compact summary of the video content.

**Frame extraction and selection criteria**

1. Frame that are sufficiently different from previous ones using absolute differences in LUV colorspace
2. Brightness score filtering of extracted frames
3. Entropy/contrast score filtering of extracted frames
4. K-Means Clustering of frames using image histogram
5. Selection of best frame from clusters based on and variance of laplacian (image blur detection)

Image Module:
-------------
This module handles the task(s) related to smart cropping.

The Smart image cropping is happening in way that the module identifies the best part or the area where someone focus more
and interprets this information while cropping the image.

**Crop extraction and selection criteria**

1. Edge, saliency and Face detection features are detected in the input image
2. All the crops with specified dimensions are extracted with calculation of score for each crop wrt to extracted features
3. The crops will be passes through filters specified which will remove the crops which filter rejects

**Supported Video and image file formats**
##########################################

All the major video formats like .mp4,.mov,.avi etc and image formats like .jpg, .png, .jpeg etc are supported. 

More selection features are in developement pipeline

###  How to install

#### Using pypi
1) Install Python 3 
2) pip install katna

#### Install from source

1) Install git
2) Install Anaconda or Miniconda Python
3) Open terminal 
4) Clone repo from here https://github.com/keplerlab/Katna.git 
5) Change the directory to the directory where you have cloned your repo 
    ```
    $cd path_to_the_folder_repo_cloned
    ```
6) Create a new anaconda environment if you are using anaconda python distribution
    ```
    conda create --name katna python=3
    source activate katna
    ```

7) Run the setup:
    ``` 
    python setup.py install 
    ```    
#### Error handling and tips 
1) If you see "AttributeError: module 'cv2.cv2' has no attribute 'saliency'" error. Uninstall opencv-contrib
by running command "python -m pip uninstall opencv-contrib-python" and then again install it by running command "python -m pip install opencv-contrib-python"

2) If you see "FileNotFoundError: frozen_east_text_detection.pb file not found". Open python shell and follow below commands.
    a) from Katna.image_filters.text_detector import TextDetector
    b) td = TextDetector()
    c) td.download()
 
### How to use Library

1) Refer to quickstart section in Katna Reference 
   from https://keplervaani.com/katna/tutorials.html

### Attributions
1) We have used the SAD (Sum of absolute difference) code from https://github.com/amanwalia92/KeyFramesExtraction  
2) Smart crop feature in Katna Image module is inspired and enhanced from Smartcrop.js by Jonas Wagner https://github.com/jwagner/smartcrop.js/ 