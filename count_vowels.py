if __name__ == '__main__':
    inputString = "petl is a general purpose Python package."
    vowels = ['a', 'e', 'o', 'u', 'i']
    # filter vowels then count
    print(len(filter(lambda x: x in vowels, inputString)))
    # sum of array[0,1,0,0...]
    print(sum(map(lambda x: x in vowels, inputString)))
