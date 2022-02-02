FROM node:lts
WORKDIR /code

ARG UID=1000
RUN mkdir /src/app && chown ${UID}:${UID} -R /src/app
USER ${UID}

WORKDIR /src/app

COPY package*.json ./
RUN yarn install

COPY . .

EXPOSE 3000

CMD [ "yarn", "dev" ]
