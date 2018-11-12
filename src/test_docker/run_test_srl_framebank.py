from . import utils
import os


script_dir = utils.script_dir(__file__)


def run_test(python_path, image_name, port):
    utils.run_container_default('inemo/isanlp', 
                                port, 
                                container_name='test_docker_isanlp')
    
    utils.run_container('inemo/syntaxnet_rus', 
                        '--shm-size=1024m -ti -p {}:9999'.format(port + 1), 
                        'server 0.0.0.0 9999', 
                        container_name='test_docker_syntaxnet',
                        sleep_time=1)
    
    utils.run_container_default(image_name, port=port + 2, sleep_time=100)
    
    utils.run_test_with_image(python_path, 
                              os.path.join(script_dir, 'test_srl_framebank.py'), 
                              TEST_MORPH_PORT=port, 
                              TEST_SYNTAX_PORT=port + 1,
                              TEST_SRL_PORT=port + 2)

    
def clean():
    utils.stop_container('test_docker_isanlp')
    utils.stop_container('test_docker_syntaxnet')
    utils.stop_container()
    