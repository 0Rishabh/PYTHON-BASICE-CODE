
# WAP to Find the Sum of Natural Number 

print("Sum of Natural number")
limit = int(input(":Enter The Limit: "))
natural_num = 0
for n in range(1,limit+1):
    natural_num += n
print(f"The Sum of Natural Numbers up to {limit} is: {natural_num}")

