import pytest
import os

from {{ cookiecutter.project_slug }} import {{ cookiecutter.model_file_class_name }}

def test_get_model_path():
    model_file_path = {{ cookiecutter.model_file_class_name }}.get_model_file_path()

    assert os.path.exists( model_file_path ), 'Model file path does not exist!'
                
