# Einstein Field Equations Solver

📊 A modern PyQt6-based application for solving and analyzing Einstein Field Equations with Claude AI integration.

## Project Structure
```
einstein-solver/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── einstein_solver/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── gui.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   ├── test_gui.py
│   └── test_utils.py
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── README.md
├── requirements.txt
└── setup.py
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/einstein-solver.git
cd einstein-solver
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```
ANTHROPIC_API_KEY=your_claude_api_key_here
```

## Usage

Run the application:
```bash
einstein-solver
```

Or from Python:
```python
from einstein_solver.main import main
main()
```

## Development

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Run tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
