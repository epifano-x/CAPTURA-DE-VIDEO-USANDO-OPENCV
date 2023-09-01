import subprocess

# Comando para executar o arquivo webcam_capture.py
comando = ["python", "webcam_capture.py"]

# Iniciar a execução do webcam_capture.py como um processo separado
subprocess.Popen(comando)

# Se você desejar manter o main.py aberto ou adicionar mais funcionalidades aqui, você pode fazê-lo
# por exemplo, você pode criar uma interface gráfica para controlar ou interagir com o webcam_capture.py
