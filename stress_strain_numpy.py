import numpy as np

# ============================================================
# ============================================================

class StressTensorError(ValueError):
    """Raised for invalid stress tensor inputs."""
    pass

class VectorError(ValueError):
    """Raised for invalid normal vector inputs."""
    pass

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Error: Enter a numeric value.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Error: Enter a numeric value.")
            continue
        if value <= 0:
            print("  Error: Value must be greater than zero.")
            continue
        return value

def build_stress_tensor():
    """Build a 3x3 symmetric stress tensor from user input."""
    print("\n  Enter stress tensor components (MPa):")
    try:
        sxx = get_float("  σxx : ")
        syy = get_float("  σyy : ")
        szz = get_float("  σzz : ")
        txy = get_float("  τxy : ")
        tyz = get_float("  τyz : ")
        tzx = get_float("  τzx : ")
    except EOFError:
        raise StressTensorError("Input stream ended unexpectedly.")

    sigma = np.array([
        [sxx, txy, tzx],
        [txy, syy, tyz],
        [tzx, tyz, szz]
    ], dtype=float)
    return sigma

def get_normal_vector():
    """Get a unit normal vector from user."""
    print("\n  Enter normal vector components:")
    try:
        nx = get_float("  nx : ")
        ny = get_float("  ny : ")
        nz = get_float("  nz : ")
    except EOFError:
        raise VectorError("Input stream ended unexpectedly.")

    n = np.array([nx, ny, nz], dtype=float)
    magnitude = np.linalg.norm(n)

    if magnitude < 1e-10:
        raise VectorError("Normal vector cannot be a zero vector.")

    n_unit = n / magnitude
    if not np.allclose(n, n_unit, atol=0.01):
        print(f"  Info: Normalized to unit vector: {np.round(n_unit, 4)}")
    return n_unit

def analyse(sigma, yield_MPa):
    """Full stress tensor analysis."""
    print(f"\n{'='*55}")
    print("  RESULTS")
    print(f"{'='*55}")

    # Symmetry
    is_sym = np.allclose(sigma, sigma.T, atol=1e-6)
    print(f"\n  Symmetry : {'PASS ✓' if is_sym else 'FAIL ✗ — not a valid stress tensor'}")

    # Traction
    try:
        n = get_normal_vector()
        traction = np.dot(sigma, n)
        print(f"  Traction : {np.round(traction, 2)} MPa")
    except VectorError as e:
        print(f"  Traction Error: {e}")

    # Principal stresses (eigenvalues)
    try:
        eigenvalues = np.linalg.eigvals(sigma)
        # Use only real parts (imaginary parts from numerical noise)
        principal = np.sort(eigenvalues.real)[::-1]
        print(f"\n  Principal Stresses:")
        print(f"    σ1 = {principal[0]:.2f} MPa")
        print(f"    σ2 = {principal[1]:.2f} MPa")
        print(f"    σ3 = {principal[2]:.2f} MPa")
    except np.linalg.LinAlgError as e:
        print(f"  Eigenvalue Error: Could not compute — {e}")
        return

    # Von Mises
    try:
        s1, s2, s3 = principal
        von_mises = np.sqrt(
            0.5 * ((s1-s2)**2 + (s2-s3)**2 + (s3-s1)**2)
        )
        print(f"\n  Von Mises Stress : {von_mises:.2f} MPa")
        print(f"  Yield Strength   : {yield_MPa:.2f} MPa")
        if von_mises < yield_MPa:
            margin = yield_MPa - von_mises
            print(f"  Status           : SAFE ✓ (Margin: {margin:.2f} MPa)")
        else:
            excess = von_mises - yield_MPa
            print(f"  Status           : YIELD ✗ (Exceeds by: {excess:.2f} MPa)")
    except (ArithmeticError, FloatingPointError) as e:
        print(f"  Von Mises Error: {e}")

    print(f"{'='*55}")

def main():
    print("=" * 55)
    print("   EXPERIMENT 03: Stress-Strain Analysis (NumPy)")
    print("   AI in Mechanical Engineering — ONT406")
    print("   Sharda University")
    print("=" * 55)

    while True:
        print("\n--- MENU ---")
        print("1. Analyse Custom Stress Tensor")
        print("2. Use Preset Example Tensor")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            try:
                sigma     = build_stress_tensor()
                yield_MPa = get_positive_float("\n  Yield Strength (MPa): ")
                analyse(sigma, yield_MPa)
            except StressTensorError as e:
                print(f"  Tensor Error: {e}")

        elif choice == '2':
            sigma     = np.array([[100,30,0],[30,50,0],[0,0,20]], dtype=float)
            yield_MPa = 250.0
            print("\n  Preset: [[100,30,0],[30,50,0],[0,0,20]] MPa | Yield=250 MPa")
            analyse(sigma, yield_MPa)

        elif choice == '3':
            print("\nExiting. Goodbye!")
            break

        else:
            print("  Error: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user. Goodbye!")
