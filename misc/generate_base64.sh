#!/bin/bash
export $(grep -v '^#' envs/api.env | xargs)
export $(grep -v '^#' envs/psql.env | xargs)



DB_NAME=$(echo -n $DB_NAME | base64)
DB_USER=$(echo -n $DB_USER | base64)
DB_PASSWORD=$(echo -n $DB_PASSWORD | base64)
DB_HOST=$(echo -n $DB_HOST | base64)
DB_PORT=$(echo -n $DB_PORT | base64)
POSTGRES_DB=$(echo -n $POSTGRES_DB | base64)
POSTGRES_USER=$(echo -n $POSTGRES_USER | base64)
POSTGRES_PASSWORD=$(echo -n $POSTGRES_PASSWORD | base64)

cat <<EOF > k8s/utils/secrets.yml

apiVersion: v1
kind: Secret
metadata:
  name: db-secrets
  namespace: junior-test
type: Opaque
data:
  POSTGRES_DB: $POSTGRES_DB
  POSTGRES_USER: $POSTGRES_USER
  POSTGRES_PASSWORD: $POSTGRES_PASSWORD
---

apiVersion: v1
kind: Secret
metadata:
  name: api-secrets
  namespace: junior-test
type: Opaque
data:
  DB_NAME: $DB_NAME
  DB_USER: $DB_USER
  DB_PASSWORD: $DB_PASSWORD
  DB_HOST: $DB_HOST
  DB_PORT: $DB_PORT

EOF
