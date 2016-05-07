dist:
	python setup.py sdist upload

test:
	py.test ec2ssh2/test

clean:
	cd ec2ssh2 && find -name "*.pyc" | xargs rm -f
	cd ec2ssh2 && find -name "__pycache__" | xargs rm -rf
	rm -rf dist ec2ssh2.egg-info

.PHONY: dist test clean
