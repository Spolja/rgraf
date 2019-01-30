Image reckognition playground
start the program: 
  - python3 detect_shapes.py --image image.png   
  - python3 detect_shapes.py --image image.png -q

This project was made as an assignment for Visoka škola za informacijske tehnologije Zagreb - Računalna grafika class.

The project is defined as an geometry shape detector, which detects geometry shapes from given image file(.png).
Shape detector supports detection for shapes:

    -   Triangle (if the object has 3 edges it is classified as an triangle)
    -   Square (if the object has 4 edges, if the angles between the vertices are cca 90 deg and all vertices are approx the same length, the object is classified as an square)
    -   Rectangle (if the object has 4 edges, if the angles between the vertices are cca 90 deg, the object is classified as an rectangle)
    -   Pentagon (if the object has 5 edges, and all the vertices are approx the same length, the object is classified as an pentagon)
    -   Hexagon (if the object has 6 edges, and all the vertices are approx the same length, the object is classified as an hexagon)
    -   Heptagon (if the object has 7 edges, and all the vertices are approx the same length, the object is classified as an heptagon)
    -   Circle (if the object has more than 7 edges and all the points of the "circle" are at the same distance from the center of the circle, the object is classified as circle)
    
    
Flow of the program goes as below:

    1) load the image and resize it to a smaller factor so that the shapes can be approximated better 
    2) convert the resized image to grayscale, blur it slightly and threshold it
    3) find contours in the thresholded image and initialize the shape detector
    4) loop over the contours
    5) compute the center of the contour, then detect the name of the shape using only the contour
    6) detect the shape using the algorithm described above
    7) multiply the contour (x, y)-coordinates by the resize ratio, then draw the contours and the name of the shape on the image
    8) show the output image
