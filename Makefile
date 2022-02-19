.PHONY: server devserver schema model

server:
	uvicorn modules.app.main:app

devserver:
	uvicorn modules.app.main:app --reload

schema:
	curl http://localhost:8000/openapi.json -o openapi.json

model:
	python modules/flower/create_iris_model.py