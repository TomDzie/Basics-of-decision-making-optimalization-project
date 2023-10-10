# Basics-of-decision-making-optimalization-project
## Schedule problem description
The restaurant uses a system where customers, must declare what time they will arrive,
what time they will leave and how much money they intend to spend before arriving.
The next day, only selected customers can appear, and they are selected so as to
maximize the restaurant's profit but number of reservations can't exceed the number of tables.
## Approach to problem
To solve this optimization problem I took two approaches,
metaheuristic: tabu search in Python and IBM CPlex OPL implementation, but first, math.  
- Parameters:  
n - number of clients  
tables - number of tables  
opening - opening hour  
closing - closing hour  
time_range = (closing-opening) * 10  
clients(n x 3) = [[entered, left, money spend] ... n]  
time(n x time_range) = {1 if client occupies table in current unit of time, 0 if not  
- Decision variables  
earings – total profit  
chosen(n x 1) = {1 if client is chosen, 0 if not  
- objective function:  
argmax{earings}  
- Limitations:
Maximize profit  
$\sum_{1}^{n}\left( chosen_{n} * clients_{n,3}  \right ) \geq earings$  
Maximum as many customers at one time as all tables:  
$\sum_{1}^{n}\left( time_{n,time range} * chosen_{n} \right ) \leq tables, \forall time_{range}$

## CPLEX OPL implementation 
In Cplex everything stays simple, just rewrite math to code. As simple as that

## Heurestic algorithm implementation
The basic idea of Tabu Search is to penalize moves that take the solution into previously visited search
spaces (also known as tabu). Tabu Search, however, does deterministically accept non-improving solutions in order to prevent getting stuck in local minimums.  
These are the steps algorithm go through:   
1. Initialization:  
Start with an initial solution to the optimization problem.  
Initialize a tabu list to keep track of recently visited solutions.  
Set other parameters, such as the size of the tabu list and the maximum number of iterations.  
2. Generate Neighboring Solutions:  
Generate a set of neighboring solutions from the current solution. This involves making small modifications to the current solution.  
These modifications can include swapping elements, reversing sequences, or other local changes depending on the nature of the problem.  
3. Evaluate Solutions:  
Evaluate the objective function for each of the generated neighboring solutions.  
The objective function quantifies the quality of a solution with respect to the optimization problem.  
4. Aspiration Criteria:  
Check if any of the neighboring solutions are better than the current solution and satisfy aspiration criteria.  
Aspiration criteria are conditions under which a solution that would normally be considered tabu is allowed if it represents a significant improvement.  
5. Update Tabu List:  
Add the current solution or move to the tabu list to prevent revisiting it in the near future.  
Remove old entries from the tabu list to ensure it does not become too large.  
6. Update Best Solution:  
If the current solution is better than the best solution found so far, update the best solution.  
7. Diversification:  
Introduce diversification mechanisms to explore different regions of the search space. This may involve perturbing the current solution to escape local optima.  
8. Termination Criteria:  
Check if termination criteria are met. This could include a maximum number of iterations, a satisfactory solution, or a time limit.  
9. Iterate:  
Repeat steps 2-8 until the termination criteria are met.  
