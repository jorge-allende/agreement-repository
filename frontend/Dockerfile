# Frontend Dockerfile
FROM node:16
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["serve", "-s", "build"]
