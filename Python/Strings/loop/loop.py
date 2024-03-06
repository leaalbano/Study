import unittest

class TestLoop(unittest.TestCase):
    def setUp(self):
        self.numbers = [1,2,3,4,5,6,7,8,9]
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j']
        self.words = ['apple', 'banana', 'orange', 'pineapple']
        self.list_of_words = [['pine', 'grape', 'lemon'], ['Apple', 'Orange', 'Banana']]


    def test_loop1(self):
        print("ex1")
        for word in self.words:
            print(word)
        
    def test_loop2(self):
        print("ex2")
        word_index = 0
        char_index = 0
        for word in self.words:
            print(f"word index: {word_index}")
            word_index += 1
            for char in word:
                print(f"char index: {char_index}")
                char_index += 1
                print(char)
    
    def test_loop3(self):
        print("ex3")
        for item in self.list_of_words:
            for list in item:
                print(list)
    
    def test_loop4(self):
        print(f"Print each number in the numbers list multiplied by 3")
        for number in self.numbers:
            print(number*3)

    def test_loop5(self):
        print(f"Print each letter in the letters list repeated 4 times.")
        for letter in self.letters:
            print(letter * 4)
                
    def test_loop6(self):
        print(f"Print each word in the words list concatenated with 's'.")
        for word in self.words:
            print(word + 's')

    def test_loop7(self):
        print(f"Print each word in the list_of_words list in lowercase.")
        for list in self.list_of_words:
            for word in list:
                print(word.lower())
    
    def test_loop8(self):
        print("Print the length of each word in the words list.")
        for word in self.words:
            print(len(word))
            
    def test_loop9(self):
        print("Print the sum of the numbers in the numbers list.")
        print(sum(self.numbers))

    def test_loop_10(self):
        print("Print the reverse of each word in the words list.")
        for word in self.words:
            reversed_word = ''.join(reversed(word))
            print(reversed_word)

    def test_loop_11(self):
        print("Print the reverse of each word in the words list.")
        for word in self.words:
            reversed_word = word[::-1]
            print(reversed_word)
    
    def test_loop_12(self):
        print("Print each word in the list_of_words list concatenated with the word 'fruit'.")
        for list in self.list_of_words:
            for word in list:
                print(word + 'fruit')

    def test_loop_13(self):
        print("Print the index of the first occurrence of the letter 'e' in the letters list.")
        index = 0
        for letter in self.letters:
            if letter == 'e':
                print(index)
            index += 1
        
    def test_loop_14(self):
        print("Print the index of the last occurrence of the letter 'a' in the letters list.")
        index = len(self.letters)
        for letter in self.letters[::-1]:
            if letter == 'a':
                print(index)
            index -= 1

    def test_loop_15(self):
        print("Print each number in the numbers list if it is greater than 5.")
        for number in self.numbers:
            if number > 5:
                print(number)
    
    def test_loop_16(self):
        print("Print each letter in the letters list if its index is even.")
        index = 0
        for letter in self.letters:
            if index%2 == 0:
                print(letter)
            index += 1

    def test_loop_17(self):
        print("Print each letter in the letters list if its index is even.")
        index = 0
        for letter in range(0,len(self.letters), 2):
            print(self.letters[letter])

    def test_loop_18(self):
        print("Print each word in the words list if its length is even.")
        for word in self.words:
            if len(word)%2 == 0:
                print(word)


    def test_loop_19(self):
        print("Print each word in the list_of_words list if any of its inner words contain the letter 'a'.")
        for list in self.list_of_words:
            for word in list:
                if 'a' or 'A' in word:
                    print(word)

    def test_loop_20(self):
        print("Print each word in the list_of_words list if all of its inner words start with 'p'.")
        p_words = []
        for list in self.list_of_words:
            for word in list:
                if word[0] == 'p':
                    p_words.append(word)
                else:
                    return None
        return(p_words)
    
    def test_loop_21(self):
        print("Print each word in the words list if it contains the letter 'n'.")
        for word in self.words:
            if 'n' in word:
                print(word)
       
    
    def test_loop_22(self):
        print("Print each letter in the letters list if it is a vowel ('a', 'e', 'i', 'o', 'u').")
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letter in self.letters:
            if letter in vowels:
                print(letter)
    
    def test_loop_23(self):
        print("Print each word in the list_of_words list if its length is greater than 2.")
        for list in self.list_of_words:
            for word in list:
                if len(word) > 2:
                    print(word)
    
    def test_loop_24(self):
        print("Print the index of each word in the words list along with the word itself.")
        index = 0
        for word in self.words:
            print(f"{index}, {word}")
            index += 1
    
    def test_loop_25(self):
        print("Print the index of each word in the words list along with the word itself.")
        for index, word in enumerate(self.words):
            print(index, word)
    
    def test_loop_26(self):
        print("Print the index of each number in the numbers list along with its square.")
        index = 0
        for number in self.numbers:
            print(index, number**3)
            index += 1
    
    def test_loop_27(self):
        print("Print the index of each word in the words list along with its length.")
        index = 0
        for word in self.words:
            print(f"index: {index}, word: {word}, length: {len(word)}")
            index += 1
    
    def test_loop_28(self):
        print("Print the index of each word in the list_of_words list along with the number of inner words it contains.")
        word_count = 0
        for list in self.list_of_words:
            index = 0
            for word in list:
                print(index, word)
                index += 1
                word_count += 1
        print("word count:", word_count)

    def test_loop_29(self):
        print("Print First 10 natural numbers using while loop")
        n = 1
        while n <= 10:
            print(n)
            n += 1

    def test_loop_30(self):
        print("Write a program to print the following number pattern using a loop.")
        '''

                1 
                1 2 
                1 2 3 
                1 2 3 4 
                1 2 3 4 5
    '''        
        row = 5
        for i in range(1, row+1,1):
            for j in range(1, i):
                print(j, end='')
            print(i)

    def test_loop_31(self):
        print("Calculate the sum of all numbers from 1 to a given number")
        num = int(input("Enter number: "))
        sum = 0
        for i in range(1, num+1, 1 ):
            sum = sum + i
        print(f"sum is: {sum}")

    def test_loop_32(self):
        print("Write a program to print multiplication table of a given number")
        num = int(input("Enter number: "))
        for i in range(1, 11, 1):
            print(num*i)

    def test_loop_33(self):
        print("Display numbers from a list using loop")
        '''The number must be divisible by five
            If the number is greater than 150, then skip it and move to the next number
            If the number is greater than 500, then stop the loop'''
        numbers = [12, 75, 150, 180, 145, 525, 50]
        for number in numbers:
            if number > 500:
                break
            elif number > 150:
                continue
            elif number % 5 == 0:
                print(number)

    def test_loop_34(self):
        print("Write a program to count the total number of digits in a number using a while loop.")
        number = input("Enter num: ")
        i = 0
        while i < len(number):
            i += 1
        print("count is",i) 

    def test_loop_35(self):
        print("Print the following pattern")
        row = 5
        inner = 5
        for i in range(0, row+1, 1):
            for j in range(inner-i, 0, -1):
                print(j, end='')
            print()

    def test_loop_36(self):
        print("Print list in reverse order using a loop")
        list1 = [10, 20, 30, 40, 50]
        reversed_list = list1[::-1]
        for num in reversed_list:
            print((num))

    def test_loop_37(self):
        print("Display numbers from -10 to -1 using for loop")
        for num in range(-10, 0, 1):
            print(num)

    def test_loop_38(self):
        print("Use else block to display a message “Done” after successful execution of for loop")
        num = 5
        for i in range(1,6,1):
            print(i)
        else:
            print("Done")

    def test_loop_39(self):
        print("Write a program to display all prime numbers within a range")
        # range
        start = 25
        end = 50
        for num in range(start, end+1, 1):
            start_index = 2
            divisible = False
            while start_index < num:
                if num%start_index != 0:
                    start_index += 1
                else:
                    divisible = True
                    break
            if divisible != True:
                print(num)

    def test_loop_40(self):
        '''print sum of first 10 numbers'''
        end = 10
        start = 1
        sum = 0
        while start <= end:
            sum += start
            start += 1
        print(f"Total: {sum}")

    def test_loop_41(self):
        '''Print sum of all even numbers from 10 to 20'''
        sum = 0
        for num in range(10,22,2):
            sum += num
        print(sum)

    def test_loop_42(self):
        '''Calculate the average of list of numbers'''
        numbers = [10, 20, 30, 40, 50]

        count = 0
        sum = 0
        for num in numbers:
            sum += num
            count += 1
        print(f"Average: {sum/count}")

    def test_loop_43(self):
        '''Print all even and odd numbers'''
        for num in range(0,21,1):
            if num%2 == 0:
                print(f"Even: {num}")
            else:
                print(f"Odd: {num}")

    def test_loop_44(self):
        '''Use for loop to generate a list of numbers from 9 to 50 divisible by 2.'''
        for num in range(9,51,1):
            if num%2 == 0:
                print(num)
            else:
                continue

if __name__ == '__main__':
    unittest.main()