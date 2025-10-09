# Estágio 1: Build da aplicação
FROM node:20 as build

WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Instalar as dependências
RUN npm install

# Copiar o resto do código da aplicação
COPY . .

# Gerar a build de produção
RUN npm run build

# Estágio 2: Servir os arquivos estáticos com um servidor leve
FROM nginx:stable-alpine

# Copiar os arquivos da build do estágio anterior
COPY --from=build /app/dist /usr/share/nginx/html

# Expor a porta 80, que é a porta padrão do Nginx
EXPOSE 80
