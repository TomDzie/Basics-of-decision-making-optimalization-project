# Basics-of-decision-making-optimalization-project
## Schedule problem description
The restaurant uses a system where customers, must declare what time they will arrive,
what time they will leave and how much money they intend to spend before arriving.
The next day, only selected customers can appear, and they are selected so as to
maximize the restaurant's profit but number of reservations can't exceed the number of tables.
## Approach to problem
To solve this optimization problem I took two approaches,
metaheuristic: tabu search in Python and IBM CPlex OPL implementation, but first, math.
[!IMPORTANT]
- Parameters:
  n - number of clients
  tables - number of tables
  opening - opening hour
  closing - closing hour
  time_range = $$(closing-opening) * 10
  
