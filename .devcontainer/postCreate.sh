# Prepare python environment
pip install -r src/requirements.txt

# Prepare MongoDB Development DB
./.devcontainer/installMongoDB.sh
./.devcontainer/startMongoDB.sh