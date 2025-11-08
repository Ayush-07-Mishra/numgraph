# How to Use numgraph in Your Project

This guide shows you how to integrate **numgraph** into your Python projects.

## Installation

### Option 1: Install from PyPI (Once Published)
```bash
pip install numgraph
```

### Option 2: Install from GitHub
```bash
pip install git+https://github.com/ayushmishra/numgraph.git
```

### Option 3: Install from Source
```bash
git clone https://github.com/ayushmishra/numgraph.git
cd numgraph
pip install .
```

## Basic Usage

### 1. Simple Equation Visualization

```python
from numgraph import make_graph

# Create and visualize a circle equation
graph = make_graph("x**2 + y**2 = 25", visualize=True)
```

### 2. Save Interactive HTML

```python
from numgraph import make_graph

# Save to a specific file
graph = make_graph(
    "x**2 + y**2 = 25",
    save_path="my_graph.html"
)
```

### 3. Function Plotting

```python
from numgraph import make_graph

# Plot a function with a range
graph = make_graph(
    "y = x**2 - 4*x + 3",
    func_range=(-2, 6),
    visualize=True
)
```

### 4. Advanced Usage

```python
from numgraph.parser import EquationParser
from numgraph.graph_builder import GraphBuilder
from numgraph.visualizer import Visualizer

# Parse equation
parser = EquationParser("x**2 + 2*x*y + y**2 = 16")
nodes, edges = parser.parse()

# Build graph
builder = GraphBuilder(nodes, edges)
graph = builder.build()

# Get statistics
stats = builder.get_stats()
print(f"Nodes: {stats['num_nodes']}")
print(f"Variables: {stats['num_variables']}")

# Visualize
viz = Visualizer(graph, equation="x**2 + 2*x*y + y**2 = 16")
viz.save_interactive("output.html")
viz.save_static("output.png")

# Export to graph formats
builder.export_graphml("graph.graphml")
builder.export_gexf("graph.gexf")
```

## Integration Examples

### In a Web Application (Flask)

```python
from flask import Flask, render_template, request
from numgraph import make_graph
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        equation = request.form['equation']
        output_path = os.path.join('static', 'graph.html')
        
        # Generate graph
        graph = make_graph(equation, save_path=output_path)
        
        return render_template('result.html', equation=equation)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### In a Jupyter Notebook

```python
from numgraph import make_graph
from IPython.display import IFrame

# Create graph
equation = "x**2 + y**2 = 25"
graph = make_graph(equation, save_path="graph.html")

# Display in notebook
IFrame('graph.html', width=800, height=600)
```

### In a Data Science Pipeline

```python
import pandas as pd
from numgraph import make_graph

def analyze_formulas(formulas_df):
    """Analyze a DataFrame of mathematical formulas"""
    results = []
    
    for idx, row in formulas_df.iterrows():
        equation = row['equation']
        
        # Create graph
        graph = make_graph(
            equation,
            save_path=f"graphs/equation_{idx}.html"
        )
        
        # Extract info
        variables = [d['label'] for _, d in graph.nodes(data=True) 
                    if d.get('type') == 'variable']
        
        results.append({
            'equation': equation,
            'num_nodes': graph.number_of_nodes(),
            'num_variables': len(set(variables)),
            'variables': list(set(variables))
        })
    
    return pd.DataFrame(results)

# Use it
formulas = pd.DataFrame({
    'equation': [
        'x**2 + y**2 = 25',
        'y = 2*x + 3',
        'y = x**2 - 4*x + 3'
    ]
})

analysis = analyze_formulas(formulas)
print(analysis)
```

### In an Educational Tool

```python
from numgraph import make_graph

class MathVisualizer:
    """Interactive math equation visualizer"""
    
    def __init__(self):
        self.history = []
    
    def visualize(self, equation, student_name="student"):
        """Visualize equation and save to student's folder"""
        
        # Create graph
        filename = f"students/{student_name}/{equation.replace(' ', '_')}.html"
        graph = make_graph(
            equation,
            save_path=filename,
            visualize=True
        )
        
        # Store history
        self.history.append({
            'student': student_name,
            'equation': equation,
            'graph': graph,
            'file': filename
        })
        
        # Generate report
        self._generate_report(graph, equation)
        
        return graph
    
    def _generate_report(self, graph, equation):
        """Generate analysis report"""
        variables = [d['label'] for _, d in graph.nodes(data=True) 
                    if d.get('type') == 'variable']
        
        print(f"Equation: {equation}")
        print(f"Variables: {set(variables)}")
        print(f"Complexity: {graph.number_of_nodes()} nodes")
        print(f"Graph saved!")

# Usage
viz = MathVisualizer()
viz.visualize("x**2 + y**2 = r**2", student_name="john")
```

### In Automated Documentation

```python
from numgraph import make_graph
import glob

def document_equations(code_dir, output_dir):
    """
    Extract and visualize all equations from code comments
    """
    # Find all Python files
    py_files = glob.glob(f"{code_dir}/**/*.py", recursive=True)
    
    equations = []
    for file in py_files:
        with open(file, 'r') as f:
            # Look for equations in comments
            for line in f:
                if '# EQUATION:' in line:
                    eq = line.split('# EQUATION:')[1].strip()
                    equations.append((file, eq))
    
    # Generate visualizations
    for file, equation in equations:
        filename = file.replace('/', '_').replace('.py', '')
        graph = make_graph(
            equation,
            save_path=f"{output_dir}/{filename}.html"
        )
        print(f"Documented: {equation} from {file}")

# Run it
document_equations("./src", "./docs/equations")
```

## Tips for Integration

1. **Error Handling**: Always wrap `make_graph()` in try-except blocks
   ```python
   try:
       graph = make_graph(user_equation)
   except Exception as e:
       print(f"Invalid equation: {e}")
   ```

2. **Validation**: Validate equations before processing
   ```python
   def is_valid_equation(eq_string):
       try:
           from numgraph.parser import EquationParser
           parser = EquationParser(eq_string)
           parser.parse()
           return True
       except:
           return False
   ```

3. **Batch Processing**: Process multiple equations efficiently
   ```python
   equations = ["x**2 = 4", "y = 2*x", "x + y = 10"]
   graphs = [make_graph(eq, save_path=f"graph_{i}.html") 
             for i, eq in enumerate(equations)]
   ```

4. **Custom Styling**: The HTML files can be customized with CSS

5. **Performance**: For large batches, consider using multiprocessing

## Requirements in Your Project

Add to your `requirements.txt`:
```
numgraph>=0.1.0
```

Or in `setup.py`:
```python
install_requires=[
    'numgraph>=0.1.0',
]
```

## Next Steps

- Check out the [examples/](examples/) directory
- Read the [API documentation](README.md#-api-reference)
- Join the discussion on GitHub Issues

Happy coding! 🚀
