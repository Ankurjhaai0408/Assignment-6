# Assignment-6
Medians and Order Statistics &amp; Elementary Data Structures
Running the Code 
Clone or download the repository. 
Open a terminal and navigate to the project directory. 
Run the script using the following command: python Assignment6Part1.py
Run the script using the following command: python Assignment6Part2.py
The script will generate execution and will display the results in the terminal.

Summary of Findings:
Randomized Quickselect 

- The expected recurrence relation is:   

  T(n) = T(n/2) + O(n)  

- Solving the recurrence using the recursion tree method yields an expected complexity of O(n). 

- However, in the worst case (bad pivot selections), the recurrence becomes: 

  T(n) = T(n-1) + O(n) which simplifies to (O(n^2). 

 

Deterministic Median of Medians 

- The median-of-medians algorithm ensures a good pivot selection by dividing the array into five groups and selecting their medians. 

"Space Complexity has 2 operators and they are Quickselect and Median of Medians". 

