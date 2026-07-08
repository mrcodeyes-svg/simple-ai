import ctypes as ct

#the data that the ai is trained on
X = [[0, 0], [0, 1], [1, 0], [1, 1], [0,0], [1,1], [1,0], [0,1]]

# the right answers
y = [0, 1, 1, 2, 0, 2, 1, 1]

#rows and cols of x
rows = len(X)
cols = 2

#the data for c++
class data2(ct.Structure):
    _fields_ = [
        ("weight1", ct.c_float),
        ("weight2", ct.c_float)
    ]

#the weights for the ai 
weight_1 = 0.15
weight_2 = 0.30

#the learning rate for the ai
learning_rate = 0.1 

#get the loop from c++
loop = ct.CDLL(r'C:\Users\mrcod\Downloads\code\simple_ai\loop.dll')

#the arg for c++
loop.loop.argtypes = [
    ct.c_int,                         
    ct.c_float,                       
    ct.c_float,                       
    ct.c_int,                         
    ct.POINTER(ct.POINTER(ct.c_int)), 
    ct.POINTER(ct.c_int),             
    ct.c_float                        
]

#define epochs
epochs = 25
#make row allocations
row_all = [(ct.c_int * cols)(*row) for row in X]
#make a pointer
pointer = ct.POINTER(ct.c_int) * rows
inputs = pointer()

#load the mem for the rows
for i, row2 in enumerate(row_all):
    inputs[i] = ct.cast(row2, ct.POINTER(ct.c_int))

#make the ans for c++ to read
ans = (ct.c_int * rows)(*y)

#the data c++ needs
loop.loop.restype = data2
data_final = loop.loop(ct.c_int(epochs), ct.c_float(weight_1), ct.c_float(weight_2), rows, inputs, ans, ct.c_float(learning_rate))

#make weight 1 and 2 the new ones
weight_1 = data_final.weight1
weight_2 = data_final.weight2

#define the test so we can use it over and over again and let the function take different tests as inputs
def test(test_1, test_2):
    #the ai makes a guess based on the tests
    final_prediction  = test_1 * weight_1
    #see if test 2 is none if it's not then we do the normal math with a error calc that uses test 2 and 1
    if not test_2 is None:
        final_prediction2 = test_2 * weight_2
        error2 = abs((test_1 - final_prediction) + (test_2 - final_prediction2))
    #if it is then we set it to none and use a different kind of error calc
    else:
        final_prediction2 = None
        error2 = test_1 - final_prediction
    #find the error of the predictions
    
    #return the values
    return final_prediction, final_prediction2, error2

#get the user's word 
word = input(" what is your word? ")
#start the word list as a empty list
word_list = []
#start the final word as a empty string
final_word = ''
#make the users's word into a list so it can be put through the ord function
list_word = list(word)
#track the pos of the letters that we have already used
pos = []

#start the 'i' var as 0 so we can use it in the while loop and to track the letter we are at
i = 0
#a while loop that goes through the word list 
while i < len(list_word):
    #we try to see if 'i' is in the pos list,
    #we also try to add 1 to 'i', 
    #and we try to give total 2 the ord value of the list word with 'i' as the input 
    #but if we get a index error we set total 2 to none and pass to the next thing
    try:
        #if 'i' is in pos we pass and skip this
        if i in pos:
            pass
        #else if it is not then we give total the value of ord with list word passed into ord,
        #and then we append 'i' to pos
        elif not i in pos:
            total = ord(list_word[i])
            pos.append(i)
        
        #we try to add 1 to 'i',
        #and then we try to use ord with list word passed into it,
        #then we append 'i' to pos
        i += 1
        total2 = ord(list_word[i])
        pos.append(i)
    except IndexError:
        total2 = None
        pass
    #test the ai on the two tests 
    test_1 = total
    test_2 = total2
    #we call on test we the two tests as the pass in so we can get the vars final prediction 1 and 2 and we also get the error 
    #we then append final prediction 1 and 2 to word list
    final_prediction, final_prediction2, error2 = test(test_1, test_2)
    word_list.append(final_prediction)
    word_list.append(final_prediction2)
    #we print all of the outputs as a kind of debuging thing and use \n to make a new line
    print(f" Test Input 1: {test_1} \nTest Input 2: {test_2} \n AI 1st Prediction: {final_prediction} \n AI 2nd Prediction: {final_prediction2} \n The final error is: {error2} \n Final Weights: Weight 1: {weight_1}, Weight 2: {weight_2}\n")
    #add 1 to 'i' to keep the loop going 
    i += 1

#for each thing in word list it checks if it is none if it is then it removes it if it's not then it rounds 'i' and use chr
for i in word_list:
    if not i is None:
        final_word += chr(round(i))
    else:
        word_list.remove(i)

#all the final lists and words 
print(f' this is your word: "{word}"')
print(f' the ai list: {word_list}')
print(f' final ai word: "{final_word}"')
#find if final word is word and if it is then it makes ans yes if not then it makes it no
if final_word == word:
    ans = 'yes'
else:
    ans = 'no'
#prints the ans
print(f" Are the two words the same? {ans} \n")