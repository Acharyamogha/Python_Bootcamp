"""
Find the longest substring without any repeating characters within a given string
"""
def longest_substring_without_repeating(s: str) -> str:
    max_length = 0
    start = 0
    longest_substr = ""

    for end in range(len(s)):
        for i in range(start, end):
            if s[i] == s[end]:
                start = i + 1
                break
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            longest_substr = s[start:end + 1]

    return longest_substr

# Example usage
input_string = "impatient"
result = longest_substring_without_repeating(input_string)
print(f"The longest substring without repeating characters is: '{result}'")