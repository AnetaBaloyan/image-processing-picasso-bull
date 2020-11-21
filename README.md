# Obtaining Picasso's bull transformations
**Author:** [Aneta Baloyan](https://www.linkedin.com/in/aneta-baloyan/)

**Institution:** [American University of Armenia](https://aua.am/)

**E-mail:** _aneta_baloyan@edu.aua.am_
***

This repository contains my final project for **_CS260 Image Processing_** course. 

In this project, I am going to use different image processing techniques (to be specified later) to obtain the transformations that Picasso obtained creating his famous [bull plates](https://www.widewalls.ch/magazine/pablo-picaso-bull-plates). In particular, I am going to work on two transitions: transition from plate **[3](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_3.jpg)** to **[4](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_4.jpg)** and transition from plate **[9](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_9.jpg)** to **[10](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_10.jpg)** (the final plate). 

You can find all the plates in the [_/Picasso-bull-plates_](https://github.com/AnetaBaloyan/image-processing-picasso-bull/tree/main/Picasso-bull-plates) directory.


***
## Entry No.1
<a href="https://www.codecogs.com/eqnedit.php?latex=Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" title="Transformation \text { } 3 \rightarrow4" /></a>

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_3.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_4.jpg" width="400"/> 

                                            _(a)_                                                                                             _(b)_

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/3-to-4-steps-ImageJ/picasso_bull_plate_3_step_2.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/3-to-4-steps-ImageJ/picasso_bull_plate_4_step_2.jpg" width="400"/> 
                                            _(c)_                                                                                             _(d)_
                                            
<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/3-to-4-steps-ImageJ/picasso_bull_plate_4_step_3.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/3-to-4-steps-python/overlay.jpg" width="400"/> 
                                            _(e)_                                                                                             _(f)_

**1. Firstly, I tried using _ImageJ_ to experiment with the plates and try out some ideas.** 

* Although ImageJ was meant to ease this proccess, I had trouble finding the tools I need and, at the end of the day, it took me longer to obtain the results I wanted. 
* However, it was useful when trying to experiment with edge detection and various filters.  
* Most of my trials with edge detection led to failures. I wanted to detect the white lines that are visible in pictures _(a)_ and _(b)_. You can see from pictures _(c)_ and _(d)_ that there is a lot of noise and many small spots are also detected. Although, _(c)_ and _(d)_ are results of a very quick experimentation, my further trials with different filters, such as minimum, maximum, gaussian, mean, etc. and adjustments of brightness and contrast did not lead anywhere satisfactory enough.
* Nevertheless, I noticed some attributes of the two plates, and realized that several regions are directly removed from the first plate. It is most visible in the lower back part, where some fraction of the back and the tail is cut out. 
* I tried to overlay the two edge detections and check this assumption. You can see the result in picture _(e)_.
* My further experimentations via **ImageJ** were unproductive.

**2. Then, I decided to switch to _Python_ and _OpenCV_ for more agile experimentations.**
* I repeated the overlay but this time I just performed the operation with the non-edge-detected grayscale images.
* I realized that there is a slight shift in the plates as the lines appeared a little off. Indeed, the first image was shifted 3 pixels to the right and upward. 
* After the correction, I got the result in picture _(f)_, where the two plates are precisely overlayed.
* From picture _(f)_, where the plate 3 appears in 0.3 opacity and plate 4 appears in 0.7, you can observe that, indeed, the second plate has some areas simply removed.









