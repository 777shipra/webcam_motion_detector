# <---------WEBCAM MOTION DETECTOR---------->

#### DESCRIPTION

A PROGRAM THAT DETECTS MOVING OBJECTS IN THE DESKTOP VIDEO FRAME AND RECORDS THE TIME OF THE OBJECT ENTERING OR LEAVING THE WEBCAM FRAME
SIMULTANEOUSLY A GRAPH WITH BE PLOTTED SHOWING THE RECORDED TIME OF THE MOVING OBJECT
APPLICATION IS MADE FROM SCRATCH WITH PYTHON

#### WORKING/BASE OF THE PROJECT

 NOTE:- code is not explained here .it is in the file
 
 The program will open the webcam and will capture or form multiple frames as follows:-
 
 1) the first frame / background / first picture will be captured as soon as the webcam will open  and stored it in a variable . this first frame will act as the base picture to detect the difference of the next frames formed . It will be static just used to compare other images
 ![base picture]()
 2) the base picture will be converted into a grey scale image 
 3) then an object/animal will appear , then convert this frame too into grey scale image
 ![object frame]()
 4) Now we have two grey scale images to check the object we will do the difference of both the grey scale image , known as the delta frame
 ![delta frame]()
 notice that behind the human u will see the lamp in the room , the python script is making the difference of the two grey scale images to check the moving object 
 the picture is a grey scale image where every pixel of the image has it's own intensity value . the black area of the image shows there is no motion and in place of the object (human) there is high intensity showing there is alot of motion . some other white areas are seen that depicts the light in the room
 5) THRESHOLD FRAME :- THIS IS TO FORM THE FINAL FRAME , the code says for this frame the convert into white where the value of the pixel is above 1000 (high intensity) to difference out the moving object . so you come up with the outline of the object/contours
 ![threshold frame]()
 contours are the white patches  in the frame . to remove the small contours along the object(biggest contour/human) we will write code that will remove the contours from the frame by setting the size ( if size == something , keep else remove )
 
 then we will make a rectangle around the biggest contour / moving object . 
 
