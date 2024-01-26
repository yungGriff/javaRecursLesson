import random

def reverse(loi):
    return loi[::-1]
def DealingDuplicates(loi1, loi2):
    return list(set(loi1) & set(loi2))
def fibo(start, duration):
    seq = []
    if duration > 1:
        seq.append(start)
        seq.append(start)
        i = 0
        while (duration - i) > 1:
            nextSeq = seq[i] + seq[i + 1]
            seq.append(nextSeq)
            i += 1
    else:
        seq.append(start)
    return seq[-1]
def augmenter(input_dictionary):
    aug_dict = {}
    random_values = {}
    for letter, number in input_dictionary.items():
        aug_number = number + 10
        random_value = random.randrange(1, 10)
        fibo_result = fibo(aug_number, random_value)
        aug_dict[letter] = fibo_result
        random_values[letter] = random_value
    return aug_dict, random_values

def decoder(aug_dict, random_values):
    decoded_dict = {}
    for letter, fibo_result in aug_dict.items():
        random_value = random_values[letter]
        decoded_number = fibo_result - random_value
        decoded_dict[letter] = decoded_number
    return decoded_dict





alphanumeric = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}



result_dict, random_values = augmenter(alphanumeric)

print("Original Dictionary:", alphanumeric)
print("Augmented Dictionary:", result_dict)

decoded_dict = decoder(result_dict, random_values)
print("Decoded Dictionary: ", decoded_dict)

# f = 1
# times = 10
# print(fibo(f, times))
# a = [1, 44, 7, 2, 9, 4]
# b = [7, 2, 1, 44, 4, 9, 10]
# print(DealingDuplicates(a,b))
#print(reverse(a))
