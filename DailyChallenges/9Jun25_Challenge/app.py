def longest_unique_substring(s: str) -> int:
    substring = ""
    final_substring = ""
    count = 0

    for char in s:
        if char in substring:       # If duplicate found, remove characters up to the first duplicate
            index = substring.index(char)
            substring = substring[index + 1:] #<- Like this
        substring += char  # Add current character to the substring

        # Update the longest substring if needed
        if len(substring) > count:
            count = len(substring)
            final_substring = substring

    print(f'Output: {count}')
    print(f'Explanation: The answer is \"{final_substring}\", with the length of {count}.')
    return count

# Test it
longest_unique_substring(input("Input: "))
