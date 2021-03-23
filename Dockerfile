FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build
#RUN ROOT_API=http://scrapingproject.example.com npm run build
#RUN ROOT_API=http://35.225.142.4 npm run build
#RUN ROOT_API=http://localhost:8080 npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]