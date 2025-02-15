# Einstein Field Equations Solver
## Purpose
The Einstein Field Equations (EFE) Solver is a Python-based application designed to help physicists, researchers, and students work with Einstein's field equations in general relativity. It provides a graphical interface for inputting metric tensors and computing various geometric quantities, making it easier to analyze spacetime geometries and their physical implications.

## Capabilities & Features

### Core Features
- Interactive GUI for metric tensor input
- Support for 2-4 dimensional spacetimes
- LaTeX input support for tensor components
- Real-time validation of metric consistency
- Computation of key geometric quantities:
  - Einstein tensor components
  - Ricci scalar
  - Christoffel symbols
- LLM-powered analysis and interpretation
- Dark mode interface optimized for scientific work

### Analysis Types
1. **Validation Analysis**
   - Signature consistency checking
   - Symmetry requirements verification
   - Physical meaningfulness assessment
   - Common error detection
   - Simplification suggestions

2. **Interpretation Analysis**
   - Spacetime classification
   - Physical significance explanation
   - Special properties identification
   - Related known solutions
   - Physical applications

3. **Suggestions**
   - Possible modifications
   - Additional terms to consider
   - Alternative coordinate systems
   - Comparative metrics
   - Physical scenarios to study

### Technical Features
- Asynchronous computation for responsiveness
- LaTeX export of results
- Error handling and recovery
- API integration with retry logic
- Extensible architecture for adding new analyses

## Requirements

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 500MB disk space
- Operating System: Windows 10+, macOS 10.14+, or Linux with glibc 2.17+

### Python Dependencies
- PyQt6 ≥ 6.4.0: GUI framework
- sympy ≥ 1.11.1: Symbolic mathematics
- einsteinpy ≥ 0.4.0: General relativity computations
- latex2sympy2 ≥ 1.8.3: LaTeX parsing
- torch ≥ 2.0.0: Tensor operations
- aiohttp ≥ 3.8.1: Async HTTP client
- requests ≥ 2.28.1: HTTP client
- typing-extensions ≥ 4.4.0: Type hinting
- numpy ≥ 1.23.0: Numerical computations

## Setup & Installation
### Basic Installation
To install the software, you'll need to install it from the source code. Here's how to do it:

1. First, create and navigate to a new directory:
```bash
mkdir einstein_solver
cd einstein_solver
```

2. Create all the files I provided earlier:
   - Create the directory structure:
   ```bash
   mkdir einstein_solver
   touch __init__.py
   touch einstein_solver/__init__.py
   ```
   
   - Create all the Python files (main.py, gui.py, analyzer.py, utils.py)
   - Create requirements.txt and setup.py with the content provided

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

After this, you should be able to run the solver using:
```bash
python run.py
```

**Note that this is a local development setup - the software is not currently distributed as a package.**

### Other Installation
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Or install from source
git clone https://github.com/moussan/einstein-solver.git
cd einstein-solver
pip install -e .
```

### API Configuration
Set up your API key for LLM analysis:
```bash
# Linux/macOS
export EINSTEIN_SOLVER_API_KEY='your-api-key'

# Windows (PowerShell)
$env:EINSTEIN_SOLVER_API_KEY='your-api-key'
```

### Running the Application
```bash
# From command line
einstein-solver

# Or from Python
from einstein_solver.main import main
main()
```

## Usage Guide

### Basic Usage
1. Launch the application
2. Set the number of dimensions (2-4)
3. Enter coordinate names in LaTeX format (e.g., t, r, \theta, \phi)
4. Click "Initialize Tensor Inputs"
5. Enter metric components in LaTeX format
6. Click "Solve Einstein Field Equations"

### Example: Schwarzschild Metric
Input the following components for a Schwarzschild metric:
```
g_00 = -(1-2M/r)
g_11 = 1/(1-2M/r)
g_22 = r^2
g_33 = r^2\sin^2\theta
```
Coordinates: t, r, \theta, \phi

### Tips
- Use LaTeX notation for mathematical expressions
- Check symmetry of your metric tensor
- Consider coordinate singularities
- Save your work frequently
- Export results for documentation

## Brief Discussion of Symbolic EFE

Einstein's field equations in symbolic form are:

G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}

Where:
- G_{\mu\nu} is the Einstein tensor
- \Lambda is the cosmological constant
- g_{\mu\nu} is the metric tensor
- T_{\mu\nu} is the stress-energy tensor
- G is Newton's gravitational constant
- c is the speed of light

The solver focuses on the vacuum field equations (T_{\mu\nu} = 0) and computes:

1. **Metric Tensor (g_{\mu\nu})**
   - Fundamental description of spacetime geometry
   - User-input through GUI
   - Must be symmetric

2. **Christoffel Symbols (Γ^λ_{\mu\nu})**
   - Connection coefficients
   - Describes how to parallel transport vectors
   - Computed from metric and its derivatives

3. **Einstein Tensor (G_{\mu\nu})**
   - Describes spacetime curvature
   - Built from Ricci tensor and scalar
   - Must satisfy Bianchi identities

4. **Ricci Scalar (R)**
   - Scalar curvature
   - Trace of the Ricci tensor
   - Important for understanding overall curvature

The solver handles all the complex symbolic computations required to go from the metric tensor to the Einstein tensor, making it easier to work with different spacetime geometries and analyze their properties.

## Contributing
Contributions are welcome! Please see our contributing guidelines for details on:
- Code style
- Testing requirements
- Pull request process
- Development setup

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- EinsteinPy development team
- SymPy development team
- PyQt development team
- All contributors and testers
