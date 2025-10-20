#!/bin/bash

# Start MongoDB service
sudo mongod --fork --logpath /var/log/mongodb/mongod.log

echo "MongoDB has been started successfully!"
mongod --version

# Run sample MongoDB commands
echo "Current databases:"
mongosh --eval "db.getMongo().getDBNames()"