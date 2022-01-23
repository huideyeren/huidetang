FROM node:lts-slim

ARG UID=1000
RUN mkdir /srv/app && chown ${UID}:${UID} -R /srv/app

USER ${UID}

WORKDIR /srv/app

COPY package*.json ./
RUN yarn install

COPY . .

EXPOSE 1337

CMD [ "yarn", "develop" ]
# CMD ["node", "server.js"]
