## Image Data Analysis Using Python - Part 2

[Part 1](https://iphton.github.io/iphton.github.io/Up-&-Running-of-Image-Data-Analysis-Using-Numpy-&-OpenCV-Part-1/)

## Intensity Transformation

#### Image Negative <a class="anchor" id="1-bullet"></a>

The transformation function has been given below

`s = T ( r )`

where r is the pixels of the input image and s is the pixels of the output image. T is a transformation function that maps each value of r to each value of s.

negative transformation, which is invert of identity transformation. In negative transformation, each value of the input image is subtracted from the `L-1` and mapped onto the output image.

In this case the following transition has been done.

`s = (L – 1) – r`

So each value is subtracted by 255 and the result image has been shown below. So what happens is that, the lighter pixels become dark and the darker picture becomes light. And it results in image negative.



# Log transformation <a class="anchor" id="2-bullet"></a>

The log transformations can be defined by this formula

`s = c log(r + 1)`.

Where s and r are the pixel values of the output and the input image and c is a constant. The value 1 is added to each of the pixel value of the input image because if there is a pixel intensity of 0 in the image, then log (0) is equal to infinity. So 1 is added, to make the minimum value at least 1.

During log transformation, the dark pixels in an image are expanded as compare to the higher pixel values. The higher pixel values are kind of compressed in log transformation. This result in following image enhancement.

The value of c in the log transform adjust the kind of enhancement you are looking for.



# Gamma Correction <a class="anchor" id="3-bullet"></a>
 
Gamma correction, or often simply gamma, is a nonlinear operation used to encode and decode luminance or tristimulus values in video or still image systems. Gamma correction is also known as the Power Law Transform. First, our image pixel intensities must be scaled from the range [0, 255] to [0, 1.0]. From there, we obtain our output gamma corrected image by applying the following equation:

`V_out = V_in ^ (1 / G)`

Where V_in is our input image and G is our gamma value. The output image O is then scaled back to the range [0, 255].

A gamma value, G < 1 is sometimes called an `encoding gamma`, and the process of encoding with this compressive power-law nonlinearity is called `gamma compression`; Gamma values < 1 will shift the image towards the darker end of the spectrum.

Conversely a gamma value G > 1 is called a `decoding gamma` and the application of the expansive power-law nonlinearity is called `gamma expansion.` Gamma values > 1 will make the image appear lighter. A gamma value of G=1 will have no affect on the input image.
