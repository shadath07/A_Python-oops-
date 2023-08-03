# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), 
# and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

def is_balanced_delimiter(input_string):
    stack = []
    opening_chars = "({["
    closing_chars = ")}]"
    char_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in input_string:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack or stack[-1] != char_pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
input_str= input("enter the string of character to check:")
print(is_balanced_delimiter(input_str))  
