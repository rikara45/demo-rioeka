FROM nginx:alpine
COPY index.html robots.txt /usr/share/nginx/html/
COPY salon /usr/share/nginx/html/salon
COPY barbershop /usr/share/nginx/html/barbershop
COPY font /usr/share/nginx/html/font
EXPOSE 80
