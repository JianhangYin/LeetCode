def LongestPalindromicSubstring(inputStream):
    def helper(input_string, left_pointer, right_pointer):
        while left_pointer >= 0 and right_pointer < len(input_string) and input_string[left_pointer] == input_string[right_pointer]:
            left_pointer -= 1
            right_pointer += 1
        return input_string[left_pointer + 1:right_pointer]
    longest_substring = ''
    for i in range(len(inputStream)):
        even_substring = helper(inputStream, i, i + 1)
        odd_substring = helper(inputStream, i, i)
        if len(longest_substring) < len(even_substring):
            longest_substring = even_substring
        if len(longest_substring) < len(odd_substring):
            longest_substring = odd_substring
    return longest_substring


