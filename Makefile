# create environment
init:
	python -m venv venv

# activate, and install dependencies
install:
    ( \
      source ./venv/Scripts/activate; \
      pip install -r requirements.txt; \
    )