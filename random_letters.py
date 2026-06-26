import random
import threading

chars = "abcdefghijklmnopkrstuvwxyz1234567890!@#$%^&*() "

def target():
    with open('letters.txt', 'w', encoding='utf-8') as f:
        run = 0
        f.write(str1)

str1 = ''
run = 0
while True:
    run += 1
    ran = random.choice(chars)
    str1 += ran
    print(str1)
    if run > 1000:
        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()