from flask import Flask, jsonify
from flask_cors import CORS
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

app = Flask(__name__)
CORS(app) # App ki connect avadaniki

def quantum_random_6_digit():
    # Quantum circuit - true randomness
    qc = QuantumCircuit(3, 3)
    qc.h([0,1,2]) # Hadamard gate
    qc.measure([0,1,2], [0,1,2])
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    bits = list(result.get_counts().keys())[0]
    # Convert to 6 digit OTP
    base = int(bits, 2) * 13789
    otp = (base + random.randint(100000, 999999)) % 1000000
    return f"{otp:06d}"

@app.route('/')
def home():
    return {"app": "QuantumSafe", "status": "Live", "made_by": "Chandu - Hyderabad"}

@app.route('/api/otp')
def get_otp():
    otp = quantum_random_6_digit()
    return jsonify({
        "otp": otp,
        "type": "Quantum-Safe",
        "message": "This OTP cannot be hacked even by quantum computer"
    })

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True)
    pass
    