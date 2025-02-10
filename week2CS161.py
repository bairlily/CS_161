#Part 1
# it printed "31 0b11111 0x1f"
#Part 2a
# the error it printed was "TypeError: 'float' object cannot be interpreted as an integer"
# this is because I was using a float when an integer was expected.
#Part 2b
x = 18
print(x, bin(x), hex(x))
# this prints 18 0b10010 0x12
#Part 3
y = 0b1011
z = 0xA3
print(y, z)
# this prints out the integer
#Part 4
w = x + y + z
# adding three variables
print('the sum is', w)
#COMPRESSION
orig_size = 240
d_size = 25
comp_text_size = 148
# this formula adds compression text size and dictionary size, then divides it by the original size, which is 240, then finally subtraction it by one.
percent_of_compression = 1 - ((comp_text_size + d_size) / orig_size)
# multiplying it by 100 should put it into a percentage form.
percent_of_compression *= 100
# rounding the decimal point by 2 so that it looks neater.
percent_of_compression = round(percent_of_compression, 2)
# printing out all the variables
print('Compressed text size:', str(comp_text_size), 'characters')
print(' 	Dictionary size:', str(d_size), 'characters')
print(' 	     Total:', comp_text_size + d_size, 'characters')
print (' Original text size:', str(orig_size), 'characters')
print (' 	Compression:', str(percent_of_compression), '%')
