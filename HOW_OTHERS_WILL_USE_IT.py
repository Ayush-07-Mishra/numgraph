"""
EXAMPLE: How Other Developers Will Use numgraph in Their Projects
==================================================================

This file shows real-world examples of how developers will integrate
numgraph into their own projects after installing it via pip.
"""

# =============================================================================
# EXAMPLE 1: Student Learning App
# =============================================================================

class MathTutor:
    """A tutoring app that uses numgraph to help students"""
    
    def teach_equation(self, equation):
        from numgraph import make_graph
        
        # Create visualization for the student
        graph = make_graph(equation, save_path=f"student_lesson.html")
        
        # Extract info to explain to student
        variables = [d['label'] for _, d in graph.nodes(data=True) 
                    if d.get('type') == 'variable']
        
        print(f"📚 In this equation: {equation}")
        print(f"   Variables: {set(variables)}")
        print(f"   Complexity: {graph.number_of_nodes()} components")
        print(f"   📊 Open 'student_lesson.html' to see the graph!")


# =============================================================================
# EXAMPLE 2: Research Paper Equation Documenter
# =============================================================================

def document_research_equations(paper_equations):
    """Generate visualizations for all equations in a research paper"""
    from numgraph import make_graph
    
    results = []
    for i, eq in enumerate(paper_equations, 1):
        # Create visualization for each equation
        graph = make_graph(eq, save_path=f"figures/equation_{i}.html")
        
        results.append({
            'number': i,
            'equation': eq,
            'visualization': f"equation_{i}.html",
            'nodes': graph.number_of_nodes()
        })
    
    # Generate LaTeX table for the paper
    print("\\begin{table}")
    print("\\caption{Equation Visualizations}")
    for r in results:
        print(f"Equation {r['number']}: {r['equation']} "
              f"(Complexity: {r['nodes']} nodes)")
    print("\\end{table}")
    
    return results


# =============================================================================
# EXAMPLE 3: Web API Service
# =============================================================================

from flask import Flask, request, send_file, jsonify
from numgraph import make_graph
import os

app = Flask(__name__)

@app.route('/api/visualize', methods=['POST'])
def visualize_equation():
    """API endpoint to visualize equations"""
    data = request.json
    equation = data.get('equation')
    
    if not equation:
        return jsonify({'error': 'No equation provided'}), 400
    
    try:
        # Generate visualization
        output_path = f"temp/{hash(equation)}.html"
        graph = make_graph(equation, save_path=output_path)
        
        # Return file URL
        return jsonify({
            'success': True,
            'url': f'/download/{hash(equation)}.html',
            'nodes': graph.number_of_nodes(),
            'edges': graph.number_of_edges()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# =============================================================================
# EXAMPLE 4: Jupyter Notebook Analysis
# =============================================================================

def analyze_formulas_notebook():
    """Example for use in Jupyter notebooks"""
    from numgraph import make_graph
    from IPython.display import IFrame, display
    import pandas as pd
    
    # List of formulas to analyze
    formulas = [
        "E = m*c**2",
        "F = G*m1*m2/r**2",
        "a**2 + b**2 = c**2"
    ]
    
    # Analyze each
    for formula in formulas:
        print(f"\n{'='*60}")
        print(f"Analyzing: {formula}")
        print('='*60)
        
        # Create graph
        graph = make_graph(formula, save_path=f"{formula.replace('=', '_')}.html")
        
        # Display in notebook
        display(IFrame(f"{formula.replace('=', '_')}.html", width=800, height=400))


# =============================================================================
# EXAMPLE 5: Command Line Tool
# =============================================================================

def cli_tool():
    """Command-line equation visualizer"""
    import sys
    from numgraph import make_graph
    
    if len(sys.argv) < 2:
        print("Usage: python equation_viz.py 'x**2 + y**2 = 25'")
        return
    
    equation = sys.argv[1]
    print(f"Visualizing: {equation}")
    
    # Generate
    graph = make_graph(equation, visualize=True, save_path="output.html")
    
    print(f"✓ Complete! Open 'output.html' in your browser.")
    print(f"  Nodes: {graph.number_of_nodes()}")
    print(f"  Edges: {graph.number_of_edges()}")


# =============================================================================
# EXAMPLE 6: Educational Dashboard
# =============================================================================

class EquationDashboard:
    """Interactive dashboard for equation exploration"""
    
    def __init__(self):
        from numgraph import make_graph
        self.make_graph = make_graph
        self.history = []
    
    def add_equation(self, equation, student_name):
        """Add an equation to student's learning history"""
        
        # Create visualization
        filename = f"dashboard/{student_name}_{len(self.history)}.html"
        graph = self.make_graph(equation, save_path=filename)
        
        # Store metadata
        self.history.append({
            'student': student_name,
            'equation': equation,
            'timestamp': __import__('datetime').datetime.now(),
            'file': filename,
            'complexity': graph.number_of_nodes()
        })
        
        print(f"✓ Added {equation} for {student_name}")
        return graph
    
    def generate_report(self, student_name):
        """Generate learning report for a student"""
        student_data = [h for h in self.history if h['student'] == student_name]
        
        print(f"\n📊 Report for {student_name}")
        print(f"   Total equations studied: {len(student_data)}")
        print(f"   Average complexity: {sum(h['complexity'] for h in student_data) / len(student_data):.1f}")
        print(f"\n   Equations:")
        for i, h in enumerate(student_data, 1):
            print(f"   {i}. {h['equation']} (complexity: {h['complexity']})")


# =============================================================================
# EXAMPLE 7: Data Science Pipeline
# =============================================================================

def analyze_model_equations():
    """Analyze mathematical formulas used in ML models"""
    from numgraph import make_graph
    import pandas as pd
    
    # Model equations
    equations = {
        'Linear Regression': 'y = w*x + b',
        'MSE Loss': 'L = (y_pred - y_true)**2',
        'Sigmoid': 'sigma = 1/(1 + e**(-x))',
        'ReLU': 'f = x' # max(0, x) simplified
    }
    
    results = []
    for name, eq in equations.items():
        graph = make_graph(eq, save_path=f"models/{name.replace(' ', '_')}.html")
        
        results.append({
            'model': name,
            'equation': eq,
            'complexity': graph.number_of_nodes()
        })
    
    # Create DataFrame
    df = pd.DataFrame(results)
    print(df)
    
    return df


# =============================================================================
# EXAMPLE 8: Auto-Documentation Generator
# =============================================================================

def auto_document_codebase(source_dir):
    """Find equations in code comments and visualize them"""
    from numgraph import make_graph
    import os
    
    equations_found = []
    
    # Scan Python files
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r') as f:
                    for line_num, line in enumerate(f, 1):
                        # Look for equation markers
                        if '# EQUATION:' in line or '# FORMULA:' in line:
                            eq = line.split(':')[1].strip()
                            equations_found.append({
                                'file': filepath,
                                'line': line_num,
                                'equation': eq
                            })
    
    # Visualize all found equations
    print(f"Found {len(equations_found)} equations in codebase")
    
    for i, eq_data in enumerate(equations_found):
        filename = f"docs/equations/eq_{i}.html"
        graph = make_graph(eq_data['equation'], save_path=filename)
        
        print(f"  {eq_data['file']}:{eq_data['line']}")
        print(f"    {eq_data['equation']}")
        print(f"    → {filename}\n")


# =============================================================================
# HOW TO RUN THESE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("numgraph - Real World Integration Examples")
    print("=" * 70)
    print()
    print("These examples show how developers will use numgraph in their projects.")
    print()
    print("After installing with: pip install numgraph")
    print()
    print("They can simply import and use:")
    print()
    
    # Show simple usage
    from numgraph import make_graph
    
    print("Example 1: Simple equation visualization")
    print("-" * 70)
    graph = make_graph("x**2 + y**2 = 25", save_path="demo_output.html")
    print(f"✓ Created graph with {graph.number_of_nodes()} nodes")
    print(f"✓ Saved to 'demo_output.html'")
    print()
    
    print("Example 2: Using in a class")
    print("-" * 70)
    tutor = MathTutor()
    tutor.teach_equation("y = 2*x + 3")
    print()
    
    print("=" * 70)
    print("That's how easy it is to use numgraph! 🎉")
    print("=" * 70)
