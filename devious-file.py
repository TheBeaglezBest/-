from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute-python-code', methods=['POST'])
def execute_python_code():
    code = request.json['code']
    result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
    return jsonify({'output': result.stdout, 'error': result.stderr})

if __name__ == '__main__':
    app.run()
