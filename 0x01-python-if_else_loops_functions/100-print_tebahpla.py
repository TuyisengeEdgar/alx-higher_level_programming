 #!/usr/bin/python3

 for char in range(ord('z'), ord('a') - 1, -1):
     if char % 2 is 1:
         char = char - ord(' ')
     print("{}".format(chr(char - i)), end="")
     
