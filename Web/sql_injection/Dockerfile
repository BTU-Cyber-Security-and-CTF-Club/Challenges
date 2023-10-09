FROM node:alpine3.18

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
COPY server.js /app/server.js
COPY public /app/public
COPY webapp.db /app/webapp.db

WORKDIR /app

RUN npm ci

EXPOSE 8080

CMD ["node", "server.js"]