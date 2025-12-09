#pregunta de rescate
#programa fibonacci

terms = input ("set your numbers terms: ")
if not terms.isdigit():
    print("error: is not a valid character")
    exit()

n = int(terms)

if n<1 or n>50:
    print("Error> the number is not in the range")
    exit()
elif n==1:
    print("fibonacci 0")
    exit()
elif n==2:
    print("fibonacci: 0, 1")
    exit()
fibo= [0,1]

for i in range (2, n):
    next_term =fibo[i-1]+fibo[i-2]
    fibo.append(next_term)
fibo_text=", ".join(str(x) for x in fibo)
print(f"fibonacci: {fibo_text}")


