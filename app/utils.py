import re
from .models import Rule

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        if self.type == 'operand':
            return {
                "type": self.type,
                "left": self.left,
                "right": self.right,
                "value": self.value
            }
        elif self.type == 'operator':
            return {
                "type": self.type,
                "left": self.left.to_dict(),
                "right": self.right.to_dict(),
                "value": self.value
            }

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.to_dict() == other.to_dict()
        return False

    def __hash__(self):
        return hash(str(self.to_dict()))

def dict_to_node(d):
    if d['type'] == 'operand':
        return Node(type=d['type'], left=d['left'], right=d['right'], value=d['value'])
    elif d['type'] == 'operator':
        return Node(type=d['type'], left=dict_to_node(d['left']), right=dict_to_node(d['right']), value=d['value'])

def tokenize(rule_string):
    # Tokenize the rule string
    tokens = re.findall(r'\(|\)|\w+|[><=]+|AND|OR|\'[^\']*\'', rule_string)
    return tokens

def parse_tokens(tokens):
    def parse_expression(index):
        stack = []
        while index < len(tokens):
            token = tokens[index]
            if token == '(':
                node, index = parse_expression(index + 1)
                stack.append(node)
            elif token == ')':
                break
            elif token in ('AND', 'OR'):
                operator = token
                left = stack.pop()
                right, index = parse_expression(index + 1)
                stack.append(Node(type='operator', left=left, right=right, value=operator))
            else:
                # Operand (e.g., age > 30)
                if re.match(r'\w+', token):
                    left_operand = token
                    operator = tokens[index + 1]
                    right_operand = tokens[index + 2]
                    index += 2
                    stack.append(Node(type='operand', left=left_operand, right=int(right_operand) if right_operand.isdigit() else right_operand.strip("'"), value=operator))
            index += 1
        return stack[0], index

    root, _ = parse_expression(0)
    return root

def parse_rule_string(rule_string):
    tokens = tokenize(rule_string)
    ast = parse_tokens(tokens)
    return ast

def evaluate_ast(ast, data):
    if ast.type == 'operator':
        left_val = evaluate_ast(ast.left, data)
        right_val = evaluate_ast(ast.right, data)
        if ast.value == 'AND':
            return left_val and right_val
        elif ast.value == 'OR':
            return left_val or right_val
    elif ast.type == 'operand':
        left_val = data.get(ast.left)
        right_val = ast.right
        if ast.value == '==':
            return left_val == right_val
        elif ast.value == '!=':
            return left_val != right_val
        elif ast.value == '<':
            return left_val < right_val
        elif ast.value == '<=':
            return left_val <= right_val
        elif ast.value == '>':
            return left_val > right_val
        elif ast.value == '>=':
            return left_val >= right_val
    return False

def combine_rules(rule_ids):
    unique_asts = set()
    for rule_id in rule_ids:
        rule = Rule.query.get(rule_id)
        if rule:
            ast = parse_rule_string(rule.rule_string)
            unique_asts.add(ast)
    
    if not unique_asts:
        return {"combined_ast": None}
    
    combined_ast = None
    for ast in unique_asts:
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node(type='operator', left=combined_ast, right=ast, value='AND')
    
    return {"combined_ast": combined_ast.to_dict()}
