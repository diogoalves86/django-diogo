up:
	docker run -d --name django-app -v /var/www/html:/home/docker/code/app dockerfiles/django-uwsgi-nginx
bash:
	docker exec -it django-app bash