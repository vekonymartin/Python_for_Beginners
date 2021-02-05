# ------ Print command ------

print('Hello World!'); # ; --> not mistake, but no necessary as in c#

# --> # this is a comment sign
""" Multiple line comment """

""" If we use # sign, we need to follow a few rules 
    Firstly, if we use a simple comment, after the # sign
    should be followed by a space
    Secondly, if we would like to comment one or more lines
    in the code, after this you need two spaces
"""

#  print('Hello World!')

print("print multiply things, like:")
print("I like reddit and")
print("I like cats' meme!")
print()
print("But also" + " like dogs as well")
print("""and the good game's story,
films and series""")
print(

)
# ------ Display special characters when using print statement ------
"""
newline = '\n \r'
quote = '\'\"'
tab = '\t'
backslash = '\\'
"""
# ---------------------------
print('----------')
print("""Deep learning super sampling \'(DLSS)\' is an image upscaling technology developed by Nvidia\n and exclusive to Nvidia graphics cards\r for \"real-time\" use in select video games, 
using deep learning to upscale\n\t lower-resolution\n images to a higher-resolution for 
display\r on \\higher-resolution\\ computer monitors. 
""")
print('----------')
# ---------------------------

# ------ Print command ------
print('Press any button and after enter...')
input()
print('You pressed the button')
input(f"Enter number: ")
# ---------------------------
print('I have %s apples and %s pears'%(input(), input()))
print('----------')
print("I have {0} apples and {1} pears".format(input(), input()))
# --- END Print/Input commands ---