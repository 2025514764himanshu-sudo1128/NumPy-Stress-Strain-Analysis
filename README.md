# Experiment 03: Matrix Operations for Stress-Strain Analysis using NumPy

**Subject:** AI in Mechanical Engineering (ONT406)
**Sharda University, Greater Noida**

---

## Aim
To perform matrix-based stress transformations and determine principal stresses and Von Mises stress using NumPy.

---

## Concepts Covered
- Cauchy Stress Tensor (3×3 matrix)
- Matrix symmetry verification
- Traction vector calculation
- Principal stresses using Eigenvalues
- Von Mises stress for yield criteria

---

## Formulas Used

| Formula | Description |
|---|---|
| T = σ × n | Traction vector |
| det(σ - λI) = 0 | Principal stress eigenvalue equation |
| σv = √(0.5×[(σ1-σ2)²+(σ2-σ3)²+(σ3-σ1)²]) | Von Mises stress |

---

## Software Required

| Software | Purpose | Download Link |
|---|---|---|
| Python 3.x | Programming language | https://www.python.org/downloads/ |
| VS Code | Code editor | https://code.visualstudio.com/ |
| Git | Version control | https://git-scm.com/ |

---

## Installation Steps

### Step 1: Install Python
```
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or above
3. CHECK "Add Python to PATH" during installation
4. Verify: python --version
```

### Step 2: Install Required Library
Open terminal and run:
```bash
pip install numpy
```

### Step 3: Verify Installation
```bash
python -c "import numpy; print(numpy.__version__)"
```

---

## How to Run

```bash
git clone https://github.com/2025514764himanshu-sudo1128/Exp03-NumPy-Stress-Strain-Analysis.git
cd Exp03-NumPy-Stress-Strain-Analysis
python stress_strain_numpy.py
```

---

## Expected Output
```
=== Stress Tensor ===
[[100  30   0]
 [ 30  50   0]
 [  0   0  20]]

Is Symmetric: True
Traction Vector: [100  30   0]
Principal Stresses (MPa): [114.14  35.86  20.  ]
Von Mises Stress (MPa): 85.44
Material Status: SAFE - No yielding
```

---

## Author
**Himanshu Kumar** (2025514764)
Department of Electrical, Electronics and Communication Engineering
Sharda University, Greater Noida
