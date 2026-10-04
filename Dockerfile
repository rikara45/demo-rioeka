FROM nginx:alpine
COPY index.html 404.html 50x.html robots.txt /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY salon /usr/share/nginx/html/salon
COPY barbershop /usr/share/nginx/html/barbershop
COPY font /usr/share/nginx/html/font
EXPOSE 80
