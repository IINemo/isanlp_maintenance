from . import utils
import os

script_dir = utils.script_dir(__file__)

def run_test(python_path, image_name, port):
    utils.run_container_default('inemo/isanlp', 
                                port, 
                                container_name='test_docker_isanlp')
    
    utils.run_container(image_name, 
                        '--shm-size=1024m -ti -p {}:9999'.format(port + 1), 
                        'server 0.0.0.0 9999', 
                        sleep_time=10)
    
    utils.run_test_with_image(python_path, 
                              os.path.join(script_dir, 'test_syntaxnet.py'), 
                              TEST_MORPH_PORT=port, 
                              TEST_SYNTAX_PORT=port + 1)

    
def clean():
    utils.stop_container()
    utils.stop_container('test_docker_isanlp')
    