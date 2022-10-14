#!/usr/bin/env bash
gcloud builds submit --config pipeline.yaml
gcloud run deploy demo-datathon \
    --region us-central1 \
    --image gcr.io/${PROJECT_ID}/demo-datathon \
    --allow-unauthenticated \
    --set-env-vars API_KEY=$API_KEY
