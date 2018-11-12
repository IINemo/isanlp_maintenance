from . import utils
from . import config as cfg
import os   
import time

script_dir = os.path.dirname(os.path.realpath(__file__))


def run_test(python_path, image_name, port, *args, **kwargs):
    utils.run_container_default(image_name, port, *args, **kwargs)
    utils.run_test_with_image(python_path, os.path.join(script_dir, 'test_default.py'), 
                              TEST_PORT=port)

    
def clean():
    utils.stop_container()
    