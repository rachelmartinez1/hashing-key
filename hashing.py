#Hashing Program
#Rachel Martinez
import sys


def menu():
    sentence = []
    sentence = input("Enter a sentence to be hashed (or enter 0 to quit): ").lower()
    if sentence == '0':
        sys.exit(0)
    else:
        return sentence

def computeSentence(sentence):
    sentenceSum = 0
    nums = []
    for c in sentence:
        if c == ' ':
            continue
        if c.isalpha():
            nums.append(ord(c) - 96)
        else:
            print("Enter an alphabetical sentence without symbols/numbers.")
            main()

    for c in nums:
        sentenceSum += c

    return nums, sentenceSum

def printVals(nums, sentenceSum):
    # print(nums)
    # print("Sentence Sum: " + str(sentenceSum))
    print("Key value: " + str(sentenceSum % 31))
    main()


def main():
    sentence = menu()
    nums, sentenceSum = computeSentence(sentence)
    printVals(nums, sentenceSum)

if __name__ == "__main__":
    main()
