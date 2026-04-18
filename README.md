# cicd-pipeline-python


1. ¿Qué ventajas le proporciona a un proyecto el uso de un pipeline de CI? Menciona al menos tres ventajas específicas y explica por qué son importantes.

    - Elimina el error humano e incrementa la velocidad de desarrollo
    - Valida el codigo rapidamente detectanto así errores, bugs y/o malas practicas
    - Se asegura una alta calidad del código y una consistencia en todo el ciclo del desarrollo


2. ¿Cuál es la diferencia principal entre una prueba unitaria y una prueba de aceptación? Da un ejemplo de algo que probarías con una prueba unitaria y algo que probarías con una prueba de aceptación (en el contexto de cualquier aplicación que conozcas, descríbela primero).

    - **Prueba unitaria**: Solo se encarga de validar una función con un resultado esperado en un modulo especifico, en un ambiente aislado y seguro.

    - **Pueba de Aceptación**: Valida el comportamiento completo de la aplicación desde la perspectiva del usuario y/o del negocio.

    Ejemplos:

    - **Unitaria**: probar que sumar(2, 3) retorne 5 en el módulo de lógica de cálculo.
    - **Aceptación**: levantar la app, enviar una operación desde la interfaz (o endpoint) y verificar que el resultado mostrado al usuario sea correcto y con el formato esperado.

3. Describe brevemente qué hace cada uno de los steps principales de tu workflow de GitHub Actions (desde el checkout hasta el push de Docker). Explica el propósito de cada uno (qué hace y para qué se hace).

    - **Checkout**
    Descarga el código del repositorio en el runner para poder trabajar sobre él.

    - **Set up Python**
    Configura Python 3.12 en el entorno de ejecución.

    - **Install dependencies**
    Actualiza pip e instala lo definido en requirements.txt; prepara el ambiente para análisis y pruebas.

    - **Run Black**
    Verifica formato de código sin modificar archivos. Su objetivo es forzar un estilo consistente.

    - **Run Pylint**
    Analiza calidad estática del código y genera el reporte, pero sin detener el pipeline.

    - **Run Flake8**
    Ejecuta reglas de estilo/errores y guarda el reporte, pero sin detener el pipeline.


    - **Run Unit Tests**
    Ejecuta pruebas unitarias excluyendo la de aceptación. Valida la lógica interna de la aplicación.

    - **Run Acceptance Tests**
    Levanta la app con Gunicorn, y ejecuta pruebas de aceptación contra la URl de la app. Además genera reportes de cobertura y HTML para evidencia.

    - **Upload Test Reports Artifacts**
    Publica reportes como artefactos del workflow para revisión posterior.

    - **SonarCloud Scan**
        Envía el análisis a SonarCloud para evaluación de calidad, mantenibilidad y posibles vulnerabilidades.

    - **Set up QEMU**
        Habilita emulación para builds multi-arquitectura de Docker cuando sea necesario.

    - **Set up Docker Buildx**
        Configura el builder moderno de Docker con capacidades avanzadas de cache y build.

    - **Login to Docker Hub**
        Autentica contra Docker Hub con variables/secrets para poder publicar imágenes.

    - **Build and push Docker image**
        Construye la imagen con Dockerfile y la publica. También usa cache de GitHub Actions para acelerar builds futuros.


4. ¿Qué problemas o dificultades encontraste al implementar este taller? ¿Cómo los solucionaste? (Si no encontraste ningún problema, describe algo nuevo que hayas aprendido).

Con la realización de este taller entendimos cómo se integran diferentes tecnologías dentro de un solo pipeline para asegurar que un código cumpla con la calidad y las buenas prácticas que se suelen exigir en el mundo real. No lo vemos como algo que nos ralentice en nuestro flujo de trabajo. Por el contrario, lo consideramos un conjunto de herramientas que, aunque pueden tener una curva de aprendizaje, posteriormente nos benefician e incrementan nuestra conciencia sobre la metodología DevOps.

Además, uno de nosotros trabaja diariamente con SonarQube, pero gracias a este taller pudo comprender mejor cómo se configura y se maneja esta herramienta.



5. ¿Qué ventajas ofrece empaquetar la aplicación en una imagen Docker al final del pipeline en lugar de simplemente validar el código?


    - **Portabilidad real**
    La imagen incluye aplicación, dependencias y configuración base. Se ejecuta igual en diferentes entornos (local, servidor, nube).

    -  **Despliegue más confiable y repetible**
    En vez de reconstruir el entorno manualmente, se despliega exactamente el mismo artefacto generado por CI.

    - **Trazabilidad de versiones**
    Al etiquetar con sha y latest, se puede saber qué commit está en producción y hacer rollback con mayor control.

    - **Menor "works on my machine"**
    El entorno queda estandarizado dentro del contenedor, reduciendo diferencias entre máquinas de desarrollo y ejecución.