cd /home/docker/code/src
python manage.py migrate --noinput
python manage.py collectstatic --noinput

supervisord -n -c /home/docker/code/deploy/supervisord.conf

