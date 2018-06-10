
"""
Image Data Analysis Using Numpy & OpenCV

author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""



# Importing Image
if __name__ == '__main__':
    import imageio
    import matplotlib.pyplot as plt
    %matplotlib inline

    pic = imageio.imread('F:/demo_2.jpg')
    plt.figure(figsize = (15,15))

    plt.imshow(pic)

    print('Type of the image : ' , type(pic))
	print()
	print('Shape of the image : {}'.format(pic.shape))
	print('Image Hight {}'.format(pic.shape[0]))
	print('Image Width {}'.format(pic.shape[1]))
	print('Dimension of Image {}'.format(pic.ndim))

	print('Image size {}'.format(pic.size))

	print('Maximum RGB value in this image {}'.format(pic.max()))
	print('Minimum RGB value in this image {}'.format(pic.min()))

'''
Let's pick a specific pixel located at 100 th Rows and 50 th Column. 
And view the RGB value gradually. 
'''
	pic[ 100, 50 ]

	# A specific pixel located at Row : 100 ; Column : 50 
    # Each channel's value of it, gradually R , G , B
	print('Value of only R channel {}'.format(pic[ 100, 50, 0]))
	print('Value of only G channel {}'.format(pic[ 100, 50, 1]))
	print('Value of only B channel {}'.format(pic[ 100, 50, 2]))

    # let's take a quick view of each channels in the whole image.

	plt.title('R channel')
	plt.ylabel('Height {}'.format(pic.shape[0]))
	plt.xlabel('Width {}'.format(pic.shape[1]))

	plt.imshow(pic[ : , : , 0])
	plt.show()

	plt.title('G channel')
	plt.ylabel('Height {}'.format(pic.shape[0]))
	plt.xlabel('Width {}'.format(pic.shape[1]))

	plt.imshow(pic[ : , : , 1])
	plt.show()

	plt.title('B channel')
	plt.ylabel('Height {}'.format(pic.shape[0]))
	plt.xlabel('Width {}'.format(pic.shape[1]))

	plt.imshow(pic[ : , : , 2])
	plt.show()



# ------------------------------------------------------

'''

Now, here we can also able to change the number of RGB values. As an example, let's set the Red, Green, Blue layer for following Rows values to full intensity.

R channel: Row- 50 to 150
G channel: Row- 200 to 300
B channel: Row- 350 to 450
We'll load the image once, so that we can visualize each change simultaneously.

'''

pic = imageio.imread('F:/demo_2.jpg')

pic[50:150 , : , 0] = 255 # full intensity to those pixel's R channel
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()


pic[200:300 , : , 1] = 255 # full intensity to those pixel's G channel
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()

pic[350:450 , : , 2] = 255 # full intensity to those pixel's B channel
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()

# To make it more clear let's change the column section and this time 
# we'll change the RGB channel simultaneously

# set value 200 of all channels to those pixels which turns them to white
pic[ 50:450 , 400:600 , [0,1,2] ] = 200 
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()




