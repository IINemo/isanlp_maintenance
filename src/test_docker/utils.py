from . import config as cfg
import os
import time
import logging

logger = logging.getLogger()


def script_dir(fl):
    return os.path.dirname(os.path.realpath(fl))


def run(s):
    logger.info('Command: {}'.format(s))
    ret = os.system(s)
    if ret != 0:
        raise RuntimeError(ret)


def pull_docker_image(image_name):
    run('docker pull {}'.format(image_name))


def run_container(image_name, 
                  container_params, 
                  exe_params, 
                  container_name=cfg.DOCKER_TEST_CONTAINER, 
                  sleep_time=1):
    logger.info('Starting docker container...')
    run('docker run --rm -d --name={} {} {} {}'.format(container_name,
                                                       container_params,
                                                       image_name,  
                                                       exe_params))
    time.sleep(sleep_time)
    logger.info('Container started.')
    

def run_container_default(image_name, port, 
                          container_name=cfg.DOCKER_TEST_CONTAINER, 
                          sleep_time=cfg.DEFAULT_CONTAINER_TIMEOUT):
    run_container(image_name, 
                  '-p {0}:3333'.format(port), '', 
                  container_name=container_name,
                  sleep_time=sleep_time)


def run_test_with_image(repo_path, test_module, *args, **kwargs):
    logger.info('Running test...')
    env_vars = ' '.join(['{}={}'.format(k, v) for k,v in kwargs.items()])
    run('PYTHONPATH={} TEST_PATH={} {} {} {}'.format(repo_path, 
                                                     cfg.TEST_TEXT_PATH, 
                                                     env_vars,
                                                     cfg.PYTHON_BIN, 
                                                     test_module))
    logger.info('Test successfull.')


def checkout_working_copy(work_dir, branch_name):
    run('git clone --branch {} --single-branch {} {}'.format(branch_name, 
                                                             cfg.GITHUB_REPO, 
                                                             work_dir))


def stop_container(name=cfg.DOCKER_TEST_CONTAINER):
    run('docker rm -f {}'.format(name))
    