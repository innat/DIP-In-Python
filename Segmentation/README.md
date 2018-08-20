
# Thresholding
---
**Ostu's Method** <a class="anchor" id="5-bullet"></a>

Thresholding is a very basic operation in image processing. Converting a greyscale image to monochrome is a common image processing task. And, a good algorithm always begins with a good basis! 

Otsu thresholding is a simple yet effective global automatic thresholding method for binarizing grayscale images such as foregrounds and backgrounds. In image processing, Otsu’s thresholding method (1979) is used for automatic **binarization** level decision, based on the shape of the **histogram**. It is based entirely on computation peformed on the histogram of an image.

The algorithm assumes that the image is composed of two basic classes: **Foreground** and **Background**. It then computes an optimal threshold value that minimizes the weighted within class variances of these two classes. 

Otsu threshold is used in many applications from medical imaging to low level computer vision. It's many advantages and assumptions.

---

**Mathematical Formulation**

In Otsu's method we comprehensively search for the threshold that minimizes the **intra-class variance** - the variance within the class which defined as a **weighted sum of variances of the two classes**:

\begin{align}
\sigma_w^2(t) & = w_0(t)\sigma_0^2(t) + w_1(t)\sigma_1^2(t)
\end{align}

Weights $W_0$ adn $W_1$ are the probabilities of the two classes separated by a threshold $t$ , and $\sigma_0^2(t)$ and $\sigma_1^2(t)$ are variances of these two classes. Mathematically probabilities of the two classes are defined as 

\begin{align}
w_0(t) & = \sum_{i=0}^{t-1} p(i) \\ 
w_1(t) & = \sum_{i=t}^{L-1} p(i)
\end{align}

Now, the Otsu's method involves the iterative fashion across all the possible threshold values and measuring the spread for the pixel levels for each side of the threshold or the pixels that either fall in background or foreground regions. The goal is to find the threshold value where the sum of the bacground and foreground spreads is at its minimum.

Let's demonstrate the process using the a simple 6:6 gray level image. The histogram for the image is drawn below. For simplification we choose only 6 levels grayscale.

<img src="hist.png", width = 200, height = 200>

Now, let's calculate for finding variacne which is the measure of spread for a single threshold. Let's assume, our threshold value is 3.

---

\begin{align}
\mu_0(t) & = \frac{\sum_{i=0}^{t-1}ip(i)}{w_0(t)} \\
\mu_1(t) & = \frac{\sum_{i=t}^{L-1}ip(i)}{w_1(t)}
\end{align}

\begin{align}
\sigma_b^2(t) & = \sigma^2(t) - \sigma_w^2(t) = w_0(\mu_0 - \mu_T)^2 + w_1(\mu_1 - \mu_T)^2 = w_0(t)w_1(t)\left[\mu_0(t) - \mu_1(t)\right]^2
\end{align}


\begin{align}
\mu_0(t) & = \frac{\sum_{i=0}^{t-1}ip(i)}{w_0(t)} \\
\mu_1(t) & = \frac{\sum_{i=t}^{L-1}ip(i)}{w_1(t)}
\end{align}



**Background**
<img src="img/back.png", width = 200, height = 200>





\begin{align}
Weight, \ \ \ \ W_0 &= \frac{10 + 8 + 6}{36} = 0.67 \\
Mean, \ \ \ \ \mu_0 &= \frac{[(0*10) + (1*8) + (2*6)]}{24} = 0.83 \\
Variance \ \ \ \sigma_0^2 &= \frac{[(0-0.83)^2*10 + (1-0.83)^2*8 + (2-0.83)^2*6]}{24} \\
&= \frac{6.89 + 0.23 + 8.21}{24} \\
&= 0.64
\end{align}

---

**Foreground**
<img src="img/fore.png", width = 200, height = 200>

\begin{align}
Weight, \ \ \ \ W_1 &= \frac{8 + 4 + 2}{36} = 0.39 \\
Mean, \ \ \ \ \mu_1 &= \frac{[(3x8) + (4x4) + (5x2)]}{14} = 3.57 \\
Variance \ \ \ \sigma_1^2 &= \frac{[(3-3.57)^2*8 + (4-3.57)^2*4 + (5-3.57)^2*2]}{14} \\
&= \frac{0.325*8 + 0.185*4 + 2.05*2}{14} \\
&= 0.53
\end{align}


The next step is to calculate the **`Within-Class Variance`**. This is simply the sum of the two variances multiplied by their associated weights.

\begin{align}
\sigma_w^2(t) & = w_0(t)\sigma_0^2(t) + w_1(t)\sigma_1^2(t) \\
&= 0.67*0.64 + 0.39*0.53 \\
&= 0.64
\end{align}

This value is the **sum of weighted of intra-class variance** for the threshold value 3. 

Otsu shows that minimizing the **intra-class variance** is the same as **maximizing inter-class variance**. Inter calss variance is mathematically defined as:

\begin{align}
\sigma_b^2(t) & = \sigma^2(t) - \sigma_w^2(t) \\
&= w_0(\mu_0 - \mu_T)^2 + w_1(\mu_1 - \mu_T)^2 = w_0(t)w_1(t)\left[\mu_0(t) - \mu_1(t)\right]^2
\end{align}

As previously we randomly choose threshold value 3, let's calculate inter-class variance for this threshold value.

\begin{align}
\sigma_b^2(t) = 0.67*0.39*[0.83-3.57]^2 = 1.96
\end{align}


This same calculation needs to be performed for all the possible threshold values 0 to 5, which is 0 to 255 for real gray level practical image. 

\begin{align}
Within \ Class \ Variance: \ \ \sigma_w^2(t) & = w_0(t)\sigma_0^2(t) + w_1(t)\sigma_1^2(t) \\
Between \ Class \ Variance: \ \ \sigma_b^2(t) & = w_0(t)w_1(t)\left[\mu_0(t) - \mu_1(t)\right]^2
\end{align}


---

**Algorithm**

If we incorporate a little math into that simple step-wise algorithm, such an explanation evolves:

- Compute histogram and probabilities of each intensity level.
- Set up initial $w_i$ and $\mu_i$.
- Step through from threshold `t = 0` to `t = L-1`:
    - update: $w_i$ and $\mu_i$
    - compute: $\sigma_b^2(t)$
- Desired threshold corresponds to the maximum value of $\sigma_b^2(t)$.


---


## KMeans Clustering <a class="anchor" id="6-bullet"></a>

k-means clustering is a method of [vector quantization](https://en.wikipedia.org/wiki/Vector_quantization), originally from signal processing, that is popular for [cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis) in [data mining](https://en.wikipedia.org/wiki/Data_mining). 

In Otsu thresholding, we found the threshold which minimised the intra-segment pixel variance. So, rather then looking for a threshold from an gray level image, we can look for clusters in colour space, and by doing so we end up with the K-means clustering technique.