import calendar


def swap(a ,b):
    a, b = b, a
    return a, b


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def distance(num1, num2, num3):
    return abs(num1-num2) ==1 or abs(num1-num3) == 1

def shift_left(list):
    return (list+list)[1:len(list)+1]


def  format_list(list):
    list[-1]="and "
    pairindex = list[::2]
    #pairindex[-1] = "and "+pairindex[-1]
    pair_with_coma = ",".join(pairindex[-1])+", and" +pairindex[-1]
    return ",".join(pairindex[:-1])+", and " +pairindex[-1]


def last_early(my_str):
    contain = my_str[:-1]
    return contain.count(my_str[-1])>0

def longest(my_list):
    return max(list1,key = len)

def numbers_letters_count(my_str):
    numbers = 0
    chars = 0
    for str in my_str:
        if(str.isnumeric()):
            numbers+=1
        else:
            chars+=1
    print("[ ",numbers,", ",chars," ]")

def sequence_del(my_str):
    ans = ""
    for char in my_str:
        if char not in ans:
            ans+=char

    print(ans)

# def shopping_list(str_items):
#     list_item = list(str_items.split(","))
#     print(list_item)
#     user_input =int(input(""))
#     while()




if __name__ == '__main__':
    # pol_word = input("put a word that you think is a palindrome:")
    # temp = pol_word.replace(" ", "").upper()
    # revers_temp = temp[::-1]
    # #print(revers_temp)
    # if(temp==revers_temp):
    #     print("OK")
    # else:
    #     print("NOT")
    #shopping_list("Milk,Cottage,Tomatoes")
    sequence_del("ssshhhiimmon")
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    numbers_letters_count("Python 3.6.3")
    print(longest(list1))
    brother = ["shimon","osher","shir","ema"]
    print(format_list(brother))
    print(distance(1,5,3))
    print( last_early("rmy_str"))

    x = [1, 2, 3, 4]
    print(shift_left(x))
    temperature = input("Insert the temperature you would like to convert:")
    if temperature[-1] == "F" or temperature[-1] == "f":

       ans = ((int(temperature[:-1])*5)-160)/9
       print(temperature[:-1],ans,"C")
    else:
        ans = ((int(temperature[:-1])*9+160)/5)
        print(ans,"F")


    date =input("Enter a date:")
    print(int(date[6:]),int(date[3:5]),int(date[:2]))
    print(calendar.calendar.weekday(int(date[6:]),int(date[3:5]),int(date[:2])))
    # sentence = input("Please enter a string:")
    # #sentence[1:].replace(sentence[0],"e")
    # sentence[int(len(sentence)//2):].upper()
    # print(sentence[:int(len(sentence)//2)]+sentence[int(len(sentence)//2):].upper())

    # x = "x"as
    # y= "6"
    # z=int(y)+2
    # boolY =bool(y)
    # print(z)
    # UserInput = input("Enter three digits (each digit for one pig):")
    # nuberOfbrik=int(UserInput[0])+int(UserInput[1])+int(UserInput[2])
    # print(nuberOfbrik)
    # print(int(nuberOfbrik/3))
    # print(nuberOfbrik%3)3

# print('"Shuffle, Shuffle, Shuffle"'+", say it together!\nChange colors and directions,\nDon't back down and stop the player!\tDo you want to play Taki?)        /tPress y\\")
