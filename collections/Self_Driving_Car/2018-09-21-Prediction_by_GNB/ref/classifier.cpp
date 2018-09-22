#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include "classifier.h"


using namespace std;
using Eigen::ArrayXd;

/**
 * Initializes GNB
 */
GNB::GNB() {
    left_means = ArrayXd(4);
	left_means << 0,0,0,0;
	
    left_sds = ArrayXd(4);
    left_sds << 0,0,0,0;
    
    left_prior = 0;
    
    keep_means = ArrayXd(4);
	keep_means << 0,0,0,0;
	
	keep_sds = ArrayXd(4);
	keep_sds << 0,0,0,0;
	
	keep_prior = 0;
	
	right_means = ArrayXd(4);
	right_means << 0,0,0,0;
	
	right_sds = ArrayXd(4);
	right_sds << 0,0,0,0;
	
	right_prior = 0;
	
}

GNB::~GNB() {}

void GNB::train(vector<vector<double>> data, vector<string> labels)
{

	/*
		Trains the classifier with N data points and labels.

		INPUTS
		data - array of N observations
		  - Each observation is a tuple with 4 values: s, d, 
		    s_dot and d_dot.
		  - Example : [
			  	[3.5, 0.1, 5.9, -0.02],
			  	[8.0, -0.3, 3.0, 2.2],
			  	...
		  	]

		labels - array of N labels
		  - Each label is one of "left", "keep", or "right".
	*/
	
	//For each label, compute ArrayXd of means, one for each data class (s, d, s_dot, d_dot).
	//These will be used later to provide distributions for conditional probabilites.
	//Means are stored in an ArrayXd of size 4.
	
	float left_size = 0;
	float keep_size = 0;
	float right_size = 0;
	
    //For each label, compute the numerators of the means for each class
    //and the total number of data points given with that label.
	for (int i=0; i<labels.size(); i++){
	    if (labels[i] == "left"){
	        left_means += ArrayXd::Map(data[i].data(), data[i].size()); //conversion of data[i] to ArrayXd
	        left_size += 1;
	    } 
	    else if (labels[i] == "keep") {
	        keep_means += ArrayXd::Map(data[i].data(), data[i].size());
	        keep_size += 1;
	    } else if (labels[i] == "right") {
	        right_means += ArrayXd::Map(data[i].data(), data[i].size());
	        right_size += 1;
	    }
	}

	
	//Compute the means. Each result is a ArrayXd of means (4 means, one for each class)..
	left_means = left_means/left_size;
    keep_means = keep_means/keep_size;
	right_means = right_means/right_size;

	
	//Begin computation of standard deviations for each class/label combination.
	ArrayXd data_point;
	
	//Compute numerators of the standard deviations.
	for (int i=0; i<labels.size(); i++){
	    data_point = ArrayXd::Map(data[i].data(), data[i].size());
	    if (labels[i] == "left"){
	        left_sds += (data_point - left_means)*(data_point - left_means);
	    } else if (labels[i] == "keep") {
	        keep_sds += (data_point - keep_means)*(data_point - keep_means);
	    } else if (labels[i] == "right") {
	        right_sds += (data_point - right_means)*(data_point - right_means);
	    }
	}
	
	//compute standard deviations
	left_sds = (left_sds/left_size).sqrt();
    keep_sds = (keep_sds/keep_size).sqrt();
    right_sds = (right_sds/right_size).sqrt();
    
    //Compute the probability of each label
	left_prior = left_size/labels.size();
	keep_prior = keep_size/labels.size();
	right_prior = right_size/labels.size();
}

string GNB::predict(vector<double> sample)
{
	/*
		Once trained, this method is called and expected to return 
		a predicted behavior for the given observation.

		INPUTS

		observation - a 4 tuple with s, d, s_dot, d_dot.
		  - Example: [3.5, 0.1, 8.5, -0.2]

		OUTPUT

		A label representing the best guess of the classifier. Can
		be one of "left", "keep" or "right".
		"""
		# TODO - complete this
	*/
	
	//Calculate product of conditional probabilities for each label.
	double left_p = 1.0;
	double keep_p = 1.0;
	double right_p = 1.0; 
	for (int i=0; i<4; i++){
	    left_p *= (1.0/sqrt(2.0 * M_PI * pow(left_sds[i], 2))) * exp(-0.5*pow(sample[i] - left_means[i], 2)/pow(left_sds[i], 2));
	    keep_p *= (1.0/sqrt(2.0 * M_PI * pow(keep_sds[i], 2))) * exp(-0.5*pow(sample[i] - keep_means[i], 2)/pow(keep_sds[i], 2));
	    right_p *= (1.0/sqrt(2.0 * M_PI * pow(right_sds[i], 2))) * exp(-0.5*pow(sample[i] - right_means[i], 2)/pow(right_sds[i], 2));
	}

	
	//Multiply each by the prior
	left_p *= left_prior;
	keep_p *= keep_prior;
	right_p *= right_prior;
    
    double probs[3] = {left_p, keep_p, right_p};
    double max = left_p;
    double max_index = 0;
    for (int i=1; i<3; i++){
        if (probs[i] > max) {
            max = probs[i];
            max_index = i;
        }
    }
	
	return this -> possible_labels[max_index];

}