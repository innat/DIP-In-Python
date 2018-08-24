
![autoen](https://user-images.githubusercontent.com/17668390/44370229-191ede00-a4fb-11e8-8b7c-ba2ff6fcfcce.png)

[Read](https://iphton.github.io/iphton.github.io/Image-Processing-in-Python-Part-2/#10-bullet) on blog in more details.

An **autoencoder** is the combination of an **encoder** function that converts the input data into a different representation and a **decoder** function that converts the new representation back into the original format. It's a data compression algorithm where the compression and decompression functions are 

- Data-specific, 
- Lossy, and 
- Learned automatically from **examples** rather than engineered by a human.

As it's data specific and lossy, it's not good for image compression in general. The fact that autoencoders are data-specific which makes them generally impractical for real-world data compression problems. But there's a hope, future advances might change this. I find it interesting, though it's not good enoguh and also very poor performance compared to othr compression algorithm like **JPEG**, **MPEG** etc. [Check out](https://blog.keras.io/building-autoencoders-in-keras.html) this **keras** blog post regarding on this issue.

And also fllowing, in case of you're interested too.

- [1](https://arxiv.org/abs/1802.09371)
- [2](https://arxiv.org/abs/1703.00395)
- [1](https://www.irisa.fr/temics/demos/visualization_ae/visualizationAE.htm)

**output:**

![out_auto](https://user-images.githubusercontent.com/17668390/44370248-3653ac80-a4fb-11e8-8174-f9e9a7e453b1.JPG)
