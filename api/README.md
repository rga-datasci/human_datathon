# Leveleando nuestro modelo de Machine Learning
## Demo para la Human Datathon 2022 by RGA

En el root (`/api`) encontrarás todos los scripts necesarios para poder disponibilizar un servicio de API REST en 
Google Cloud Run.

Elementos necesarios:
- Cuenta de GCP
- Crear una service account con privilegios suficientes para deployear imagenes a container registry y para deployear 
en Cloud Run
  
Variablea de entorno a setear:
```shell
API_KEY=<API KEY A ELECCION>
PROJECT_ID=<INSERTE SU PORJECTO DE GCP>
GOOGLE_APPLICATION_CREDENTIALS=<SERVICE ACCOUNT FILE>
```
