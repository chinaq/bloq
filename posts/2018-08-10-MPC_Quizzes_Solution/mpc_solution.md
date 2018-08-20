# MPC Quizzes Solution



- [MPC Quizzes Solution](#mpc-quizzes-solution)
    - [Code on Solution](#code-on-solution)
    - [Nonlinear Programming Using CppAD and Ipopt](#nonlinear-programming-using-cppad-and-ipopt)


## Code on Solution
- [CarND Controls Quizzes](https://github.com/udacity/CarND-MPC-Quizzes)
``` cpp
auto coeffs = polyfit(ptsx, ptsy, 1);    // fit the polynomial to the way points
double cte = polyeval(coeffs, x) - y;    // init cross track error
double epsi = psi - atan(coeffs[1]);     // init orientation error
state << x, y, psi, v, cte, epsi;

for (size_t i = 0; i < iters; i++) {
    // to get the best values of speed and orientation by IPOPT 
    // which is used to solve a nonlinear optimization problem 
    auto vars = mpc.Solve(state, coeffs);

    // x, y, psi, v, cte, epsi, delta, a  << from vars[0] to vars[7];
    state << vars[0], vars[1], vars[2], vars[3], vars[4], vars[5];
}
```




## Nonlinear Programming Using CppAD and Ipopt
- [Example and Test](https://www.coin-or.org/CppAD/Doc/ipopt_solve_get_started.cpp.htm)
- Problems
$$\begin{array}{lc}
{\rm minimize \; }      &  x_1 * x_4 * (x_1 + x_2 + x_3) + x_3 \\
{\rm subject \; to \; } &  x_1 * x_2 * x_3 * x_4  \geq 25 \\
                        &  x_1^2 + x_2^2 + x_3^2 + x_4^2 = 40 \\
                        &  1 \leq x_1, x_2, x_3, x_4 \leq 5
\end{array}$$
- Solve
``` cpp
    CppAD::ipopt::solve<Dvector, FG_eval>(
        options, xi, xl, xu, gl, gu, fg_eval, solution
    );
```
- xi, xl, xu
    - x and constrains
$$\begin{array}{lc}
    &  1 \leq x_1, x_2, x_3, x_4 \leq 5
\end{array}$$
- gl, gu
  - functions' constrains
$$\begin{array}{lc}
\\\ {\rm subject \ to \ } &  f[0] \geq 25
\\\ &  f[1] = 40
\\\ &  f[2] \leq 5
\end{array}$$
- fg_eval
    - functions
$$\begin{array}{lc}
\\{\rm minimize \ }       &  x_1 * x_4 * (x_1 + x_2 + x_3) + x_3
\\{\rm subject \ to \ }   &  x_1 * x_2 * x_3 * x_4
\\                        &  x_1^2 + x_2^2 + x_3^2 + x_4^2
\end{array}$$


