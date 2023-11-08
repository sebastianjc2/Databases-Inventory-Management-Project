FROM postgres
ENV POSTGRES_DB sqlytes-inventory-app
ENV POSTGRES_USER docker_admin
ENV POSTGRES_PASSWORD postgresadmin
COPY Backend/schema.sql /docker-entrypoint-initdb.d/