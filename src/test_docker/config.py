import os

DEFAULT_TEST = 'run_test_default'

DOCKER_MODULE_LIST = [
    dict(image_name='inemo/isanlp',
         test_script=DEFAULT_TEST),
    dict(image_name='inemo/isanlp_udpipe',
         test_script=DEFAULT_TEST),
    dict(image_name='inemo/syntaxnet_rus',
         test_script='run_test_syntaxnet'),
    dict(image_name='inemo/isanlp_srl_framebank',
         test_script='run_test_srl_framebank'),
    dict(image_name='inemo/isanlp_parser_conll2008',
         test_script='run_test_parser_conll2008'),
    dict(image_name='inemo/isanlp_deep_srl',  # built from (gh) source with this name
         test_script='run_test_deep_srl',
         is_local=True)
]


TEST_TEXT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                              '../../data/text_ru.txt')

TEST_EN_TEXT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              '../../data/text_en.txt')

GITHUB_REPO = 'https://github.com/IINemo/isanlp'


DOCKER_TEST_CONTAINER = 'docker_test'

DEFAULT_CONTAINER_TIMEOUT = 3

DEFAULT_PORT = 3333


try:
    os.system('python3 --help > /dev/null 2>&1')
except:
    PYTHON_BIN = 'python'
else:
    PYTHON_BIN = 'python3'
    
