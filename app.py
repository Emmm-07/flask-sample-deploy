from flask import Flask, render_template , request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


# Example route to perform an operation
@app.route('/perform_operation', methods=['POST'])
def perform_operation():
    # Extract data from the request
    data = request.json
    # Perform the operation (example operation: addition)
    result = data['num1'] + data['num2']
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)