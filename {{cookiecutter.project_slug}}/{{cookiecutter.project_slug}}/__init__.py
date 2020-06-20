import os, inspect

class {{ cookiecutter.model_file_class_name }}(object):

    def __init__( self ):
        pass

    @staticmethod
    def get_model_file_path():
        model_path = os.path.join( os.path.dirname(inspect.getfile( {{ cookiecutter.model_file_class_name }} )), 'models' )
        return os.path.join( model_path, 'my_model_file.checkpoint' )


'''
from {{ cookiecutter.project_slug }} import {{ cookiecutter.model_file_class_name }}
print( 'model file path is %s' % ( {{ cookiecutter.model_file_class_name }}.get_model_file_path() ) )
'''
