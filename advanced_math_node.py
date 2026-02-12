import math

class ContainsAnyDict(dict):
    def __contains__(self, key):
        return True

    def __getitem__(self, key):
        # If key exists in the actual dict, return it
        if dict.__contains__(self, key):
            return dict.__getitem__(self, key)
        # Otherwise return a default input type for dynamic variables
        # This handles inputs like a, b, c, d, etc.
        return ("INT,FLOAT,STRING", {"forceInput": True})

class AdvancedMathExpressionNode:
    """
    Advanced Math Expression Node with infinite dynamic inputs
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": ContainsAnyDict({
                "expression_1": ("STRING", {
                    "multiline": True,
                    "default": "a + b"
                }),
            }),
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO"
            }
        }

    RETURN_TYPES = ("FLOAT", "INT", "STRING")
    RETURN_NAMES = ("float_result", "int_result", "string_result")
    FUNCTION = "evaluate_expressions"
    CATEGORY = "math/advanced"
    OUTPUT_NODE = False

    def evaluate_expressions(self, **kwargs):
        """
        Evaluates all dynamic math expressions and returns combined results
        """
        results = []
        expression_results = {}

        # Safe math context with common functions
        safe_dict = {
            '__builtins__': {},
            'abs': abs, 'round': round, 'min': min, 'max': max,
            'pow': pow, 'sum': sum,
            'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos,
            'tan': math.tan, 'asin': math.asin, 'acos': math.acos,
            'atan': math.atan, 'atan2': math.atan2,
            'log': math.log, 'log10': math.log10, 'exp': math.exp,
            'floor': math.floor, 'ceil': math.ceil,
            'pi': math.pi, 'e': math.e,
            'radians': math.radians, 'degrees': math.degrees,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
        }

        # Separate expressions from variable inputs
        expressions = {}
        variables = {}

        for key, value in kwargs.items():
            if key.startswith('expression_'):
                expressions[key] = value
            elif key not in ['unique_id', 'extra_pnginfo', 'prompt']:
                # These are variable inputs (a, b, c, etc.)
                variables[key] = value

        # Add variables to safe context
        safe_dict.update(variables)

        # Sort expressions by number to maintain order
        sorted_expressions = sorted(expressions.items(),
                                   key=lambda x: int(x[0].split('_')[1]))

        # First pass: evaluate expressions 2+ to populate result_2, result_3, etc.
        # This allows expression_1 to reference these results
        for expr_name, expr_string in sorted_expressions:
            if expr_name == 'expression_1':
                continue  # Skip expression_1 in first pass

            if not expr_string or expr_string.strip() == "":
                continue

            try:
                # Allow multi-line expressions
                lines = expr_string.strip().split('\n')
                result = None

                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    # Evaluate the line
                    result = eval(line, safe_dict, safe_dict)

                    # Store result with expression name for cross-referencing
                    expr_num = expr_name.split('_')[1]
                    safe_dict[f'result_{expr_num}'] = result

                if result is not None:
                    expression_results[expr_name] = result

            except Exception as e:
                print(f"Error evaluating {expr_name}: {str(e)}")
                print(f"Expression was: {expr_string}")

        # Second pass: evaluate expression_1 with all result_N available
        if 'expression_1' in expressions:
            expr_string = expressions['expression_1']
            if expr_string and expr_string.strip() != "":
                try:
                    lines = expr_string.strip().split('\n')
                    result = None

                    for line in lines:
                        line = line.strip()
                        if not line or line.startswith('#'):
                            continue

                        result = eval(line, safe_dict, safe_dict)
                        safe_dict['result_1'] = result

                    if result is not None:
                        results.append(result)
                        expression_results['expression_1'] = result

                except Exception as e:
                    print(f"Error evaluating expression_1: {str(e)}")
                    print(f"Expression was: {expr_string}")
                    results.append(0)
                    expression_results['expression_1'] = 0

        # Collect all results in order for final output
        for expr_name, _ in sorted_expressions:
            if expr_name in expression_results:
                if expr_name != 'expression_1':  # expression_1 already added
                    results.append(expression_results[expr_name])

        # Return result from expression_1 if it exists, otherwise last result
        final_result = expression_results.get('expression_1', results[-1] if results else 0)

        # Convert to appropriate types
        float_result = float(final_result)
        int_result = int(final_result)
        string_result = f"{final_result}"

        return (float_result, int_result, string_result)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Always re-evaluate when inputs change
        return float("NaN")

# Node registration
NODE_CLASS_MAPPINGS = {
    "AdvancedMathExpression": AdvancedMathExpressionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AdvancedMathExpression": "Advanced Math Expression ∞"
}
