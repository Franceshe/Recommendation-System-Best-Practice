# Using matrix factorization to learn user and movie embeddings.


## Tensorflow Core:
* tf.gather_nd
.... side notes: It is elegent way to acess atonmic numbers in matrix. Which could solved many dirty hancks
for my early robotics project...Wish to know this feature earlier.
... Robotics community and ROS SHOULD CONSIDER UTILIZE SUCH PROPERTY. :)
* tf.keras.losses.MSE


## Tensorflow hacks:
* [CPU incompatibility issue solved](https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-that-this-tensorflow-binary-was-not-compiled-to-u)
* [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)
* [Multiply–accumulate operation](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply.E2.80.93add):which speed up linear algebra computation, namely dot-product, matrix multiply, convolution, etc.
