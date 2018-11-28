from . import utils
from . import config as cfg
import os

script_dir = utils.script_dir(__file__)


def run_test(python_path, image_name, port):
    utils.run_container_default('inemo/isanlp',
                                port,
                                container_name='test_docker_isanlp')

    utils.run_container_default(image_name, port=port + 1, sleep_time=100)

    utils.run_test_with_image(python_path,
                              os.path.join(script_dir, 'test_deep_srl.py'),
                              test_text_path=cfg.TEST_EN_TEXT_PATH,
                              TEST_MORPH_PORT=port,
                              TEST_SRL_PORT=port + 1)


def clean():
    utils.stop_container('test_docker_isanlp')
    utils.stop_container()
