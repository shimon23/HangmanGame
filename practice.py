



def swap(a ,b):
    a ,b = b, a
    return a ,b

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':

    sentence = input("Please enter a string:")
    #sentence[1:].replace(sentence[0],"e")
    sentence[int(len(sentence)//2):].upper()
    print(sentence[:int(len(sentence)//2)]+sentence[int(len(sentence)//2):].upper())

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

print('"Shuffle, Shuffle, Shuffle"'+", say it together!\nChange colors and directions,\nDon't back down and stop the player!\tDo you want to play Taki?)        /tPress y\\")
