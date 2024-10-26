import json
from utils import parse_rule_string

def test_parse_rule_string():
    # Define the rule string
    rule_string = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"

    try:
        # Parse the rule string
        ast_root = parse_rule_string(rule_string)

        # Print the AST as a dictionary
        ast_dict = ast_root.to_dict()
        print(json.dumps(ast_dict, indent=4))

        # Expected output
        expected_output = {
            "type": "operator",
            "left": {
                "type": "operator",
                "left": {
                    "type": "operator",
                    "left": {
                        "type": "operand",
                        "left": "age",
                        "right": 30,
                        "value": ">"
                    },
                    "right": {
                        "type": "operand",
                        "left": "department",
                        "right": "Sales",
                        "value": "=="
                    },
                    "value": "AND"
                },
                "right": {
                    "type": "operator",
                    "left": {
                        "type": "operand",
                        "left": "age",
                        "right": 25,
                        "value": "<"
                    },
                    "right": {
                        "type": "operand",
                        "left": "department",
                        "right": "Marketing",
                        "value": "=="
                    },
                    "value": "AND"
                },
                "value": "OR"
            },
            "right": {
                "type": "operator",
                "left": {
                    "type": "operand",
                    "left": "salary",
                    "right": 50000,
                    "value": ">"
                },
                "right": {
                    "type": "operand",
                    "left": "experience",
                    "right": 5,
                    "value": ">"
                },
                "value": "OR"
            },
            "value": "AND"
        }

        # Check if the output matches the expected output
        assert ast_dict == expected_output, "The parsed AST does not match the expected output."

        print("Test passed!")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_parse_rule_string()