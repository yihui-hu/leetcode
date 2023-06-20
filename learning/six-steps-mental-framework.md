## Step 1

Write down the problem.

```
Write a function to convert a given umber to English words. E.g. input is 123, output is "one hundred twenty three".
```

## Step 2

Clarify problem space.

```
- What is range of input?
- Can input be negative?
- Can input be fractional?
- Does output have dashes?
- Does output have "and" between hundred and the rest?
```

## Step 3

Write down test / edge cases.

```
1…9 → one…nine
10…19 → ten…nineteen
20, 30,…90 → twenty, thirty,…ninety
21 → twenty one
100 → one hundred
101…109 → one hundred one…one hundred nine
110…119 → one hundred ten…one hundred nineteen
120 → one hundred twenty
123 → one hundred twenty three
200 → two hundred
999 → nine hundred ninety nine
```

## Step 4

Describe and write down the algorithm. Form a clear idea before the implementation (in writing or comments). Don't jump to code.

Craft a solution with appropriate data structues and algorithms.

A potential first draft of the algorithm:

```
1. Create dictionary for all unique words (one ... ten, eleven ... nineteen, twenty, thirty, forty, ... ninety, hundred, ...)
2. Check boundaries: < 1 and > 999
3. Check simple unique words: < 20
4. Check ones
5. Check tens
6. Check hundreds
7. Put all words together
```

Writing it out might help you catch some errors – it's better to do steps 6 to 3 in reverse because we say "one hundred twenty three" and not "three twenty one hundred".

## Step 5

Start coding.

## Step 6

Test with your ccases found in Step 3.

## Epilogue

> Russians had a reputation for being the best programmers on Wall Street, and Serge thought he knew why: They had been forced to learn to program computers without the luxury of endless computer time.

> Many years later, when he had plenty of computer time, Serge still wrote out new programs on paper before typing them into the machine. “In Russia, time on the computer was measured in minutes,” he said. “When you write a program, you are given a tiny time slot to make it work. Consequently we learned to write the code in ways that minimized the amount of debugging. And so you had to think about it a lot before you committed it to paper. . . . The ready availability of computer time creates this mode of working where you just have an idea and type it and maybe erase it ten times. Good Russian programmers, they tend to have had that one experience at some time in the past — the experience of limited access to computer time.”

> — Michael Lewis. Flash Boys: A Wall Street Revolt
