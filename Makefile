deps:
	pip install -r requirements.txt

generate:
	python generate.py

clean:

all: clean deps generate 
