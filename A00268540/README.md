### Examen 3
**Universidad ICESI**  
**Curso:** Sistemas Distribuidos  
**Docente:** Daniel Barrag�n C.  
**Tema:** Descubrimiento de servicios  
**Correo:** daniel.barragan at correo.icesi.edu.co

### Objetivos
* Realizar de forma aut�noma el aprovisionamiento autom�tico de infraestructura
* Diagnosticar y ejecutar de forma aut�noma las acciones necesarias para lograr infraestructuras estables

### Prerrequisitos
* Docker
* Docker-Compose
* Contenedores: consul, consul-template, registrator, load balancer (nginx, haproxy)

### Descripci�n
Deber� realizar el aprovisionamiento de un ambiente compuesto por los siguientes elementos:
un servidor web con capacidad de escalar a N instancias (puede	emplear	apache+php o crear	un servicio web con el	lenguaje de su preferencia), un balanceador de carga para redireccionar las peticiones a los servidores web.

Tenga en cuenta:
* Para el aprovisionamiento deber� usar docker-compose
* Emplear una herramienta de descubrimiento de servicio (zookeper, consul, etcd) que permita
registrar autom�ticamente las nuevas instancias de servidores web. Las tecnolog�as de descubrimiento de servicio se componen de agentes y un servidor � cl�ster de servidores. Los
agentes env�an informaci�n al cl�ster acerca de los servicios que se ejecutan en las instancias. El servidor registran los servicios que son anunciados por los agentes para ser consultados por los clientes � otros servicios
* Para evitar ejecutar mas de un servicio por contenedor (agente de consul y servicio web) emplee la aplicaci�n dockerizada registrator (� una tecnolog�a similar) para registrar los nuevos contenedores ante el servidor de descubrimiento de servicio
* Para actualizar la configuraci�n de los archivos de configuraci�n del balanceador de carga y reiniciar el servicio emplee la aplicaci�n consul-template. Consul-template consulta al servidor de consul el estado de los servicios y ante un cambio en ellos, a partir de plantillas, crea nuevamente los archivos de configuraci�n.

### Actividades
1. Documento en formato PDF:  
  * Formato PDF (5%)
  * Nombre y c�digo de los integrantes del grupo (5%)
  * Ortograf�a y redacci�n (5%)
2. Consigne los comandos de linux necesarios para el aprovisionamiento de los servicios solicitados. En este punto no debe incluir archivos tipo Dockerfile solo se requiere que usted identifique los comandos o acciones que debe automatizar (15%)
3. Escriba los archivos Dockerfile para cada uno de los servicios solicitados junto con los archivos fuente necesarios. Tenga en cuenta consultar buenas pr�cticas para la elaboraci�n de archivos Dockerfile. (20%)
4. Escriba el archivo docker-compose.yml necesario para el despliegue de la infraestructura (10%). No emplee configuraciones deprecated. Incluya un diagrama general de los componentes empleados.
5. El informe debe publicarse en un repositorio de github el cual debe ser un fork de https://github.com/ICESI-Training/sd-exam3 y para la entrega deber� hacer un Pull Request (PR) respetando la estructura definida. El c�digo fuente y la url de github deben incluirse en el informe (15%). Tenga en cuenta publicar los archivos para el aprovisionamiento
6. Incluya evidencias que muestran el funcionamiento de lo solicitado (15%)
7. Documente algunos de los problemas encontrados y las acciones efectuadas para su soluci�n al aprovisionar la infraestructura y aplicaciones (10%)

### Referencias
https://livewyer.io/blog/2015/02/05/service-discovery-docker-containers-using-consul-and-registrator/  
https://picodotdev.github.io/blog-bitix/2017/01/registro-y-descubrimiento-de-servicios-con-spring-cloud-y-consul/
