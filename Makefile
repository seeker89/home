deps:
	pip install -r requirements.txt

generate:
	python generate.py

clean:

serve:
	python serve.py

all: clean deps generate 
