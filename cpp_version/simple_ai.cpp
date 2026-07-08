#include <cstddef>
#include <iostream>
#include <cmath>
#include <vector>

//a struct to return some data
struct tests {
    float final_prediction;
    float final_prediction2;
    float error2;
};

//make a function that we can call later
tests test(int test1, int test2, float weight1, float weight2) {
    //the ai make a guess based on the tests
    float final_prediction = test1 * weight1;
    //define final_prediction2
    float final_prediction2 = NULL;
    //define error2
    float error2 = NULL;

    //see if test_2 is null
    if (test2 != NULL) {
        float final_prediction2 = test2 * weight2;
        float error2 = std::abs((test1 - final_prediction) + (test2 - final_prediction2));
    }
    else {
        float final_prediction2 = NULL;
        float error2 = test1 - final_prediction;
    }
    //return all the values
    return {final_prediction, final_prediction2, error2};
}

//the main function
int main() {
    //the data the ai is trained on
    std::vector<std::vector<int>> X = {{0, 0}, {0, 1}, {1, 0}, {1, 1}, {0,0}, {1,1}, {1,0}, {0,1}};

    //the right answers
    std::vector<int> y = {0, 1, 1, 2, 0, 2, 1, 1};

    //the weights
    float weight1 = 0.15;
    float weight2 = 0.30;

    //the learning rate for the ai
    float learning_rate = 0.1;

    //the loop for traning
    for (int epoch = 0; epoch < 25; epoch++) {
        //the loop through X
        for (size_t i = 0; i < X.size(); i++) {
            //the vars for the loop
            int input1 = X[i][0];
            int input2 = X[i][1];
            int target = y[i];

            //make a guess
            float prediction = (input1 * weight1) + (input2 * weight2);
            //find the error from the target and the guess being subtracted
            float error = target - prediction;
            //change the weights based on the error
            weight1 += error * input1 * learning_rate;
            weight2 += error * input2 * learning_rate;
            //change the learing rate based off of the two weights and add a fixed number
            learning_rate = std::abs(weight1 - weight2) + 0.5;
            //print everything
            std::cout << "learning rate " << learning_rate << ", weight 1: " << weight1 << ", weight 2: " << weight2 << std::endl;
        }
    }
    //get user input
}