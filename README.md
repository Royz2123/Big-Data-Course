# Big-Data-Course
A collection of homework assignments from the Big Data course from Haifa University

## Overview
The following projects are python implementations of Big Data techniques using Data Coresets. The main idea is taking a huge amount of data, and compressing it into a smaller (core) set that represents it and has properties with regards to the original data.


## Examples
Here are a few examples of the many things we implemented in this course


### Epsilon sample
Here's an example you can find in HW2, that finds an e-sample of a set. The idea is taking a group of d dimensional points and breaking them down into (1/epsilon)^d representatives. This is used many times by more complex algorithms. Below is an example for d = 2:

Input Image:

![input image](https://github.com/Royz2123/Big-Data-Course/blob/master/HW2/images/input.png)


Output Image:

![input image](https://github.com/Royz2123/Big-Data-Course/blob/master/HW2/images/output.png)


Notice how the output still represents the points, and is spaced out accordingly.



### Alpha-Beta approximation for the K-Enclosing Squares problem
One of the uses for the epsilon sample is the example of K-enclosing squares. The idea is enclosing a set of points in a group of k squares, such that their "radius" is as small as possible. 
Since this is very difficult to acheive, we strive for a solution with Klogn squares. We will do this by reducing our data using an epsilon sample, and iteratively finding enclosing squares using exhasitve search. We get a total runtime of O(nlogndk).

Input Image:

![input image](https://github.com/Royz2123/Big-Data-Course/blob/master/HW2/images/q1b_input.png)


Output Image:

![input image](https://github.com/Royz2123/Big-Data-Course/blob/master/HW2/images/q1b_output.png)


Notice how there are a few centeres in the middle of the image, and there are more around the edges. This is because we first eliminate the big groups of points, and are left with the edge cases that need handling.



## Execution
Executing any project can be done by

```bash

python qX.py
```


