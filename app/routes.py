from flask import Flask, request, jsonify, current_app as app, render_template
from .models import Rule
from . import db
from .utils import Node, parse_rule_string, combine_rules, evaluate_ast, dict_to_node
import json
import logging

# app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/combine')
def combine():
    return render_template('combine.html')

@app.route('/evaluate')
def evaluate():
    return render_template('evaluate.html')


@app.route('/create_rule', methods=['GET', 'POST'])
def create_rule():
    if request.method == 'POST':
        try:
            # Ensure the request is JSON and contains the 'rule_string' key
            if not request.is_json:
                return jsonify({'error': 'Request must be JSON'}), 400

            data = request.get_json()
            if 'rule_string' not in data:
                return jsonify({'error': 'Missing rule_string in request'}), 400

            rule_string = data['rule_string']
            ast = parse_rule_string(rule_string)
            ast_json = json.dumps(ast.to_dict(), indent=4)
            new_rule = Rule(rule_string=rule_string, ast_json=ast_json)
            db.session.add(new_rule)
            db.session.commit()
            return jsonify({'id': new_rule.id, 'ast': ast_json})
        except Exception as e:
            return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    return render_template('create_rule.html')



@app.route('/combine_rules', methods=['GET', 'POST'])
def combine_rules_endpoint():
    if request.method == 'POST':
        try:
            # Check if the request is JSON
            if not request.is_json:
                return jsonify({'error': 'Request must be JSON'}), 400

            data = request.get_json()
            if 'rule_ids' not in data:
                return jsonify({'error': 'Missing rule_ids in request'}), 400

            rule_ids = data['rule_ids']
            combined_ast = combine_rules(rule_ids)
            return jsonify(combined_ast)
        except Exception as e:
            return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    return render_template('combine.html')



@app.route('/evaluate_rule', methods=['GET', 'POST'])
def evaluate_rule():
    if request.method == 'POST':
        try:
            # Ensure the request is JSON
            if not request.is_json:
                return jsonify({'error': 'Request must be JSON'}), 400

            data = request.get_json()
            if 'ast' not in data or 'data' not in data:
                return jsonify({'error': 'Missing ast or data in request'}), 400

            ast_json = data['ast']
            evaluation_data = data['data']

            ast = dict_to_node(ast_json)
            result = evaluate_ast(ast, evaluation_data)
            return jsonify({'result': result})
        except KeyError:
            return jsonify({'error': 'Missing ast or data in request'}), 400
        except Exception as e:
            return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    return render_template('evaluate.html')



