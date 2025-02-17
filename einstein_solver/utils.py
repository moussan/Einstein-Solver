from dataclasses import dataclass
from typing import List, Optional
import sympy as sp
from latex2sympy2 import latex2sympy
import os
import logging
from pathlib import Path

@dataclass
class MetricData:
    """Data class for storing metric tensor information"""
    components: List[List[str]]
    dimension: int
    coordinates: List[str]
    
    def to_matrix(self) -> sp.Matrix:
        """Convert components to sympy Matrix"""
        metric = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                try:
                    if self.components[i][j] == "0":
                        row.append(sp.Integer(0))
                    else:
                        expr = latex2sympy(self.components[i][j])
                        row.append(expr)
                except:
                    row.append(sp.Integer(0))
            metric.append(row)
        return sp.Matrix(metric)

@dataclass
class APIConfig:
    """Configuration for API connections"""
    api_key: Optional[str] = None
    api_url: str = "https://api.example.com/v1"
    timeout: int = 30
    max_retries: int = 3
    
    def __post_init__(self):
        """Load API key from environment if not provided"""
        if not self.api_key:
            self.api_key = os.getenv('EINSTEIN_SOLVER_API_KEY')
    
    def get_headers(self) -> dict:
        """Get HTTP headers for API requests"""
        if not self.api_key:
            return {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def to_dict(self) -> dict:
        """Convert config to dictionary"""
        return {
            'api_url': self.api_url,
            'timeout': self.timeout,
            'max_retries': self.max_retries
        }

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Path('logs/einstein_solver.log')),
            logging.StreamHandler()
        ]
    )