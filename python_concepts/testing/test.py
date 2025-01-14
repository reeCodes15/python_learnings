# print('1')

# print('1')

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

def needle_in_haystack(needle, haystack):

    # print(needle)
    # print(haystack)
    result= haystack.find(needle)
    # print(result)
    return result

str21 = "sad"
haystack = "asadbutsad"


