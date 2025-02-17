from setuptools import setup, find_packages

setup(
    name="einstein-solver",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'PyQt6',  # If using Qt
        'sympy>=1.11.1',
        'einsteinpy>=0.4.0',
        'latex2sympy2>=1.8.3',
        'torch>=2.0.0',
        'aiohttp>=3.8.1',
        'requests>=2.28.1',
        'typing-extensions>=4.4.0',
        'numpy>=1.23.0',
    ],
    entry_points={
        'console_scripts': [
            'einstein-solver=einstein_solver.main:main',
        ],
    },
    python_requires='>=3.8',
    author="MoussaN",
    description="Einstein Field Equations Solver with LLM Integration",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
