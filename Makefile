BUILD_NAME=gymkhana-acac
BUILD_TAG=$$(git log -1 --pretty=%h)

build:
	@docker build -t ${BUILD_NAME}-backend:${BUILD_TAG} -t ${BUILD_NAME}-backend:latest -f acac_backend/Dockerfile acac_backend

.env:
	@cp .env.example .env

dev-up: .env
	@docker-compose up

dev-up-bg: .env
	@docker-compose up -d

dev-stop:
	@docker-compose down

dev-logs:
	@docker-compose logs -f

ex-django:
	@docker exec -it $$(echo "$$(docker ps --filter "name=django")" | awk 'NR > 1 {print $$1}') sh

ex-vue:
	@docker exec -it $$(echo "$$(docker ps --filter "name=vue")" | awk 'NR > 1 {print $$1}') sh

ex-postgresql:
	@docker exec -it $$(echo "$$(docker ps --filter "name=postgresql")" | awk 'NR > 1 {print $$1}') sh