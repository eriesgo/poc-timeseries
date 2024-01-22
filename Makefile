# Makefile
check-types:
	mypy flask_server

lint:
	pylint --rcfile=./flask_server/pylintrc flask_server/*.py