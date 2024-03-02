while ! nc -z db 3307
do
	echo "Waiting for the MySQL Server"
	sleep 3
done

python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi --ini /var/www/html/myproject/uwsgi.ini&&
tail -f /dev/null
exec "$@"
