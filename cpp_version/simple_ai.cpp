#include <cstddef>
#include <iostream>
#include <cmath>
#include <ostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdexcept>

//a custom function that acts like python's if x in y
bool find(const std::vector<int>& list, int thing) {
    return std::find(list.begin(), list.end(), thing) != list.end();
}

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
    float final_prediction2;
    //define error2
    float error2;

    //see if test_2 is 0
    if (test2 != 0) {
        final_prediction2 = test2 * weight2;
        error2 = std::abs((test1 - final_prediction) + (test2 - final_prediction2));
    }
    else {
        final_prediction2 = 0.0f;
        error2 = test1 - final_prediction;
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
    std::string input;
    std::cout << "what is your word ";
    std::cin >> input;
    //start the word list as a empty list
    std::vector<float> word_list;
    //start the final word as a empty string
    std::string final_word;
    //make the users's word into a list so we can turn it into numbers
    std::vector<char> list_word(input.begin(), input.end());
    //track the pos of the letters that have been used already
    std::vector<int> pos;

    //start the 'i' var as 0 so we can use it in the loop
    size_t i2 = 0;
    //define the 2 totals so we can use them
    int total; int total2;
    //a while loop that goes through the word_list
    while (i2 < list_word.size()) {
        //we try to see if 'i' is in the pos list,
        //we also try to add 1 to 'i', 
        //and we try to give total 2 the ord value of the list word with 'i' as the input 
        //but if we get a index error we set total 2 to none and pass to the next thing
        try {
            char letter = list_word.at(i2);
            //if 'i' is in pos we pass and skip thisk
            if (find(pos, i2)) {
                
            }
            //else if it is not then we give total the value of ord with list word passed into ord,
            //and then we append 'i' to pos
            else if (!find(pos, i2)) {
                total = letter;
                pos.push_back(i2);
            }

            //we try to add 1 to 'i',
            //and then we try to use ord with list word passed into it,
            //then we append 'i' to pos
            i2++;
            letter = list_word.at(i2);
            total2 = letter;
            pos.push_back(i2);
        }
        catch (const std::out_of_range& w) {
            total2 = 0;
        }
        
        //test the ai on the 2 totals
        //we call on the test function and get final prediction 1 and 2 and we also get error2
        //we then append final prediction 1 and 2 to word list
        tests data = test(total, total2, weight1, weight2);
        float final_prediction = data.final_prediction;
        float final_prediction2 = data.final_prediction2;
        float error2 = data.error2;
        //now append
        word_list.push_back(final_prediction); if (final_prediction2 != 0.0f) { word_list.push_back(final_prediction2);}

        //print all the data that we got
        std::cout << "Test Input 1: " << total << "\nTest Input 2: " << total2 << "\nAI's 1st Prediction: " << final_prediction << "\nAI's 2nd Prediction: " << final_prediction2 << "\nThe final error is: " << error2 << "\n Final Weights: Weight 1: " << weight1 << ", Weight 2: " << weight2 << "\n" << std::endl;
        //add 1 to 'i' to keep it going
        i2++;
    };

    //use std::erase to get rid of all 0.0f
    std::erase(word_list, 0.0f);
    //for each thing in word list it checks if it is none if it is then it removes it if it's not then it rounds 'i' and use chr
    for (float i = 0; i < word_list.size(); i++) {
        float item = word_list[i];
        if (item != 0.0f) {
            char letter = std::round(item);
            final_word += letter;
        }
    }

    //all the data we have gotten 
    std::cout << "this is you word: " << input << std::endl;
    //use a for loop to print the list
    for (float item : word_list) {
        std::cout << item << " ";
    }
    //use a if statement to make it say yes or no
    std::string ans;
    if (final_word == input) {ans = "yes";} else {ans = "no";}
    std::cout << "\nfinal ai word: " << final_word << "\nare the two words the same " << ans << "\n" << std::endl;
}