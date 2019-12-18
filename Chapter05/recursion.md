The problem all over the world can be divided into
1. the one based on the natural rule
2. the one depended on the previous stage (some previous stage will be duplicated in the problem solving, we can remember every stage to save time )

Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.

iteration have a fixed range of items.(for)
but while?

the while condition is the smaller problem we can solve, and we break down the item in the loop body.
The function calling itself don't need to set a flag variable, and keep it all. It just needs the range of each stage and reaching the smallest one to solve out.

0. figure out the expect result
1. Wirte the first step (It's important to find the law) to split
F(n) = k(n) + F(n-1) 
2. find a way to split the remain steps
3. figure out the F(0/1/2) solution
4. when you complete all step, the success will come without your notice. (Like you plan to achieve a goal)

how to implement the loop in the electric circuit?