# ASS-MUIT: Healthcare Service Architectures

This GitHub organization hosts repositories supporting the Healthcare Service Architectures course within the Master's Degree in Telecommunication Engineering at the University of Seville.

## Course Guide

**Introduction:**

This organization serves as the central hub for the Healthcare Service Architectures course.  Here you'll find original repositories and forks relevant to the course.  These provide support for practical exercises and examples related to the technologies we'll be using.

**Course Objectives:**

The primary objective of this course is to provide students with a deep understanding of the architecture, design, development, and integration of information systems in the healthcare sector. You will learn to apply principles of SOA (Service-Oriented Architecture) and BPM (Business Process Management) to build robust, scalable, and interoperable solutions that meet the needs of the healthcare industry.

**Key Technologies:**

Throughout the course, we will work with the following technologies:

* **jBPM:** An open-source workflow engine for business process automation. We will learn to model, execute, and monitor processes using jBPM.
* **KIE Business Central:** A web platform for the development, deployment, and management of jBPM applications. We will use Business Central to design and deploy our processes.
* **WSO2 Micro Integrator:** A lightweight integration platform for connecting different systems and applications. We will learn to create APIs and integrate services using Micro Integrator.
* **WSO2 Identity Server:** An identity and access management platform to secure access to resources. We will learn to configure authentication and authorization using Identity Server.
* **WSO2 Integration Studio:** The development environment for building integrations and APIs on the WSO2 platform.


**WSO2 Documentation:**

To assist you with using WSO2 products, we have compiled some examples and links to the official documentation:

* **[Official WSO2 Micro Integrator Documentation](https://wso2.com/integration/micro-integrator/)**
* **[Official WSO2 Identity Server Documentation](https://wso2.com/identity-and-access-management/)**


**jBPM Documentation:**

To deploy a jBPM process to Kie Server, follow these steps:

1. **Build your project:** Package your jBPM project as a .jar (kjart) file.
2. **Access the Kie Server console:** Open the Kie Server administration console in your browser (typically `http://localhost:8080/kie-server/services/rest/server`).
3. **Deploy the kjart:** In the "Deployments" section, select the option to deploy a new file and upload your .jar file.
4. **Verify deployment:** Ensure your process is deployed correctly in the "Containers" section by verifying that the container corresponding to the deployment unit has been created. You can test the process execution by instantiating it in Business Central or via the Kie Server REST API.


## Course GitHub Organization Repositories (ASS-MUIT)

Below is a brief description of each repository available in the asshub organization on GitHub. Remember that you can access them via the URL: [https://github.com/ASS-MUIT](https://github.com/ASS-MUIT)

* **Repository 1: [consultaNeurologica-kjar] ([https://github.com/ASS-MUIT/consultaNeurologica-kjar])**: Knowledge base used in Practice 1.
* **Repository 2: [wih] ([https://github.com/ASS-MUIT/wih])**: Work Item Handler for querying attributes of an ``Appointment`` resource from FHIR.
* **Repository 3: [kieServerApp] ([https://github.com/ASS-MUIT/kieServerApp])**: jBPM application that starts a Kie engine in development mode, controlled by Business Central.
* **Repository 4: [ICD] ([https://github.com/ASS-MUIT/ICD])**: Knowledge base for the terminology systems practice.


**Reference Repositories:**
Several additional repositories of interest related to the course material are also included. Forks of these repositories are available via the URL: [https://github.com/ASS-MUIT](https://github.com/ASS-MUIT)
