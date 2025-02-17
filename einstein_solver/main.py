# In einstein_solver/main.py
import sys
from PyQt6.QtWidgets import QApplication
from einstein_solver.gui import EinsteinSolverWindow  # Changed from EinsteinSolverGUI

def main():
    """Application entry point"""
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = EinsteinSolverWindow()  # Changed from EinsteinSolverGUI
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()