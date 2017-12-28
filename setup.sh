echo "Creando servicio uwsgi"
cp ./install/emperor.uwsgi.service /etc/systemd/system/

echo "Creando Carpetas uwsgi"
mkdir /etc/uwsgi
mkdir /etc/uwsgi/vassals

echo "Copiando configuracion uwsgi"
cp ./install/emperor.ini /etc/uwsgi

echo "Configurando logs uwsgi"
mkdir /var/log/uwsgi
chown -R www-data:www-data /var/log/uwsgi

echo "Agregando confguracion servicio kernkoa a uwsgi"
ln -s /usr/local/kernkoa/kernkoa_uwsgi.ini /etc/uwsgi/vassals/

echo "Desconectando Sitio por defecto de nginx"
rm /etc/nginx/sites-enabled/default

echo "Creando sitio de KernKoa"
ln -s /usr/local/kernkoa/kernkoa_nginx.conf /etc/nginx/sites-enabled/

echo "Activando Servicio UWSGI"
systemctl enable emperor.uwsgi.service
systemctl start emperor.uwsgi.service

echo "Reiniciando NGinX"
/etc/init.d/nginx restart
