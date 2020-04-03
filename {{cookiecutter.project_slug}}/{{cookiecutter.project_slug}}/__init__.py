import os, inspect

class MyModelFileClassName(object):

    def __init__( self ):
        pass

    @staticmethod
    def get_model_file_path():
        model_path = os.path.join( os.path.dirname(inspect.getfile( MyModelFileClassName )), 'models' )
        return os.path.join( model_path, 'my_model_file.checkpoint' )


'''
from {{ cookiecutter.project_slug }} import MyModelFileClassName
print( 'model file path is %s' % ( MyModelFileClassName.get_model_file_path() ) )
'''
