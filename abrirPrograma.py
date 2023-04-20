import subprocess

procesos = []

for i in range(1):
    
    proceso = subprocess.Popen("notepad.exe")
    procesos.append(proceso)
    
for proceso in procesos:
    
    proceso.wait()