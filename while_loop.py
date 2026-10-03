# 🟢 Beginner
# 1 se 10 tak numbers print karo using while loop.
# num = 1
# while num <=10:
#     print(num)
#     num +=1



# 10 se 1 tak reverse counting print karo.
# num = 10
# while num > 0:
#     print(num)
#     num -= 1

# User se n input lo aur 1 se n tak numbers print karo.
# num = int(input("Enter a number : "))
# i = 1
# while i<=num:
#     print(i)
#     i += 1 


# 1 se 50 tak even numbers print karo.

# num = 1
# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# 1 se 50 tak odd numbers print karo.
# num = 1
# while num <= 50:
#     if num % 2 != 0:
#         print(num)
#     num += 1

# User se n lo aur 1 se n tak ka sum calculate karo.

# num = int(input("Enter a number : "))
# sum = 0
# i = 1
# while i <=num:
#     sum += i
#     i += 1

# print(sum)

# User se number lo aur uska table (1–10) print karo.

# num = int(input("Enter a number"))
# i = 1

# while i<=10:
#     print(f"{num} * {i} = {num * i}")
#     i+=1

# User se number lo aur uske digits count karo.
# Example: 58321 → 5 digits

# num = input("Enter a number : ")
# count = 0
# while num > 0:
#     num = num // 10
#     count +=1
    
# print(count)


# 🟡 Intermediate
# User se number lo aur uska factorial while loop se nikalo.

# Number ke digits ka sum find karo.
# Example: 1234 → 10
# num = int(input("Enter a number : "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum +=digit
#     num = num // 10 

# print(sum)


# Number ko reverse karo.
# Example: 12345 → 54321
# num = 5678
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print(rev)
# Check karo ki number palindrome hai ya nahi.
# num = 121
# copy = num
# rev = 0
# while copy > 0:
#     digit = copy % 10
#     rev = rev * 10 + digit
#     copy = copy // 10
    
# if num == rev:
#     print(f"{num} is palindrome")
# else:
#     print(f"{num} is not palindrome")

# Example: 121 → Palindrome


# Check karo ki number prime hai ya nahi.
# num = 23
# i = 1
# count = 0
# while i <= num:
#     if num % i == 0:
#         count += 1
#     i +=1
    
# if count ==2:
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not a prime number")


# n terms tak Fibonacci series print karo.

# n = int(input("Enter a number : "))
# a = 0 
# b = 1
# i = 1
# while i <= n:
#     print(a,end=" ")
#     c = a + b 
#     a = b
#     b = c
#     i += 1
    
    

# User se numbers input lete raho jab tak user 0 enter na kare. End me total sum print karo.
# stop = False
# sum = 0
# while stop == False:
#     n = int(input("Enter a number : "))
#     sum +=n
#     if n == 0:
#         stop = True
        
# print(sum)
     
# User se numbers input lete raho aur positive aur negative numbers ki count batao. 0 par stop karo.
# positive_number_count = 0
# negative_number_count = 0
# stop = False
# while stop == False:
#     num = int(input("Enter a number"))
#     if num > 0:
#         positive_number_count +=1
#     if num < 0:
#         negative_number_count +=1
#     if num == 0:
#         stop = True

# print(f"Positive numbers {positive_number_count}")
# print(f"negative numbers {negative_number_count}")
        
