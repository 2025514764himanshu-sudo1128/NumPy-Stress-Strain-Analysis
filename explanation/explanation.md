# Experiment 03 — Code Explanation
# Matrix Operations for Stress-Strain Analysis using NumPy

---

## What is this program doing?

In real mechanical systems, stress at any point in a 3D body
is not just one number — it has 9 components represented
as a 3×3 matrix called the **Stress Tensor**.

This program:
- Represents 3D stress as a matrix
- Verifies it is physically valid (symmetric)
- Calculates the traction force on a surface
- Finds principal stresses (the maximum/minimum stresses)
- Calculates Von Mises stress to predict if material will yield

---

## What is NumPy?

NumPy (Numerical Python) is a library for:
- Creating and manipulating arrays and matrices
- Fast mathematical operations on entire arrays at once
- Linear algebra (eigenvalues, matrix multiplication, etc.)

Without NumPy you would need hundreds of lines to do
what NumPy does in one line.

---

## Line by Line Explanation

---

### Line 1
```python
import numpy as np
```
Imports NumPy and gives it the short name `np`.
`np` is the universal convention — every engineer uses it.

---

### Lines 6-11 (Stress Tensor)
```python
sigma = np.array([
    [100, 30, 0],
    [30,  50, 0],
    [0,   0, 20]
])
```
**What is np.array()?**
Creates a NumPy array (matrix) from a Python list.
`[[...],[...],[...]]` = list of rows = 3×3 matrix.

**What does this tensor represent?**
```
σxx=100  τxy=30  τxz=0
τyx=30   σyy=50  τyz=0
τzx=0    τzy=0   σzz=20
```
- σxx, σyy, σzz = Normal stresses on each face (MPa)
- τxy, τyz, τzx = Shear stresses between faces (MPa)

**Physical meaning:**
The rod is being pushed with 100 MPa in x-direction,
50 MPa in y-direction, 20 MPa in z-direction,
and 30 MPa of shear between x and y faces.

---

### Lines 14-15 (Symmetry Check)
```python
is_symmetric = np.allclose(sigma, sigma.T)
print(f"Is Symmetric: {is_symmetric}")
```
**What is sigma.T?**
`.T` gives the **transpose** of the matrix —
rows become columns and columns become rows.

**What is np.allclose()?**
Checks if two matrices are equal within a small
numerical tolerance. Returns True or False.

**Why must stress tensor be symmetric?**
In mechanics, τxy = τyx (moment equilibrium requires this).
If it's not symmetric, the tensor is physically invalid.

---

### Lines 18-20 (Traction Vector)
```python
n = np.array([1, 0, 0])
traction = np.dot(sigma, n)
```
**What is a traction vector?**
The force per unit area acting on a surface with
normal direction n = [1,0,0] (the x-face).

**What is np.dot()?**
Matrix multiplication: T = σ × n
This is the most fundamental operation in stress analysis.

**Result:**
T = [100×1 + 30×0 + 0×0, 30×1 + 50×0 + 0×0, 0×1 + 0×0 + 20×0]
T = [100, 30, 0]
Meaning: On the x-face, there's 100 MPa normal stress
and 30 MPa shear stress.

---

### Lines 23-25 (Principal Stresses)
```python
eigenvalues = np.linalg.eigvals(sigma)
principal_stresses = np.sort(eigenvalues)[::-1]
```
**What are eigenvalues?**
When you rotate the coordinate system to a special
orientation, all shear stresses disappear and you're
left with only normal stresses — these are principal stresses.

Mathematically: solve det(σ - λI) = 0
The λ values are eigenvalues = principal stresses.

**What is np.linalg.eigvals()?**
`linalg` = linear algebra module inside NumPy.
`eigvals()` solves the eigenvalue equation and returns σ1, σ2, σ3.

**What is np.sort()[::-1]?**
`np.sort()` sorts ascending (low to high).
`[::-1]` reverses it to descending (high to low).
So σ1 > σ2 > σ3 — standard convention.

**Why do we need principal stresses?**
They tell us the MAXIMUM stress in the material,
regardless of direction — critical for failure prediction.

---

### Lines 28-30 (Von Mises Stress)
```python
s1, s2, s3 = principal_stresses
von_mises = np.sqrt(0.5 * ((s1-s2)**2 + (s2-s3)**2 + (s3-s1)**2))
```
**What is Von Mises stress?**
A single number that combines all stress components
into one equivalent stress for predicting yielding.

**Formula:**
σv = √(0.5 × [(σ1-σ2)² + (σ2-σ3)² + (σ3-σ1)²])

**How to use it:**
- If Von Mises stress < Yield strength → Material is SAFE
- If Von Mises stress ≥ Yield strength → Material YIELDS

**Why not just use maximum stress?**
Because yielding depends on the combination of all
stress directions, not just one. Von Mises accounts for all.

**What is np.sqrt()?**
NumPy's square root function — faster and more accurate
than math.sqrt() for array operations.

**Unpacking:**
`s1, s2, s3 = principal_stresses`
Assigns the 3 values from the array to 3 separate variables
in one clean line.

---

### Lines 33-37 (Safety Check)
```python
if von_mises < yield_strength:
    print("Material Status: SAFE - No yielding")
else:
    print("Material Status: YIELD - Material will deform plastically")
```
**What is plastic deformation?**
When stress exceeds yield strength, the material
permanently deforms — it doesn't return to original shape.
This is failure in engineering design.

---

## Key Concepts Summary

| Concept | What it is | Why important |
|---|---|---|
| Stress Tensor | 3×3 matrix of all stress components | Complete picture of stress state |
| Symmetry | τxy = τyx | Physical requirement — moment balance |
| Traction | Force on a specific surface | Design of bolts, welds, supports |
| Principal Stresses | Max/min normal stresses | Find worst case stress direction |
| Von Mises | Single equivalent stress | Predict if material will yield |

---

## NumPy Functions Used

| Function | What it does |
|---|---|
| np.array() | Create matrix from list |
| sigma.T | Transpose of matrix |
| np.allclose() | Check approximate equality |
| np.dot() | Matrix multiplication |
| np.linalg.eigvals() | Find eigenvalues |
| np.sort()[::-1] | Sort descending |
| np.sqrt() | Square root |
| np.round() | Round to decimal places |
