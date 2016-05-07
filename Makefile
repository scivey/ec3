dist:
	python setup.py sdist upload

test:
	py.test ec3/test

clean:
	cd ec3 && find -name "*.pyc" | xargs rm -f
	cd ec3 && find -name "__pycache__" | xargs rm -rf
	rm -rf dist ec3.egg-info

.PHONY: dist test clean
