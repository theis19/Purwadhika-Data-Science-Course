# No.1
def Hashtag(string):
    words = string.split()
    z = '#'
    for word in words:
        z += word.capitalize()
    if len(z)> 140 or z == '#':
        return False
    else:
        return z

print(Hashtag(" Hello there how are you doing"))
print(Hashtag(" Hello World " ))
print(Hashtag(""))

# No.2
def create_phone_number(number):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*number)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    
# No.3
def sort_odd_even(num):
    odd = []
    index_odd = []
    even = []
    index_even = []
    for i , j in enumerate(num):
        if j % 2 == 0:
            even.append(j)
            index_even.append(i)
        else:
            odd.append(j)
            index_odd.append(i)
    odd.sort()
    even.sort(reverse=True)        
    result = [0 for i in range(len(num))]
    for index, value in zip(index_odd, odd):
        result[index] = value
    for index, value in zip(index_even, even):
        result[index] = value
    return result        

print(sort_odd_even([5, 3, 2, 8, 1, 4]))

# No.4
def hollowTriangle(height):
    if height == 1:
        print('#')
        print()
    else: 
        z = '_'* (height - 1) + '#' + '_' * (height - 1)
        z += '\n'
        for i in range(height - 2, 0, -1):
            z += '_' * i + '#' + '_' * (2 * (height- i) - 3) + '#' + '_' * i
            z += '\n'
        z += '#' * (2 * height - 1)    
        
        print(z)
        print()  

hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)   
hollowTriangle(4)   
hollowTriangle(5)   
hollowTriangle(6)           