import numpy as np
rgb_image= np.array( [[[123,200,98],
                      [34,90,200],
                       [255,100,50]],
                       [[60,180,75],
                        [90,45,210],
                        [200,200,200]],
                        [[10,10,10],
                        [250,250,100],
                        [80,120,160]]])

grayscale_image = np.mean(rgb_image, axis = 2)
print("Orginal RGB Image:\n", rgb_image)
print("\n Greyscale image: \n",grayscale_image)