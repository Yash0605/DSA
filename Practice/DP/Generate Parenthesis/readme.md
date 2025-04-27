# Generate Parentheses

[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

## Prac 1 thought process
------------------------------
Keep track of the open and closed parantheses => if we track and correctly update the open and closed parantheses then we can be sure that we generate only valid values.
We need to make msure how we are checking and adding the values.
Recursion will take care of generating all the different versions of the required values.

We need yo properly update the current string while calling the recursive method, else we need to explicitly back track
✅ current + '(' = safe, no side effects, each branch independent.

❌ current += '(' = dangerous, affects all future paths, wrong results.

Why is it safe for open and close?

open and close are integers.
Integers are immutable in Python.
open += 1 creates a new integer in memory for the current call frame.
Each recursive call still gets its own open and close values.
There’s no shared mutation problem like there is with strings or lists.

Let's walk through your code step-by-step for n = 2.

First, you call:

generateParenthesis(2)
which does:

ans = []
self.parenthesisHelper(2, ans, 0, 0, '')
Now stepping through parenthesisHelper:

First Call:

n=2, ans=[], open=0, close=0, current=''
open < n, so call with open=1, current='('.

Second Call:

n=2, ans=[], open=1, close=0, current='('
open < n, call with open=2, current='(('.

Third Call:

n=2, ans=[], open=2, close=0, current='(('
open == n now, cannot add '(' anymore.

close < open, so call with close=1, current='(()'.

Fourth Call:

n=2, ans=[], open=2, close=1, current='(()'
open == n, cannot add '('.

close < open, call with close=2, current='(())'.

Fifth Call:

n=2, ans=[], open=2, close=2, current='(())'
len(current) == 2*n (4 == 4), so append (()) to ans.

Now ans = ['(())']

Return.
(Returns back to Fourth Call → Third Call → Second Call)

Back to Second Call (current='('):

After adding '(' path, now check close < open:

close=0, open=1, so close < open is true → call with close=1, current='()'.

Sixth Call:

n=2, ans=['(())'], open=1, close=1, current='()'
open < n, call with open=2, current='()('.

Seventh Call:

n=2, ans=['(())'], open=2, close=1, current='()('
open == n, cannot add '('.

close < open, call with close=2, current='()()'.

Eighth Call:

n=2, ans=['(())'], open=2, close=2, current='()()'
len(current) == 4, so append ()() to ans.

Now ans = ['(())', '()()']

Return.

At this point, all recursive paths have been completed.

Finally, generateParenthesis(2) returns:
['(())', '()()']
