# Cookiecutter template for packaging of ML model files

```
pip install cookiecutter
cookiecutter https://github.com/ml-illustrated/cookiecutter-ml-model-files
# fill in your project info

cd <name_of_your_project>
# add your model definition into <name_of_your_project>/__init__.py
# copy your model files into <name_of_your_project>/models
# ...

# run the test
pip install -r requirements_dev.txt

pip install -e .
pytest tests/test_model.py

# if needed, update the package version
bumpversion --current-version <current version> minor setup.py <name_of_your_project>/__init__.py


# build your python package
python setup.py sdist bdist_wheel

# test packages before uploading to PyPI
twine check dist/*

# Test upload packages to TestPyPI, note that it has separate account from production PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Publish your package to production PyPI
twine upload dist/*
```
