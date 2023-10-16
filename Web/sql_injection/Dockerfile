FROM node:alpine3.18

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
COPY server.js /app/server.js
COPY generate_db.js /app/generate_db.js
COPY public /app/public

WORKDIR /app

RUN npm ci
# For some reason this has to be run twice to create DB, otherwise it'll crash
RUN node generate_db.js
RUN node generate_db.js

EXPOSE 8080

CMD ["node", "server.js"]