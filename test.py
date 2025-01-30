import onnx

model_path = "/path/to/your/model.onnx"
onnx_model = onnx.load(model_path)

for inp in onnx_model.graph.input:
    print(inp.name, inp.type)
