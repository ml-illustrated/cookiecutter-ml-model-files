{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```
pip install {{ cookiecutter.project_slug }}
```

## Basic Usage

```
from {{ cookiecutter.project_slug }} import {{ cookiecutter.model_file_class_name }}
print( 'model file path is %s' % ( {{ cookiecutter.model_file_class_name }}.get_model_file_path() ) )
```

## Credits

This package was created with _Cookiecutter_ and the `audreyr/cookiecutter-pypackage` project template.

- _Cookiecutter_: https://github.com/audreyr/cookiecutter
- `audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
- `cookiecutter-ml-model-files`: https://github.com/ml-illustrated/cookiecutter-ml-model-files
