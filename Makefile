run:
	docker pull mcfly17/utoville-homecare-admin:dev
	docker stop admin
	docker run -d --name admin -p 8002:8002 docker/utoville-homecare-admin