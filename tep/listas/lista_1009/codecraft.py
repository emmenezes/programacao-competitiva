months = [
    'December',
    'January', 
    'February', 
    'March', 
    'April', 
    'May', 
    'June', 
    'July', 
    'August', 
    'September', 
    'October', 
    'November',     
]

mon = input()
id = months.index(mon)
s = int(input())

print(months[(s+id)%12])