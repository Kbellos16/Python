# Define a function named count that takes a single parameter. 
# The parameter is a string. The string will contain a single word divided into syllables by hyphens
# "ho-tel" "cat" "met-a-phor" "ter-min-a-tor"
# Your function should count the number of syllables and return it.
# For example, the call count("ho-tel") should return 2.
string="cat" 
def count(string):
    syllibles =1
    for i in string:
        if i == '-':
            syllibles+=1
    return(syllibles)
print(count(string))
