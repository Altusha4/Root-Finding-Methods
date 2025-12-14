# Root Finding Methods — Numerical Analysis

A structured implementation of **numerical root-finding methods** for solving a
nonlinear equation.  
Developed using **Python**, **NumPy**, **Matplotlib**, and **Jupyter Notebook**
as part of the **Numerical Methods / Computational Mathematics** course.

---

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)  
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## Selected Function

The selected nonlinear function (**Function 9**) is:

\[
f(x) = e^x - 3x
\]

The goal of the project is to approximate the root of this equation using
different numerical methods and analyze their convergence behavior.

---

## Features

- **Implementation of six numerical root-finding methods**
- **Clear iteration tables** (iteration, approximation, function value, error)
- **Graphical visualization of the function and estimated root**
- **Convergence plots** (log-scale error analysis)
- **Comparison of iteration counts between methods**
- **Clean and well-organized project structure**
- **Final Jupyter Notebook for analysis and presentation**

---

## Implemented Methods

- **Bisection Method**
- **False Position Method (Regula Falsi)**
- **Fixed Point Iteration**
- **Newton–Raphson Method**
- **Secant Method**
- **Muller’s Method**

Each method follows the stopping criteria defined in the assignment and is
implemented both as a standalone Python script and inside the final notebook.

---

## Project Structure
```
PythonProject/
│
├── methods/
│ ├── bisection.py # Bisection method implementation
│ ├── false_position.py # False Position (Regula Falsi) method
│ ├── fixed_point.py # Fixed Point Iteration method
│ ├── newton.py # Newton–Raphson method
│ ├── secant.py # Secant method
│ └── muller.py # Muller’s method
│
├── notebook/
│ └── Root_Finding_Methods.ipynb # Final analysis notebook
│
├── venv/ # Python virtual environment (ignored by git)
├── .gitignore
└── README.md
```

---

## Stopping Criteria

The iteration process is stopped when one of the following conditions is
satisfied:

- the function value is sufficiently close to zero,
- two successive approximations are sufficiently close,
- or the interval containing the root becomes sufficiently small.

The tolerance is set to:

**Tolerance:** ε = 10⁻³

---

## How to Run the Project

### 1. Activate virtual environment (optional)
```bash
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```
### 2. Open the Jupyter Notebook
```bash
jupyter notebook notebook/Root_Finding_Methods.ipynb
```
### 3. Run all cells in order
The notebook contains the complete implementation, plots, and comparison.

## Comparison Summary
The methods were compared based on:

* number of iterations
* convergence speed
* stability and robustness

Bracketing methods were more stable, while open methods converged faster when
good initial guesses were provided.
