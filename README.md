# **Sistema Distribuido de Gestión de Pedidos**  
Gestión eficiente de pedidos mediante un sistema distribuido, utilizando tecnologías modernas y un enfoque basado en contenedores.

---

## **Descripción del Proyecto**  
Este proyecto implementa un sistema distribuido para la gestión de pedidos con las siguientes características:  
- **Dashboard web interactivo**: Permite filtrar pedidos por sucursal y ordenarlos por fechas.  
- **Integración con Kafka**: Un *consumer* de Kafka procesa los mensajes de pedidos desde un *topic* dedicado.  
- **Persistencia de datos**: Los datos procesados se almacenan en una base de datos MySQL.  
- **Contenerización con Docker**: Todo el sistema está diseñado para ejecutarse en contenedores, con una configuración que incluye Nginx como servidor proxy inverso.  

---

## **Tecnologías Utilizadas**  
- **Backend**: Flask  
- **Mensajería distribuida**: Kafka  
- **Base de datos**: MySQL  
- **Proxy inverso**: Nginx  
- **Contenerización**: Docker  

---

## **Características Destacadas**  
- **Consumer Kafka**:  
  - Procesa mensajes del *topic* correspondiente.  
  - Almacena los datos de los pedidos en la base de datos MySQL.  
- **Dashboard web**:  
  - Visualiza los pedidos almacenados.  
  - Permite filtrado dinámico por sucursal y fechas.  
- **Configuración modular**:  
  - Todos los componentes están desplegados en contenedores Docker.  
  - Uso de volúmenes para la persistencia de datos.  

---

## **Estado Actual del Proyecto**  
- [x] Lógica del sistema actualizada (27/01/25).  
- [ ] Organización de contenedores y volúmenes pendientes.  
- [ ] Depuración de fallos y limpieza de archivos no utilizados.  

---

## **Capturas de Pantalla**  
> *(Incluye aquí capturas relevantes como el dashboard o el flujo del sistema.)*

### Dashboard Web  
![Dashboard](assets/dashboard_web.png)  

### Flujo del Sistema Distribuido  
![Flujo del Sistema](assets/flujo_sistema.png)  

---

## **Instrucciones de Instalación y Uso**  
1. **Clonar el repositorio**:  
   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
