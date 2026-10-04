FROM nginx:alpine
COPY index.html robots.txt /usr/share/nginx/html/
COPY salon /usr/share/nginx/html/salon
COPY barbershop /usr/share/nginx/html/barbershop
COPY img /usr/share/nginx/html/img
EXPOSE 80
