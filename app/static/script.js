document.addEventListener('DOMContentLoaded', function () {
    const createRuleForm = document.getElementById('create-rule-form');
    const combineRulesForm = document.getElementById('combine-rules-form');
    const evaluateRuleForm = document.getElementById('evaluate-rule-form');

    if (createRuleForm) {
        createRuleForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const ruleString = document.getElementById('rule-string').value;
            fetch('/create_rule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ rule_string: ruleString })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('create-rule-result').innerText = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (combineRulesForm) {
        combineRulesForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const ruleIds = document.getElementById('rule-ids').value.split(',').map(id => parseInt(id.trim()));
            fetch('/combine_rules', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ rule_ids: ruleIds })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('combine-rules-result').innerText = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
        });
    }


    if (evaluateRuleForm) {
        evaluateRuleForm.addEventListener('submit', function (e) {
            e.preventDefault();
            ast = JSON.parse(document.getElementById('ast').value);
            data = JSON.parse(document.getElementById('data').value);
            fetch('/evaluate_rule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ast: ast, data: data })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('evaluate-rule-result').innerText = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
        });
    }
});


// document.addEventListener('DOMContentLoaded', function () {
//     const createRuleForm = document.getElementById('create-rule-form');
//     const combineRulesForm = document.getElementById('combine-rules-form');
//     const evaluateRuleForm = document.getElementById('evaluate-rule-form');

//     if (createRuleForm) {
//         createRuleForm.addEventListener('submit', function (e) {
//             e.preventDefault();
//             const ruleString = document.getElementById('rule_string').value;
//             fetch('/create_rule', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ rule_string: ruleString })
//             })
//             .then(response => response.json())
//             .then(data => {
//                 document.getElementById('create-rule-result').innerText = JSON.stringify(data, null, 2);
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     }

//     if (combineRulesForm) {
//         combineRulesForm.addEventListener('submit', function (e) {
//             e.preventDefault();
//             const ruleIds = document.getElementById('rule_ids').value.split(',').map(id => parseInt(id.trim()));
//             fetch('/combine_rules', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ rule_ids: ruleIds })
//             })
//             .then(response => response.json())
//             .then(data => {
//                 document.getElementById('combine-rules-result').innerText = JSON.stringify(data, null, 2);
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     }

//     if (evaluateRuleForm) {
//         evaluateRuleForm.addEventListener('submit', function (e) {
//             e.preventDefault();
//             const ast = JSON.parse(document.getElementById('ast').value);
//             const data = JSON.parse(document.getElementById('data').value);
//             fetch('/evaluate_rule', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ ast: ast, data: data })
//             })
//             .then(response => response.json())
//             .then(data => {
//                 document.getElementById('evaluate-rule-result').innerText = JSON.stringify(data, null, 2);
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     }
// });