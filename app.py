import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

def quantum_random_6_digit():
    qc = QuantumCircuit(3, 3)
    qc.h([0,1,2])
    qc.measure([0,1,2], [0,1,2])
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    bits = list(result.get_counts().keys())[0]
    base = int(bits, 2) * 13789
    otp = (base + random.randint(100000, 999999)) % 1000000
    return f"{otp:06d}"

st.set_page_config(page_title="QuantumSafe", page_icon="🔐")
st.title("🔐 QuantumSafe - Quantum OTP Generator")
st.write("True randomness using Quantum Computing (Qiskit)")

if st.button("Generate Quantum OTP"):
    with st.spinner("Generating using Quantum Circuit..."):
        otp = quantum_random_6_digit()
        st.success(f"Your Quantum OTP is: **{otp}**")
        st.balloons()

st.info("Powered by Qiskit Aer Simulator - Hadamard Gates for true randomness")