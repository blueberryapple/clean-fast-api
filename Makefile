.PHONY: server devserver schema

server:
	uvicorn modules.app.main:app

devserver:
	uvicorn modules.app.main:app --reload

schema:
	curl http://localhost:8000/openapi.json -o openapi.json