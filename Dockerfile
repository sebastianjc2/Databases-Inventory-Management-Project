FROM postgres
ENV POSTGRES_DB dcfajr03gbu43b
ENV POSTGRES_USER rfuunoitsqrvhu
ENV POSTGRES_PASSWORD ad03f3262f921e6a03acbf5a2def6d79b298b9e3e732e33a641e359e141e69b3
COPY schema.sql /docker-entrypoint-initdb.d/