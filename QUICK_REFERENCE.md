# numgraph - Quick Reference

## Installation
```bash
pip install numgraph  # Once published to PyPI
# OR
pip install git+https://github.com/ayushmishra/numgraph.git
```

## Basic Usage

### Simple Equation
```python
from numgraph import make_graph

graph = make_graph("x**2 + y**2 = 25", visualize=True)
```

### Save to File
```python
graph = make_graph("x**2 + y**2 = 25", save_path="output.html")
```

### Function with Range
```python
graph = make_graph("y = x**2 - 4*x + 3", 
                   func_range=(-2, 6), 
                   visualize=True)
```

## Advanced Usage

### Manual Control
```python
from numgraph.parser import EquationParser
from numgraph.graph_builder import GraphBuilder
from numgraph.visualizer import Visualizer

# Parse
parser = EquationParser("x**2 + y**2 = 25")
nodes, edges = parser.parse()

# Build
builder = GraphBuilder(nodes, edges)
graph = builder.build()

# Visualize
viz = Visualizer(graph, equation="x**2 + y**2 = 25")
viz.show_interactive()
viz.save_static("graph.png")
```

### Get Statistics
```python
stats = builder.get_stats()
# Returns: {
#   'num_nodes': ...,
#   'num_edges': ...,
#   'num_variables': ...,
#   'num_operators': ...,
#   'num_constants': ...,
#   'max_depth': ...
# }
```

### Export Graph
```python
builder.export_graphml("graph.graphml")
builder.export_gexf("graph.gexf")
```

## Supported Equation Types

✅ Algebraic: `x**2 + y**2 = 25`
✅ Functions: `y = x**2 - 4*x + 3`
✅ Linear: `y = 2*x + 3`
✅ Polynomials: `x**3 + 2*x**2 - 3*x + 1`
✅ Mixed: `x**2 + 2*x*y + y**2`
✅ Expressions: `2*x**2 + 3*x + 1` (no =)

## Tips

- Use `**` for exponents (not `^`)
- Wrap in quotes: `"x**2 + y**2 = 25"`
- Use `*` for multiplication: `2*x` not `2x`
- Variables can be any letter
- Supports: +, -, *, /, ** (power)

## Common Patterns

### Batch Processing
```python
equations = ["x**2 = 4", "y = 2*x", "x + y = 10"]
graphs = [make_graph(eq, save_path=f"graph_{i}.html") 
          for i, eq in enumerate(equations)]
```

### Error Handling
```python
try:
    graph = make_graph(user_equation)
except Exception as e:
    print(f"Invalid equation: {e}")
```

### Extract Variables
```python
variables = builder.get_variables()
# Returns: ['x', 'y', ...]
```

## Resources

- Full docs: [README.md](README.md)
- Examples: [examples/](examples/)
- API reference: [README.md#-api-reference](README.md#-api-reference)
- Usage guide: [USAGE_GUIDE.md](USAGE_GUIDE.md)

## Support

- Issues: https://github.com/ayushmishra/numgraph/issues
- Discussions: https://github.com/ayushmishra/numgraph/discussions
