
## [Image Data Analysis Using Python - Part 1](https://www.linkedin.com/pulse/basic-image-data-analysis-using-numpy-opencv-part-1-mohammed-innat/?published=t)

Computer store images as a mosaic of tiny squares. This is like the ancient art form of tile mosaic, or the melting bead kits kids play with today. Now, if these square tiles are too big, it’s then hard to make smooth edges and curves. The more and smaller tiles we use, the smoother or as we say less pixelated, image will be. These sometimes gets referred to as resolution of the images.

Vector graphics are somewhat different method of storing images that aims to avoid pixel related issues. But even vector images, in the end, are displayed as a mosaic of pixels. The word pixel means a picture element. A simple way to describe each pixel is using a combination of three colors, namely Red, Green, Blue. This is what we call an RGB image.

In an RGB image, each pixel is represented by three 8 bit numbers associated to the values for Red, Green, Blue respectively. Eventually using a magnifying glass, if we zoom a picture, we’ll see the picture is made up of tiny dots of little light or more specifically the pixels and what more interesting is to see that those tiny dots of little light are actually multiple tiny dots of little light of different colors which are nothing but Red, Green, Blue channels.

Pixel together from far away, create an image and upfront they’re just little lights that are ON and OFF. The combination of those create images and basically what we see on screen every single day.

![rig_gif](https://user-images.githubusercontent.com/17668390/44360736-95a2c400-a4dd-11e8-9a6c-37f8db15b6ab.gif)

Every photograph, in digital form, is made up of pixels. They are the smallest unit of information that makes up a picture. Usually round or square, they are typically arranged in a 2-dimensional grid.

Now, if all three values are at full intensity, that means they’re 255, it then shows as white and if all three colors are muted, or has the value of 0, the color shows as black. The combination of these three will, in turn, give us a specific shade of the pixel color. Since each number is an `8-bit` number, the values range from `0-255`.

Combination of these three color will posses tends to the highest value among them. Since each value can have 256 different intensity or brightness value, it makes 16.8 million total shades.

### Table of Contents : Part 1

- Importing images and observe it’s properties
- Splitting the layers
- Greyscale
- Using Logical Operator on pixel values
- Masking using Logical Operator
- Satellite Image Data Analysis

---

## Image Data Analysis Using Python - Part 2

Following contents are the reflection of my completed academic image processing course in previous term. So, I am not planning on putting anything into production sphere. Instead the aim of this article is to try and realize the fundamentals of a few basic image processing techniques. For this reason, I am going to stick to using `SciKit-Image` - `numpy` mainly to preform most of the manipulations, although I will use other libraries now and then rather than using most wanted tools like `OpenCV`.


![ab](https://user-images.githubusercontent.com/17668390/44361038-807a6500-a4de-11e8-9245-bc990304367a.JPG)


### Table of Contents : Part 2

- Intensity Transformation
    - Basic Function
        - Image Negative
        - Log Transformation
        - Gamma Correction

- Convolution
    - Convolving Procedure 
    - Implementation and Use Cases

- Segmentation
    - Thresholding
        - Ostu's Method
        - KMeans Clustering
    - Object Detection
        - Line Detection
            - Hough transform
        - Edge Detection
            - Cany Edge Detection

- Vectorization
    - Contour tracking

- Image Compression
    - Stacked Autoencoder


