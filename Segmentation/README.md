
[Read](https://innat.github.io/innat.github.io/Image-Processing-in-Python-Part-2/#5-bullet) on blog in more details.

**Ostu's Method** <a class="anchor" id="5-bullet"></a>

Thresholding is a very basic operation in image processing. Converting a greyscale image to monochrome is a common image processing task. And, a good algorithm always begins with a good basis! 

Otsu thresholding is a simple yet effective global automatic thresholding method for binarizing grayscale images such as foregrounds and backgrounds. In image processing, Otsu’s thresholding method (1979) is used for automatic **binarization** level decision, based on the shape of the **histogram**. It is based entirely on computation peformed on the histogram of an image.

The algorithm assumes that the image is composed of two basic classes: **Foreground** and **Background**. It then computes an optimal threshold value that minimizes the weighted within class variances of these two classes. 

Otsu threshold is used in many applications from medical imaging to low level computer vision. It's many advantages and assumptions.

Otsu shows that minimizing the **intra-class variance** is the same as **maximizing inter-class variance**. Inter calss variance is mathematically defined as:


**Algorithm**

If we incorporate a little math into that simple step-wise algorithm, such an explanation evolves:

- Compute histogram and probabilities of each intensity level.
- Set up initial w_i and mu_i.
- Step through from threshold `t = 0` to `t = L-1`:
    - update: w_i and mu_i
    - compute: sigma_b^2(t)
- Desired threshold corresponds to the maximum value of sigma_b^2(t).


---


## KMeans Clustering <a class="anchor" id="6-bullet"></a>

k-means clustering is a method of [vector quantization](https://en.wikipedia.org/wiki/Vector_quantization), originally from signal processing, that is popular for [cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis) in [data mining](https://en.wikipedia.org/wiki/Data_mining). 

In Otsu thresholding, we found the threshold which minimised the intra-segment pixel variance. So, rather then looking for a threshold from an gray level image, we can look for clusters in colour space, and by doing so we end up with the K-means clustering technique.
