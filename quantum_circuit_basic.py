from qiskit import QuantumCircuit, transpile, ClassicalRegister, QuantumRegister
qr=QuantumRegister(1,name="quantum")
cr=ClassicalRegister(1,name="classical")
qc=QuantumCircuit(qr,cr)
qc.draw("mpl", filename="quantum_circuit_basic.png")