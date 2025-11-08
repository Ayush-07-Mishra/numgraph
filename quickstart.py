#!/usr/bin/env python3
"""
Quick Start Guide for numgraph
Run this script to see numgraph in action!
"""

def main():
    print("=" * 70)
    print("Welcome to numgraph! 🔢➡️📊")
    print("=" * 70)
    print()
    
    # Check if dependencies are installed
    try:
        from numgraph import make_graph
        print("✓ numgraph is installed correctly!")
    except ImportError as e:
        print("❌ Error: Dependencies not installed")
        print(f"   {e}")
        print()
        print("Please install dependencies:")
        print("  pip install -r requirements.txt")
        print("  or")
        print("  pip install -e .")
        return
    
    print()
    print("Let's create some graphs!")
    print("-" * 70)
    
    # Example 1: Simple circle equation
    print("\n[Example 1] Circle Equation: x**2 + y**2 = 25")
    print("-" * 70)
    try:
        graph1 = make_graph("x**2 + y**2 = 25", save_path="quickstart_circle.html")
        print(f"✓ Graph created with {graph1.number_of_nodes()} nodes")
        print("✓ Saved as 'quickstart_circle.html' - open in browser!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Example 2: Quadratic function
    print("\n[Example 2] Quadratic Function: y = x**2 - 4*x + 3")
    print("-" * 70)
    try:
        graph2 = make_graph("y = x**2 - 4*x + 3", save_path="quickstart_quadratic.html")
        print(f"✓ Graph created with {graph2.number_of_nodes()} nodes")
        print("✓ Saved as 'quickstart_quadratic.html'")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Example 3: Complex expression
    print("\n[Example 3] Complex Expression: 2*x**2 + 3*x*y + y**2")
    print("-" * 70)
    try:
        graph3 = make_graph("2*x**2 + 3*x*y + y**2", save_path="quickstart_complex.html")
        print(f"✓ Graph created with {graph3.number_of_nodes()} nodes")
        print("✓ Saved as 'quickstart_complex.html'")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    print("=" * 70)
    print("🎉 All done! Check the generated HTML files.")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  • Open the HTML files in your browser")
    print("  • Check out the examples/ directory for more")
    print("  • Read the API documentation in README.md")
    print("  • Try your own equations!")
    print()
    print("Happy graphing! 📊")

if __name__ == "__main__":
    main()
