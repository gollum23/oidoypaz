build-docker-dev:
	cp requirements/base.txt docker/dev/base.txt
	cd docker/dev/ && docker build -t "mantis/oidoypaz-2020" .
	rm -rf docker/dev/base.txt

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop

ssh-dev:
	@docker exec -it -w /app oidoypaz zsh

build-docker-prod:
	cp requirements/base.txt docker/prod/base.txt
	cp requirements/prod.txt docker/prod/prod.txt
	cd docker/prod/ && docker build -t "mantis/oidoypaz" .
	rm -rf docker/prod/base.txt
	rm -rf docker/prod/prod.txt

start-prod:
	cd docker/prod/ && docker-compose up -d

stop-prod:
	cd docker/prod/ && docker-compose stop
