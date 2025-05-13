# Prepare python environment
pip install -r src/requirements.txt

# Prepare MongoDB Dev DB
chmod +x ./.devcontainer/installMongoDB.sh
./.devcontainer/installMongoDB.sh