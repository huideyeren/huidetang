FROM node:lts

ARG UID=1000
RUN mkdir /code && chown ${UID}:${UID} -R /code
USER ${UID}

WORKDIR /code

COPY package*.json ./
RUN yarn install

COPY . .

EXPOSE 3000

CMD [ "yarn", "dev" ]
