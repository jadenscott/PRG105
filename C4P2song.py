"""This program will display every single lyric of the song "99 bottles of beer on the wall" """

# This program does not require any variables, a for loop that counts down from 99 to 2 is established below
for num in range(99, 2, -1):
    print(f'{num} bottles of beer on the wall,\n{num} bottles of beer\nTake one down, pass it around\n{num - 1} bottles of beer on the wall')
    print()

# To account for different grammar when talking about the singular bottle
print("2 bottles of beer on the wall,\n2 bottles of beer\nTake one down, pass it around\n1 bottle of beer on the wall")
print()
print("1 bottle of beer on the wall,\n1 bottle of beer\nTake one down, pass it around\n0 bottles of beer on the wall")
