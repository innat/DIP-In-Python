Canny Edge Detectoin
----------------------

This repository contains an **educational** implementation of the Canny Edge Detector in Python 3x.

A multi-stage edge detection operation capable of detecting wide range of edges in images. Now, the Process of Canny edge detection algorithm can be broken down to 5 different steps:

1. Apply Gaussian Filter
2. Find the intensity gradients
3. Apply non-maximum suppression 
4. Apply double threshold
5. Track edge by hysteresis.


**Usage**
-----
A demo pic is provided, namely `r.jpg`. Download this repo. Operate CMD on that directory and run following command.

`python detector.py r.jpg 1.4 20 40`

**Expected Output:**

![canny](https://user-images.githubusercontent.com/17668390/44365545-fb964800-a4eb-11e8-8e23-81f49ef517fe.png)
