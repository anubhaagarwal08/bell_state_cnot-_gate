from qiskit import QuantumCircuit, transpile, ClassicalRegister, QuantumRegister
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

service = QiskitRuntimeService()
backend = service.least_busy(
    operational=True,
    simulator=False
)



q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')

circuit = QuantumCircuit(q, c)

circuit.h(q[0])          # Create superposition
circuit.cx(q[0], q[1])   # Entangle the qubits

circuit.measure(q, c)

# Optimize the circuit for the selected hardware
pm = generate_preset_pass_manager(
    optimization_level=1,
    backend=backend
)

isa_circuit = pm.run(circuit)

# Create the Sampler
sampler = Sampler(mode=backend)

# Run on the quantum computer
job = sampler.run([isa_circuit], shots=1024)

print("Job ID:", job.job_id())

# Get the result
result = job.result()[0]

print(result.data)

bit_array = result.data.c

counts = bit_array.get_counts()

print(counts)

