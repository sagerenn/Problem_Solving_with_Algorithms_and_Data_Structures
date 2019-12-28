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
2. find all the ways and their relationships(step by step, all need to invoke) to split the remain steps
3. figure out the F(0/1/2) solution
4. when you complete all step, the success will come without your notice. (Like you plan to achieve a goal)

how to implement the loop in the electric circuit?

Maybe the iteration and recursion can be exchange within one dimension problem. Those more than one dimension will be elegant to solve by recursion.

The problem have a clear rule or a repeatable process and can break down(save the previous result in the temperory or permanent memory), then we can consider to solve it by recursion.


# Dynamic Programming
Maybe use recursion directly can solve the problem, but it's not the best or the least cost solution instead of one solution based on the order of recursion cmds in general, e.g. the path of maze(NSWE,WESN), it'll contain some extra point or steps that is not false.
To optimize some situation, the dynamic programming is one of the strategy.
Maybe we need to find out all result to compare which one is the least. In the process, some variable can be used in others solution, it will save time to read the intermedia variable rather than doing search all the time.

1. recursion(top down)
2. caching or memoization, reduce the repeated work, which smaller one is not needed will not be cached. (holes in the list)
3. dynamic programming, solve systematically the current state by the all previous state. We start to solve the basic one, and get larger until the the current value(buttom up). The min current will be calculated by loop over the previous state within some fix rule or value, save the min and the corresponding value to keep track the size and item of conbination.