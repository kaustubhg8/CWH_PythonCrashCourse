try:
    num = int(input("Enter number: "))
    print(num + 3)
except Exception as e:
    print("Some error occurred.", e)

print("Code ran completely")