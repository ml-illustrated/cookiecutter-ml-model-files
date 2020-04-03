# Cookiecutter template for packaging of ML model files

```
pip install cookiecutter
cookiecutter https://github.com/ml-illustrated/cookiecutter-ml-model-files
# fill in your project info

cd <name_of_your_project>
# add your model definition into <name_of_your_project>/__init__.py
# copy your model files into <name_of_your_project>/models
# ...

# build your python package
python setup.py bdist_wheel
```
