FROM node:12-alpine as build-stage

WORKDIR /app

COPY package*.json ./
# RUN npm install -g @vue/cli

RUN npm install


COPY . .

# Command to run the application
CMD ["npm", "run", "serve"]
