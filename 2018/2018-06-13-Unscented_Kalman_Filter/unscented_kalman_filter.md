# Unscented Kalman Filter

- [Unscented Kalman Filter](#unscented-kalman-filter)
    - [CTRV](#ctrv)
    - [predict](#predict)
        - [Generate Sigma Points](#generate-sigma-points)
        - [Predict Sigma Points](#predict-sigma-points)
        - [Predict Mean and Covariance](#predict-mean-and-covariance)
    - [Update](#update)
        - [Predict Measurement](#predict-measurement)
        - [Update State](#update-state)
    - [UKF in Lidar and Radar](#ukf-in-lidar-and-radar)






## CTRV
- process  
![](./img/ctrv.png)
- add noise  
![](./img/process.png)



## predict

### Generate Sigma Points
![](./img/generate_sigma_points.png)
- gen sigmas  
![](./img/gen_sigmas.png)
- how to choose sigmas  
![](./img/choose_sigmas.png)


### Predict Sigma Points
![](./img/predict_sigma_points.png)
- by x(k+1) = x(k) + x_dot(k) + noise(k)  
![](./img/process_sigmas.png)

### Predict Mean and Covariance
![](./img/predict_mean_covariance.png)  
- predict equations  
![](./img/predict_mean_cov_equations.png)





## Update

### Predict Measurement
![](./img/predict_measurement.png)
- choose sigmas (augmented -> predcted -> measurement)  
![](./img/existed_sigmas.png)
- gen sigmas  
![](./img/gen_measurements_sigmas.png)
- predict means and covariance  
![](./img/predict_measurements_mean_cov.png)


### Update State
![](./img/update_state.png)
- combine predictions and measurements  
![](./img/combine_pred_meas.png)
- update equations  
![](./img/update_equations.png)
- NIS  
![](./img/NIS.png)
- Result  
![](./img/result.png)






## UKF in Lidar and Radar
- init
    - init by lidar
        - set x by sensor x
        - set y by sensor y
    - or init by radar
        - set x by rho,theta
        - set y by rho,theta
        - set v by rho_dot? better or worse? 
- predict
    - Augmented Sigma Points
    - predict sigma points
    - predict mean and convariance 
- update lidar by kalman filter
    - update mean and convariance 
    - cal NIS
- or update radar by unscented kalman filter
    - predict radar sigma points
    - update mean and convariance 
    - cal NIS