## Requirements

- Ubuntu WSL 2 (optional)
- Visual studio code (optional)
- Virtualenv Python (optional)
- Google Cloud Platform Account
- Google Cloud Platform - API Cloud Build

## Install Google Cloud CLI

```
* sudo apt-get update
* sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo
* echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
* curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add –
* sudo apt-get update && sudo apt-get install google-cloud-cli
```

## Deploy Model

```
Navigate to the modeldeploy folder:
* gcloud init
* gcloud builds submit --tag gcr.io/glassfit/predict_face
<<glassfit is the project ID and predict_face is the Flask endpoint name in main.py>>
Example:
@app.route('/predict_face', methods=['POST'])
* gcloud run deploy --image gcr.io/glassfit/predict_face --platform managed
```
