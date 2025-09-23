import random
 #สุ่มตัวเลขจำนวนเต็ม 
def test_random():
    #สร้างตัวแปร random_numberตัวแปรคือการสุ่มตัวเลขตั้งแต่ 1-10
    random_number = random.randint(1, 100)   #ประกาศตัวแปร
    print(random_number)
    guess_number = int(input("what is your guess number"))
    if  random_number  == guess_number:
        print("Congratulation")

    elif random_number  < guess_number:
        print("Too hight")

    elif  random_number > guess_number:
        print("Too low")  

#print(random_number)
     
test_random()