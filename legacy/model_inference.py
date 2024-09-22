import tensorflow as tf
from tensorflow.lite.python.interpreter import Interpreter

# Cargar el modelo
interpreter = Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Preparar la entrada
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Ejecutar la inferencia
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Obtener el resultado
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)

