# Particle Filter



- [Particle Filter](#particle-filter)
    - [Process](#process)
        - [Initializtion](#initializtion)
        - [Predict](#predict)
        - [Update](#update)
        - [Resampling](#resampling)
        - [New Particles](#new-particles)



## Process
![](./img/flowchart.png)
![](./img/pseudocode.png)
![](./img/particle_sum.png)




### Initializtion
- At the initialization step we estimate our position from GPS input. The subsequent steps in the process will refine this estimate to localize our vehicle.

### Predict
- During the prediction step we add the control input (yaw rate & velocity) for all particles
- predict equations when yaw rate is not zero
    - ![](./img/predict_equations.png)
  
### Update
- During the update step, we update our particle weights using map landmark positions and feature measurements.
- to map coordinate
    - ![](./img/transformation.png)
- cal new weight for observations of each particle
    - ![](./img/cal_new_weight_0.png)
    - for each observations
        - ![](./img/cal_new_weight.png)
- cal error of weight
    - ![](./img/error.png)

### Resampling
- During resampling we will resample M times (M is range of 0 to length_of_particleArray) drawing a particle i (i is the particle index) proportional to its weight. 
    - resampling wheel
        - ![](./img/resampling_wheel.jpg)

### New Particles
- The new set of particles represents the Bayes filter posterior probability. We now have a refined estimate of the vehicles position based on input evidence.