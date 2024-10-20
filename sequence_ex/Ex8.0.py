current_hour = int(input("Enter the current hour: "))
want_to_wait = int(input("How long do you want to wait: "))

result = (current_hour + want_to_wait) % 24
print(f"The alarm will sound at: {result}h")