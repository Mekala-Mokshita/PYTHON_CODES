# Longest Repeating Character Replacement(from leetcode)
def characterReplacement(s, k):
    freq = {}          # store frequency of characters
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        # increase frequency
        freq[s[right]] = freq.get(s[right], 0) + 1

        # update max frequency
        max_freq = max(max_freq, freq[s[right]])

        # check window validity
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        # update max length
        max_len = max(max_len, right - left + 1)

    return max_len


s = "AABABBAAC"
k = 2
print(characterReplacement(s, k))