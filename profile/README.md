# ASS-MUIT: Arquitecturas de Servicios Sanitarios

Esta organización GitHub alberga repositorios que servirán de apoyo para el curso de Arquitecturas de Servicios Sanitarios del Máster Universitario en Ingeniería de Telecomunicación de la Universidad de Sevilla

## Guía del Curso

**Introducción:**

Esta organización como punto central para el curso de Arquitecturas de Servicios Sanitarios. Aquí encontrarás repositorios originales y forks de interés en el curso.
Pueden proporcionar soporte para las prácticas o ejemplos relacionados con las tecnologías que utilizaremos. 

**Objetivos del Curso:**

El objetivo principal de este curso es proporcionar a los estudiantes una comprensión profunda de la arquitectura, diseño, desarrollo e integración de sistemas de información en el ámbito sanitario.  
Aprenderás a aplicar principios de SOA (Arquitectura Orientada a Servicios) y BPM (Gestión de Procesos de Negocio) para construir soluciones robustas, escalables e interoperables que satisfagan las necesidades del sector salud.

**Tecnologías Clave:**

A lo largo del curso, trabajaremos con las siguientes tecnologías:

* **jBPM:** Un motor de workflow de código abierto para la automatización de procesos de negocio. Aprenderemos a modelar, ejecutar y monitorizar procesos utilizando jBPM.
* **Business Central de KIE:** Una plataforma web para el desarrollo, despliegue y gestión de aplicaciones jBPM. Utilizaremos Business Central para diseñar y desplegar nuestros procesos.  
* **WSO2 Micro Integrator:** Una plataforma de integración ligera para conectar diferentes sistemas y aplicaciones.  Aprenderemos a crear APIs e integrar servicios utilizando Micro Integrator.
* **WSO2 Identity Server:** Una plataforma de gestión de identidades y accesos para asegurar el acceso a los recursos. Aprenderemos a configurar la autenticación y autorización utilizando Identity Server.
* **WSO2 Integration Studio:** El entorno de desarrollo para construir integraciones y APIs en la plataforma WSO2.


**Documentación de WSO2:**

Para ayudarte con el uso de los productos de WSO2, hemos recopilado algunos ejemplos y enlaces a la documentación oficial:

* **[Documentación oficial de WSO2 Micro Integrator](https://wso2.com/integration/micro-integrator/)**
* **[Documentación oficial de WSO2 Identity Server](https://wso2.com/identity-and-access-management/)**


**Documentación de jBPM:**

Para desplegar un proceso jBPM en Kie Server, sigue estos pasos:

1. **Construye tu proyecto:**  Empaqueta tu proyecto jBPM como un archivo .jar (kjart).
2. **Accede a la consola de Kie Server:** Abre la consola de administración de Kie Server en tu navegador. (normalmente `http://localhost:8080/kie-server/services/rest/server`)
3. **Despliega el kjart:** En la sección "Deployments", selecciona la opción para desplegar un nuevo archivo y sube tu archivo .jar.  
4. **Verifica el despliegue:** Asegúrate de que tu proceso esté desplegado correctamente en la sección "Containers"  verificando que se ha creado el contenedor correspondiente a la unidad de despliegue.  Puedes probar la ejecución del proceso instanciándolo en Business Central o a través de la API REST de Kie Server.

## Repositorios de trabajo en la organización github del curso (ASS-MUIT)

A continuación, se describe brevemente cada uno de los repositorios disponibles en la organización asshub en GitHub.  Recuerda que puedes acceder a ellos a través de la URL: [https://github.com/ASS-MUIT](https://github.com/ASS-MUIT)

* **Repositorio 1: [consultaNeurologica-kjar] ([https://github.com/ASS-MUIT/consultaNeurologica-kjar])**: Base de conocimiento utilizada en la práctica 1
* **Repositorio 2: [wih] ([https://github.com/ASS-MUIT/wih])**: Work Item Handler para la consulta de atributos de un recurso ``Appointment`` de FHIR
* **Repositorio 3: [kieServerApp] ([https://github.com/ASS-MUIT/kieServerApp])**: Aplicación jbpm que levanta un motor kie en modo development, controlado por bussiness central
* **Repositorio 4: [ICD] ([https://github.com/ASS-MUIT/ICD)])**: Base de conocimiento para la práctica de sistemas de términos

**Repositorios de referencia:**
Se incluyen también algunos repositorios adicionales de interés en la materia tratada en el curso. Se ha realizado un fork de los mismos, a los que puedes acceder a través de la URL: [https://github.com/ASS-MUIT](https://github.com/ASS-MUIT)
