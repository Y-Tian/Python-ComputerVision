# OpenCV
Hack the North Project:

Implemented OpenCV to detect facial features from a live video source.

Capturing and reading a live video feed from a generic webcam (640x480) and having the webcam follow and point a laser beam at the
moving face.

Process: Have two stepper motors attached to an Arduino and are controlled by the .py main file through command terminal.

The center of the webcam is (320, 240) as shown in the diagram:

https://user-images.githubusercontent.com/28987070/30516429-1e6935d4-9b0d-11e7-8028-e5af9d82a747.png

Now, the issue was determining where the vertex on the rectangles were:

https://user-images.githubusercontent.com/28987070/30516431-207cc6ba-9b0d-11e7-9f80-da367574111f.png

Finally, to find the piece-wise functions for the direction of the motors:

Variables: C = center of the camera's viewpoint, X = x-axis, Y = y-axis

If conditions:

Cx - X < 0, Horizontal motor turns clockwise
Cx - X > 0, Horizontal motor turns counter-clockwise
Cy - Y < 0, Vertical motor turns counter-clockwise
Cy - Y > 0, Vertical motor turns clockwise

