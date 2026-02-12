# ComfyUI Advanced Math Expression Node

An advanced math expression node for ComfyUI with support for infinite dynamic expressions and variable inputs.
<img width="1370" height="766" alt="image" src="https://github.com/user-attachments/assets/fd0d7311-ba0b-4cd2-8815-84bbcdda9b2f" />

## Features

- **Infinite Dynamic Inputs**: Connect unlimited numeric inputs (a, b, c, d, etc.) from other nodes
- **Multiple Expression Fields**: Add expression_2, expression_3, etc. for intermediate calculations
- **Cross-Expression References**: Use `result_2`, `result_3`, etc. in expression_1 to combine calculations
- **Comprehensive Math Functions**: Trigonometric, logarithmic, and common mathematical operations
- **Multi-Line Expressions**: Each expression field supports multiple lines for complex calculations
- **Multiple Output Types**: Returns FLOAT, INT, and STRING for compatibility with various nodes
- **Error Resilient**: Failed expressions return 0 and display errors in console without breaking the node

## Installation

1. Clone or download this repository to `ComfyUI/custom_nodes/ComfyUI-Advanced-Math-Expression/`
2. Restart ComfyUI
3. Find the node under `math/advanced` category as "Advanced Math Expression ∞"

## How It Works

### Evaluation Order
1. **First Pass**: Evaluates expression_2, expression_3, expression_4, etc. (in order)
   - Results are stored as `result_2`, `result_3`, `result_4`, etc.
2. **Second Pass**: Evaluates expression_1 with all `result_N` values available
3. **Output**: Returns the result from expression_1

### Dynamic Variable Inputs
- Connect any number of inputs by linking to the input sockets (a, b, c, d, etc.)
- These can be added from the right click menu
- Supports INT, FLOAT, and STRING inputs

### Expression Fields
- **expression_1** (main field): Final calculation that can reference all `result_N` values
- **expression_2, expression_3, etc.**: Intermediate calculations accessed via context menu

### Supported Functions
**Operators**: `+`, `-`, `*`, `/`, `**` (power), `%` (modulo)
**Basic Math**: `abs()`, `round()`, `min()`, `max()`, `pow()`, `sum()`
**Advanced Math**: `sqrt()`, `floor()`, `ceil()`
**Trigonometry**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`, `atan2()`
**Logarithms**: `log()`, `log10()`, `exp()`
**Hyperbolic**: `sinh()`, `cosh()`, `tanh()`
**Conversions**: `radians()`, `degrees()`
**Constants**: `pi`, `e`

## Examples

### Example 1: Simple Calculation
```
Inputs: a=6, b=67, c=77

expression_2: a + b       # Result: 73, stored as result_2
expression_3: a + b       # Result: 73, stored as result_3
expression_1: result_2 + result_3   # Output: 146
```

### Example 2: Pythagorean Theorem
```
Inputs: a=3, b=4

expression_2: a**2        # Result: 9, stored as result_2
expression_3: b**2        # Result: 16, stored as result_3
expression_1: sqrt(result_2 + result_3)   # Output: 5.0
```

### Example 3: Multi-Step Calculation
```
Inputs: x=10, y=20

expression_2: x * 2       # Result: 20, stored as result_2
expression_3: y / 2       # Result: 10, stored as result_3
expression_4: result_2 + result_3   # Result: 30, stored as result_4
expression_1: result_4 * pi         # Output: 94.248...
```

### Example 4: Multi-Line Expression
```
expression_2:
  # Calculate area of circle
  radius = a
  radius**2 * pi

expression_1: result_2 * 2   # Double the area
```

## Tips

- Variable names are case-sensitive: use lowercase `result_2`, not `Result_2`
- Errors are printed to the console but won't break the node (returns 0)
- Use expression_2+ for intermediate steps, expression_1 for final output
- Comments in expressions start with `#`
- Multi-line expressions evaluate line by line, returning the last result

## License

MIT License
