from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QTextEdit, QPushButton, QSpinBox, 
    QMessageBox, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
import sympy as sp
from einsteinpy.symbolic import MetricTensor, EinsteinTensor
from latex2sympy2 import latex2sympy

from .analyzer import LLMAnalyzer
from .utils import MetricData, APIConfig

class TensorInputWidget(QWidget):
    def __init__(self, dim: int, coords: list, tensor_name: str = "g"):
        super().__init__()
        self.setup_ui(dim, coords, tensor_name)
    
    def setup_ui(self, dim: int, coords: list, tensor_name: str):
        layout = QVBoxLayout()
        self.inputs = []
        
        for i in range(dim):
            row = QHBoxLayout()
            row_inputs = []
            for j in range(dim):
                input_widget = self.create_input_widget(i, j, tensor_name)
                row_inputs.append(input_widget)
                row.addWidget(input_widget)
            self.inputs.append(row_inputs)
            layout.addLayout(row)
        
        self.setLayout(layout)
    
    def create_input_widget(self, i: int, j: int, tensor_name: str) -> QTextEdit:
        widget = QTextEdit()
        widget.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 8px;
            }
            QTextEdit:focus {
                border: 1px solid #0099ff;
            }
        """)
        widget.setFixedHeight(60)
        widget.setPlaceholderText(f"{tensor_name}_{{i{i}i{j}}}")
        return widget

class EinsteinSolverWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api_config = APIConfig()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle('Einstein Field Equations Solver')
        self.setMinimumSize(1200, 800)
        self.apply_theme()
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Add dimension input
        dim_layout = QHBoxLayout()
        dim_label = QLabel("Dimensions:")
        self.dim_input = QSpinBox()
        self.dim_input.setRange(2, 4)
        self.dim_input.setValue(4)
        dim_layout.addWidget(dim_label)
        dim_layout.addWidget(self.dim_input)
        dim_layout.addStretch()
        layout.addLayout(dim_layout)
        
        # Add coordinates input
        coords_layout = QHBoxLayout()
        coords_label = QLabel("Coordinates (LaTeX, comma-separated):")
        self.coords_input = QLineEdit()
        self.coords_input.setPlaceholderText("t, r, \\theta, \\phi")
        coords_layout.addWidget(coords_label)
        coords_layout.addWidget(self.coords_input)
        layout.addLayout(coords_layout)
        
        # Add initialize button
        self.init_button = QPushButton("Initialize Tensor Inputs")
        self.init_button.clicked.connect(self.initialize_tensors)
        layout.addWidget(self.init_button)
        
        # Add tensor input area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: #1a1a1a; }")
        
        self.tensor_widget = QWidget()
        self.tensor_layout = QVBoxLayout(self.tensor_widget)
        scroll.setWidget(self.tensor_widget)
        layout.addWidget(scroll)
        
        # Add results area
        self.results = QTextEdit()
        self.results.setReadOnly(True)
        self.results.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 8px;
                font-family: monospace;
            }
        """)
        layout.addWidget(self.results)
        
        # Add solve button
        self.solve_button = QPushButton("Solve Einstein Field Equations")
        self.solve_button.clicked.connect(self.solve_equations)
        layout.addWidget(self.solve_button)
    
    def apply_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #1a1a1a; }
            QLabel { color: #e0e0e0; font-size: 14px; }
            QPushButton {
                background-color: #0099ff;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #007acc; }
        """)
        
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(26, 26, 26))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(224, 224, 224))
        palette.setColor(QPalette.ColorRole.Base, QColor(43, 43, 43))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.Text, QColor(224, 224, 224))
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(224, 224, 224))
        self.setPalette(palette)
    
    def initialize_tensors(self):
        try:
            dim = self.dim_input.value()
            coords_text = self.coords_input.text()
            if not coords_text:
                raise ValueError("Please enter coordinates")
            
            coords = [c.strip() for c in coords_text.split(',')]
            if len(coords) != dim:
                raise ValueError(f"Number of coordinates must match dimensions ({dim})")
            
            # Clear previous tensor inputs
            for i in reversed(range(self.tensor_layout.count())): 
                self.tensor_layout.itemAt(i).widget().setParent(None)
            
            # Add metric tensor input
            metric_label = QLabel("Metric Tensor Components:")
            self.tensor_layout.addWidget(metric_label)
            self.metric_input = TensorInputWidget(dim, coords)
            self.tensor_layout.addWidget(self.metric_input)
            
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def solve_equations(self):
        try:
            dim = self.dim_input.value()
            coords = [c.strip() for c in self.coords_input.text().split(',')]
            
            # Create 2D list of metric components
            metric_components = []
            for i in range(dim):
                row = []
                for j in range(dim):
                    text = self.metric_input.inputs[i][j].toPlainText().strip()
                    if not text:
                        text = "0"
                    row.append(text)
                metric_components.append(row)
            
            metric_data = MetricData(
                components=metric_components,
                dimension=dim,
                coordinates=coords
            )
            
            # Convert to sympy Matrix
            metric = []
            for i in range(dim):
                row = []
                for j in range(dim):
                    try:
                        if metric_components[i][j] == "0":
                            row.append(sp.Integer(0))
                        else:
                            expr = latex2sympy(metric_components[i][j])
                            row.append(expr)
                    except:
                        row.append(sp.Integer(0))
                metric.append(row)
            
            metric_matrix = sp.Matrix(metric)
            
            # Create coordinate symbols
            coord_symbols = sp.symbols(' '.join(coords))
            
            # Create metric tensor
            metric_tensor = MetricTensor(metric_matrix, coord_symbols)
            einstein_tensor = EinsteinTensor.from_metric(metric_tensor)
            
            results = {
                'metric': metric_matrix,
                'einstein_tensor': einstein_tensor.tensor(),
                'ricci_scalar': einstein_tensor.ricci_scalar(),
                'christoffel_symbols': metric_tensor.christoffels()
            }
            
            self.display_results(results)
                
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def display_results(self, results: dict):
        self.results.clear()
        self.results.append("=== Calculation Results ===\n")
        self.results.append("Metric Tensor:")
        self.results.append(str(results['metric']))
        self.results.append("\nEinstein Tensor:")
        self.results.append(str(results['einstein_tensor']))
        self.results.append("\nRicci Scalar:")
        self.results.append(str(results['ricci_scalar']))
        self.results.append("\nChristoffel Symbols:")
        self.results.append(str(results['christoffel_symbols']))