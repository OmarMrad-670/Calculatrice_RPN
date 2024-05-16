# Utilisez l'image de base Python
FROM python:3.9

# Copiez le code de votre application dans le conteneur
COPY . /app
WORKDIR /app

# Installez les dépendances
RUN pip install -r requirements.txt

# Exposez le port sur lequel l'application FastAPI fonctionne
EXPOSE 8000

# Commande pour démarrer l'application FastAPI
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
