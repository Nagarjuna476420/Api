'''from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the addition function
def add_numbers(a, b):
    return a + b

# Define the API route for GET request
@app.route('/add', methods=['GET'])
def add_api():
    try:
        # Get parameters from the query string
        a = request.args.get('a', type=float)  # 'a' should be a float
        b = request.args.get('b', type=float)  # 'b' should be a float

        # Validate inputs
        if a is None or b is None:
            return jsonify({'error': 'Missing parameters a or b'}), 400

        # Perform the addition operation
        result = add_numbers(a, b)

        # Return the result
        return jsonify({'result': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)'''
    
    
    
from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
# Define your API routes
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Global API!'})
 
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"name": "John Doe", "age": 30, "city": "New York"}
    return jsonify(sample_data)
 
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"received": data})
 
if __name__ == '__main__':
    # Bind to all public IPs
    app.run(host='0.0.0.0', port=5000)
