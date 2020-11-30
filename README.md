# Obtaining Picasso's bull transformations
**Author:** [Aneta Baloyan](https://www.linkedin.com/in/aneta-baloyan/)

**Institution:** [American University of Armenia](https://aua.am/)

**E-mail:** _aneta_baloyan@edu.aua.am_
***

This repository contains my final project for **_CS260 Image Processing_** course. 

In this project, I am going to use different image processing techniques (to be specified later) to obtain the transformations that Picasso obtained creating his famous [bull plates](https://www.widewalls.ch/magazine/pablo-picaso-bull-plates). In particular, I am going to work on two transitions: transition from plate **[3](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_3.jpg)** to **[4](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_4.jpg)** and transition from plate **[9](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_9.jpg)** to **[10](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Picasso-bull-plates/picasso_bull_plate_10.jpg)** (the final plate). 

You can find all the plates in the [_/Picasso-bull-plates_](https://github.com/AnetaBaloyan/image-processing-picasso-bull/tree/main/Picasso-bull-plates) directory.

***
## Content
* Transformation 3 to 4.
  * [Entry 1](https://github.com/AnetaBaloyan/image-processing-picasso-bull#entry-no1)
  * [Entry 2](https://github.com/AnetaBaloyan/image-processing-picasso-bull#entry-no2)
  * [Entry 3](https://github.com/AnetaBaloyan/image-processing-picasso-bull#entry-no3)
* Transformation 9 to 10.
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

***
***
## Entry No.2
<a href="https://www.codecogs.com/eqnedit.php?latex=Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" title="Transformation \text { } 3 \rightarrow4" /></a>

In this entry, I use the information obtained during Entry 1, and build on it to achieve the 3 -> 4 transformation. The process is described in a Power Point presentation [Entry-2.pptx](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Entry-2.pptx) (I know it's rough but it was convenient). All the steps are attached in the folder [/entry-2](https://github.com/AnetaBaloyan/image-processing-picasso-bull/tree/main/entry-2).
Here are some steps to the final result.

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_ellipse.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_4_elipse.jpg" width="400"/>

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_half_cut.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_half_cut_center_of_mass.jpg" width="400"/>

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_spine_and_central_ine.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_new_head.jpg" width="400"/> 

<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_final.jpg" width="400"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_4_no_ground.jpg" width="400"/> 

For the detailed explanation of each step, please refer to the [presentation](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Entry-2.pptx).

***
***
## Entry No.3
<a href="https://www.codecogs.com/eqnedit.php?latex=Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Transformation&space;\text&space;{&space;}&space;3&space;\rightarrow4" title="Transformation \text { } 3 \rightarrow4" /></a>

In this entry, I am further investigating the issue of the unexpected center of mass. 

* I use Python in this part to write my own function for calculating a **weighted center of mass** and change the vertical reference line to a more intuitive and naturally explainable one: the vertical line going through the midpoint of the **frontal and back legs**.
<img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-2/picasso_bull_plate_3_center_of_mass.jpg" width="400"/> <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F5%2F58%2FOcticons-arrow-small-right.svg%2F180px-Octicons-arrow-small-right.svg.png&f=1&nofb=1" width="40"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/entry-3/jpg/picasso_bull_plate_3_vertical_axis.jpg" width="400"/>

* Please see the Power Point presentation [Entry-3.pptx](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/Entry-3.pptx) for more detailed explanation.
* All the code can be found in [3-to-4-center-of-mass.py](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/3-to-4-center-of-mass.py) and [ImageHandler.py](https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/ImageHandler.py).
* All the intermediate steps can be found in the directory [/entry-3](https://github.com/AnetaBaloyan/image-processing-picasso-bull/tree/main/entry-3).

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.drodd.com%2Fimages14%2Fwhite6.png&f=1&nofb=1" width="200"/> <img src="https://github.com/AnetaBaloyan/image-processing-picasso-bull/blob/main/center-of-mass.gif" width="600"/>

***

### Thank you for your interest!



