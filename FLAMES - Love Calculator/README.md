## Aim:
I aimed to solve the FLAMES game in very simple logic. As a beginner, it was very challenging for me to come up with simple and precise logic for this problem.

## What is FLAMES?
**FLAMES** is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.

There are two steps in this game.

**Step 1**: Take the two names.
Remove the common characters with their respective common occurrences. Get the count of the characters that are left.

**Step 2**: Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
Start removing letter using the count we got. The letter that lasts the process is the result.

Example:

 **Input**: Player1 = AJAY, Player2 = PRIYA
 
**Output**: Friends

**Explanation:**

In the above given two names A and Y are common letters which are occurring one time(common count) in both names so we are removing these letters from both names. Now count the total letters that are left here it is 5. Now start removing letters one by one from FLAMES using the count we got and the letter which lasts the process is the result.
 

**FLAMES**

Initially Counting starts from the first letter i.e., F. So E is at 5th count so we remove E and start counting again but this time start from S.

**FLAMS**

M is at 5th count so we remove M and counting starts from S.

**FLAS**

S is at 5th count so we remove S and counting start from F.

**FLA**

L is at 5th count so we remove L and counting starts from A.

**FA**

A is at 5th count so we remove A. Now we have only one letter remaining, so this is the final answer.

**F**

So, the relationship is F i.e., Friends.

## Credits:
The above explanation for the FLAMES game has been taken from [geeksforgeeks](https://www.geeksforgeeks.org/program-to-implement-flames-game/)
