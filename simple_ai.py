# 1. The Training Data (Input 1, Input 2)
X = [[0, 0], [0, 1], [1, 0], [1, 1], [0,0], [1,1], [1,0], [0,1]]

# 2. The Targets (The correct answers)
y = [0, 1, 1, 2, 0, 2, 1, 1]

# 3. Start with random internal numbers (weights)
weight_1 = 0.15
weight_2 = 0.30

# 4. Set the step size (Learning Rate)
learning_rate = 0.1

# 5. The Training Loop (Run 100 times)
# This trains the AI completely before we ever test it
for epoch in range(10000):
    for i in range(len(X)):
        input_1 = X[i][0]
        input_2 = X[i][1]
        target = y[i]

        # Make a guess
        prediction1 = (input_1 * weight_1) + (input_2 * weight_2)

        # Reverted fix: Simple error subtraction tells the AI the direction to move
        error = target - prediction1

        # Adjust the weights
        weight_1 += error * input_1 * learning_rate
        weight_2 += error * input_2 * learning_rate
        learning_rate = abs(weight_1 - weight_2) + 0.01

        print(f"learning rate {learning_rate}, weight 1: {weight_1}, weight 2: {weight_2}")

def test(test_1, test_2):
    # The AI makes its final prediction using the stable weights
    final_prediction, final_prediction2 = (test_1 * weight_1), (test_2 * weight_2)
    error2 = test_1 - final_prediction
    return final_prediction, final_prediction2, error2

word = input("what is your word? ")
word_list = []
final_word = ''
list_word = list(word)
pos = []

i = 0
while i < len(list_word):
    try:
        if i in pos:
            pass
        elif not i in pos:
            total = ord(list_word[i])
            pos.append(i)

        i += 1
        total2 = ord(list_word[i])
        pos.append(i)
    except IndexError:
        pass
    # 6. Test the trained AI on a new scenario
    test_1 = total
    test_2 = total2
    final_prediction, final_prediction2, error2 =  test(test_1, test_2)
    word_list.append(final_prediction)
    word_list.append(final_prediction2)
    print(f"Test Input: {test_1}")
    print(f"Test Input: {test_2}")
    print(f"AI 1st Prediction: {final_prediction}")
    print(f"AI 2nd Prediction: {final_prediction2}")
    print(f"The final error is: {error2}")
    print(f"Final Stable Weights -> Weight 1: {weight_1}, Weight 2: {weight_2}")
    print()
    i += 1

print(word_list)

for i in word_list:
    final_word += chr(round(i))

print(f'the ai list "{word_list}"')
print(f'final ai word "{final_word}"')
print(f'Are the two words the same {final_word == word}')
print()