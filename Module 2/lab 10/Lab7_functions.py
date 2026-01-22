def Welcoming_Message(name):
    print(f"Welcome, {name}")

def Words_connector(word1, word2):
    connected_words = word1 + " " + word2
    return connected_words

def Min_and_Max(nums):
    return(min(nums), max(nums))

def Key_Power_Value(n):
    d={}
    for i in range(1, n+1):
        d[i] = i**2
    print(d)
def Connect_Strings(*args):
    result = ', '.join(args)
    return result

