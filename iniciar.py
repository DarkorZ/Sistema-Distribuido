import subprocess
import webbrowser
def manage_docker():
    print("\n")
    print("---------------------John Serrano---------------------")
    print("--------------Proyecto 2do Parcial-------------------")
    print("------Sistema Distribuido Gestión de Pedidos--------")
    print("----Tecnologias Implementadas en el sistema:---------\n")
    print("---KAFKA----\n")
    print("---FLASk----\n")
    print("---MYSQL----\n")

    try:
        print("📌 Verificando si hay contenedores en ejecución...")
        subprocess.run("sudo docker ps -q | xargs -r sudo docker stop", shell=True, check=True)

        print("📌 Apagando servicios con docker-compose down...")
        subprocess.run("sudo docker-compose down", shell=True, check=True)
        

        print("📌 Construyendo y levantando docker-compose...")
        subprocess.run("sudo docker-compose up --build -d", shell=True, check=True)

        print("✅ Docker-compose ha sido ejecutado correctamente.")

        print("📂 Abriendo navegador en http://localhost:8080...")
        webbrowser.open("http://localhost:8080")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando Docker: {e}")
        exit(1)

# Ejecutar la función
manage_docker()
