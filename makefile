APP_PACKAGE := app
WSGI_APP := $(APP_PACKAGE).wsgi:application
GUNICORN_DEV_CONF := config/gunicorn.dev.conf.py
GUNICORN_PROD_CONF := config/gunicorn.prod.conf.py

.PHONY: run
run:
	export FLASK_APP=$(APP_PACKAGE) && \
	export FLASK_ENV=development && \
	export FLASK_DEBUG=true && \
	flask run --host=0.0.0.0 --port=8000

.PHONY: start
start:
	gunicorn --config $(GUNICORN_DEV_CONF) $(WSGI_APP)

.PHONY: test
test:
	python -m unittest

.PHONY: lint
lint:
	pylint $(APP_PACKAGE)

.PHONY: shell
shell:
	export FLASK_APP=$(APP_PACKAGE).wsgi && \
	flask shell
