#include <cmath>
#include <cstddef>
#include <iostream>
#include <vector>

//make some data so we can return a value
struct data {
    float weight1;
    float weight2;
    float learning_rate;
};

//compile into c
extern "C" {
    //make a loop with epochs the weights and the two inputs and the thing we are looking for use data so we can return a value
    data loop(int epochs, float weight1, float weight2, std::vector<std::vector<int>> inputs, std::vector<int> ans, float learning_rate) {
        //train for the amount of epoches given
        for (int epoch = 0; epoch < epochs; epoch++) {
            //loop through inputs
            for (size_t i = 0; i < inputs.size(); i++) {
                //the vars
                int input1 = inputs[i][0]; 
                int input2 = inputs[i][1];
                int target = ans[i];

                //make a guess
                float prediction = (input1 * weight1) + (input2 * weight2);
                //subtract the target and the prediction for the error
                float error = target - prediction;
                //change the weights based on the error, inputs, and learning rate
                weight1 += error * input1 * learning_rate;
                weight2 += error * input2 * learning_rate;
                //change the learning rate based off of the two weights and a fixed number
                learning_rate = std::abs(weight1 - weight2) + 0.5;
                //print the learning rate and the two weights
                std::cout << "learning rate "  << learning_rate << ", weight 1: " << weight1 << ", weight 2: " << weight2 << std::endl;
            };
        };
        //return the values
        return {weight1, weight2, learning_rate};
    };
};
int main() {
    std::vector<std::vector<int>> x = {{0, 0}, {0, 1}, {1, 0}, {1, 1}, {0, 0}, {1, 1}, {1, 0}, {0, 1}};
    std::vector<int> y = {0,1,1,2,0,2,1,1};
    loop(25, 0.15, 0.30, x, y, 0.1);
}