# Decode Ways

[Decode Ways](https://leetcode.com/problems/decode-ways/description/)

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

## Prac 1 thought process
------------------------------

We need to be aware that we need to calculate the number of ways. Basically same as number of ways to climb the stairs.
So for number of ways like stairs, we always have => ways = single + double
Add condition to check if single char can be decoded
Add condition to check if 2 chars can be decoded

For tabulation
When you're at the very beginning:

Before any character (i = 0), you have 1 way to decode an "empty string" — do nothing, valid way. So, prev2 = 1.

At the first character (i = 1):

If the first character is not '0', there is 1 way to decode it.

(If it were '0', we'd already return 0 at the beginning.)

Thus:

prev2 = 1 for the empty string ("" → 1 way),

prev1 = 1 for the first character (assuming it’s not '0')

3. Analogy
Think of climbing stairs:

prev2 is the number of ways to be 2 steps below.

prev1 is the number of ways to be 1 step below.

You build from those two options.

Since there's 1 way to be at step 0 (standing still) and 1 way to reach step 1 (single move if the first character isn't '0'), you start with both as 1.