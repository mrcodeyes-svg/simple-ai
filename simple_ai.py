import random

# 1. The Training Data (Input 1, Input 2)
X = [[0, 0], [0, 1], [1, 0], [1, 1], [0,0],[1,1],[1,0],[0,1]]

# 2. The Targets (The correct answers)
y = [0, 0, 1, 1,0,1,1,0]

# 3. Start with random internal numbers (weights)
weight_1 = 0.15
weight_2 = 0.30

# 4. Set the step size (Learning Rate)
learning_rate = 0.1

# 5. The Training Loop (Run 100 times)
# This trains the AI completely before we ever test it
for epoch in range(100):
    for i in range(len(X)):
        input_1 = X[i][0]
        input_2 = X[i][1]
        target = y[i]

        # Make a guess
        prediction = (input_1 * weight_1) + (input_2 * weight_2)

        # Reverted fix: Simple error subtraction tells the AI the direction to move
        error = target - prediction

        # Adjust the weights
        weight_1 += error * input_1 * learning_rate
        weight_2 += error * input_2 * learning_rate
        learning_rate = abs(weight_1 - weight_2) + 0.1
        print(f"learning rate {learning_rate}, weight 1: {weight_1}, weight 2: {weight_2}")

# 6. Test the trained AI on a new scenario
test_1 = random.randint(0, 10000000000)
test_2 = 0

# The AI makes its final prediction using the stable weights
final_prediction = (test_1 * weight_1) + (test_2 * weight_2)
error2 = test_1 - final_prediction

print(f"Test Input: {test_1}")
print(f"AI Prediction: {final_prediction:.4f}")
print(f"The final error is: {error2:.4f}")
print(f"Final Stable Weights -> Weight 1: {weight_1:.2f}, Weight 2: {weight_2:.2f}")
