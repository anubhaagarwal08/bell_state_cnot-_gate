from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# Create the simulator backend
backend = AerSimulator()

# Create quantum and classical registers
q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')

# Create the quantum circuit
circuit = QuantumCircuit(q, c)

# Create Bell State
circuit.h(q[0])
circuit.cx(q[0], q[1])

# Measure the qubits
circuit.measure(q, c)

# Draw the circuit
print("Quantum Circuit:")
print(circuit.draw())

# Compile for simulator
compiled_circuit = transpile(circuit, backend)

# Execute
job = backend.run(compiled_circuit, shots=1024)

# Get results
result = job.result()

counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)