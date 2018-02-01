echo "Asign user permisions to www-data over kernkoa folder..."
chown -R www-data:www-data ../kernkoa

echo "Creating UWSGI service..."
cp ./install/emperor.uwsgi.service /etc/systemd/system/

echo "Crating UWSGI folders..."
mkdir /etc/uwsgi
mkdir /etc/uwsgi/vassals

echo "Copying UWSGI configuration file..."
cp ./install/emperor.ini /etc/uwsgi

echo "Configuring uwsgi Logs (/var/log/uwsgi/)..."
mkdir /var/log/uwsgi
chown -R www-data:www-data /var/log/uwsgi

echo "Configuring uwsgi Logs (/var/log/uwsgi/)..."
mkdir /var/log/celery
chown -R www-data:www-data /var/log/celery

echo "Adding Kernkoa to UWSGI Service..."
ln -s /usr/local/kernkoa/kernkoa_uwsgi.ini /etc/uwsgi/vassals/

echo "Deleting default NGinX sites..."
rm /etc/nginx/sites-enabled/default

echo "Creating KernKoa site in NGinX..."
ln -s /usr/local/kernkoa/kernkoa_nginx.conf /etc/nginx/sites-enabled/

echo "Activating UWSGI service"
systemctl enable emperor.uwsgi.service
systemctl start emperor.uwsgi.service

echo "Restarting NGinX Web Server"
/etc/init.d/nginx restart

echo "Success!!!.\n now you can try kernkoa writing server ip in any webbrowser.(http://<server ip>)"
