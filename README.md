# ComfyUI Advanced Math Expression Node

An advanced math expression node for ComfyUI with support for infinite dynamic expressions and variable inputs.

## Features

- **Infinite Dynamic Expressions**: Add unlimited expression inputs via right-click menu
- **Variable Inputs**: Create custom variable inputs (a, b, c, x, y, etc.) that can be connected from other nodes
- **Cross-Expression References**: Reference previous expression results using `result_1`, `result_2`, etc.
- **Comprehensive Math Functions**: Includes trigonometric, logarithmic, and common mathematical operations
- **Multi-Line Expressions**: Each expression field supports multiple lines for complex calculations
- **Multiple Output Types**: Returns FLOAT, INT, and STRING for compatibility with various nodes

## Installation

1. Extract this folder to `ComfyUI/custom_nodes/`
2. Restart ComfyUI
3. Find the node under `math/advanced` category

## Usage

### Right-Click Menu Options
- **Add Expression**: Adds a new expression input field
- **Add Variable Input**: Creates a new variable input socket
- **Remove Last Expression**: Removes the most recently added expression

### Supported Functions
**Basic**: `+`, `-`, `*`, `/`, `**`, `%`
**Math**: `abs()`, `round()`, `min()`, `max()`, `pow()`, `sum()`, `sqrt()`, `floor()`, `ceil()`
**Trig**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`, `atan2()`
**Log**: `log()`, `log10()`, `exp()`
**Constants**: `pi`, `e`

### Example Expressions

**Expression 1**: `sqrt(a**2 + b**2)`  
**Expression 2**: `result_1 * pi`  
**Expression 3**: `sin(result_2) + cos(result_1)`

## License

MIT License
