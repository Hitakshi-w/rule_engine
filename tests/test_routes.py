import pytest
from app import create_app, db
from app.models import Rule

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_rule(client):
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    response = client.post('/create_rule', json={'rule_string': rule_string})
    assert response.status_code == 200
    assert 'ast' in response.json

def test_create_rule_invalid(client):
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing') AND (salary > 50000 OR experience > 5)"
    response = client.post('/create_rule', json={'rule_string': rule_string})
    assert response.status_code == 400
    assert 'error' in response.json

def test_combine_rules(client):
    rule_strings = [
        "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
        "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    ]
    rule_ids = [client.post('/create_rule', json={'rule_string': rs}).json['id'] for rs in rule_strings]
    response = client.post('/combine_rules', json={'rule_ids': rule_ids})
    assert response.status_code == 200
    assert 'combined_ast' in response.json

def test_combine_rules_invalid(client):
    response = client.post('/combine_rules', json={'rule_ids': "invalid"})
    assert response.status_code == 400
    assert 'error' in response.json

def test_evaluate_rule(client):
    ast = client.post('/create_rule', json={'rule_string': "age > 30"}).json['ast']
    data = {"age": 35}
    response = client.post('/evaluate_rule', json={'ast': ast, 'data': data})
    assert response.status_code == 200
    assert response.json['result'] == True

def test_evaluate_rule_invalid(client):
    ast = client.post('/create_rule', json={'rule_string': "age > 30"}).json['ast']
    data = "invalid"
    response = client.post('/evaluate_rule', json={'ast': ast, 'data': data})
    assert response.status_code == 400
    assert 'error' in response.json

if __name__ == '__main__':
    pytest.main()