{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Basic Usage

```
from {{ cookiecutter.project_slug }} import {{ cookiecutter.model_file_class_name }}
print( 'model file path is %s' % ( {{ cookiecutter.model_file_class_name }}.get_model_file_path() ) )
```

## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
