

[Read](https://iphton.github.io/iphton.github.io/Image-Processing-in-Python-Part-2/#4-bullet) on blog in more details.

# Convolution <a class="anchor" id="4-bullet"></a>

We've discussed briefly in previous [article](https://iphton.github.io/iphton.github.io/Up-&-Running-of-Image-Data-Analysis-Using-Numpy-&-OpenCV-Part-1/) that, when a computer sees an image, it sees an array of pixel values. Now, Depending on the resolution and size of the image, it will see a 32 x 32 x 3 array of numbers where the 3 refers to RGB values or channels. Just to drive home the point, let's say we have a color image in PNG form and its size is 480 x 480. The representative array will be 480 x 480 x 3. Each of these numbers is given a value from 0 to 255 which describes the pixel intensity at that point. 

Like we mentioned before, the input is a 32 x 32 x 3 array of pixel values. Now, the best way to explain a convolution is to imagine a flashlight that is shining over the top left of the image. Let’s say that the flashlight shines covers a 3 x 3 area. And now, let’s imagine this flashlight sliding across all the areas of the input image. In machine learning terms, this flashlight is called a **filter** or  **kernel** or sometimes refer to as **weights** or **mux** and the region that it is shining over is called the **receptive field**.

Now this filter is also an array of numbers where the numbers are called weights or parameters. A very important note is that the depth of this filter has to be the same as the depth of the input, so the dimensions of this filter is 3 x 3 x 3. 

An image **kernel** or **filter** is a small matrix used to apply effects like the ones we might find in Photoshop or Gimp, such as blurring, sharpening, outlining or embossing. They're also used in machine learning for `feature extraction`, a technique for determining the most important portions of an image. For more, have a look at Gimp's excellent documentation on using [Image kernel's](https://docs.gimp.org/en/plug-in-convmatrix.html). We can find a list of most common kernels [here](https://en.wikipedia.org/wiki/Kernel_(image_processing))

Now, let’s take the filter to the top left corner. As the filter is sliding, or **convolving**, around the input image, it is multiplying the values in the filter with the original pixel values of the image (aka computing element wise multiplications). These multiplications are all summed up. So now we have a single number. Remember, this number is just representative of when the filter is at the top left of the image. Now, we repeat this process for every location on the input volume. Next step would be moving the filter to the right by **stride** or **step** 1 unit, then right again by **stride** 1, and so on. Every unique location on the input volume produces a number. We can also choose stride or the step size 2 or more, but we have to carefull wheter it will fit or not on the input image. 

![convoving](https://user-images.githubusercontent.com/17668390/44360200-f4673e00-a4db-11e8-9422-f39e0693ba05.gif)

After sliding the filter over all the locations, we will find out that, what we’re left with is a 30 x 30 x 1 array of numbers, which we call an **activation map** or **feature map**. The reason we get a 30 x 30 array is that there are 900 different locations that a 3 x 3 filter can fit on a 32 x 32 input image. These 900 numbers are mapped to a 30 x 30 array. 

Let's say we've a following $3x3$ filter, convolving on a $5x5$ matri and according to the equation we should get a $3x3$ matrix, technically called **activation map** or **feature map**.

![conv_gif](https://user-images.githubusercontent.com/17668390/44360222-05b04a80-a4dc-11e8-8c57-48b7d2c96fd2.gif)

Moreover, we practically use more filters instead of one. Then our output volume would be `28 x 28 x n` (where n is the number of **activation map**). By using more filters, we are able to preserve the spatial dimensions better. 

However, For the pixels on the border of image matrix, some elements of the kernel might stands out of the image matrix and therefore does not have any corresponding element from the image matrix. In this case, we can eliminate the convolution operation for these position which end up an output matrix smaller than the input or we can apply **padding** to the input matrix 
