# TODO: add custom tests

###########################################################

import os

###########################################################
    
import logging

logPath = './'
fileName = 'main.log'
logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

fileHandler = logging.FileHandler(os.path.join(logPath, fileName))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

logger.setLevel(logging.INFO)

###########################################################   

if __name__ == "__main__":
    import argparse
    import importlib
    import test_docker.config as cfg
    import test_docker.utils as utils
    
    parser = argparse.ArgumentParser(description='Test IsaNLP containers.')
    parser.add_argument('-w', '--workdir', default='workdir', 
                        help='workdir to run tests in.')
    parser.add_argument('-g', '--gittag', default='', 
                        help='name of the github tag.')
    parser.add_argument('-b', '--branch', default='master', 
                        help='name of a branch.')
    parser.add_argument('-d', '--dockertag', default='latest', 
                        help='name of a docker tag.')
    parser.add_argument('test', nargs='*', help='name of tests.', default=[])

    args = parser.parse_args()

    if args.gittag:
        args.branch = args.gittag

    tmp_index = {e['image_name'] : i for i, e in enumerate(cfg.DOCKER_MODULE_LIST)}
    module_list = cfg.DOCKER_MODULE_LIST if not args.test else [cfg.DOCKER_MODULE_LIST[tmp_index[e]] 
                                                                   for e in args.test]
    for i, module in enumerate(module_list):
        module_list[i]['image_name'] = '{}:{}'.format(module['image_name'], args.dockertag)
        
        
        
#############################################################################

    from test_docker import run_test_default
    
    try:
        repo_path = os.path.join(args.workdir, 'repo')
        utils.checkout_working_copy(repo_path, args.branch)
    except:
        pass
    
    stat_positive = 0
    
    for module in module_list:
        try:
            logger.info('------------- Testing module: {} ...'.format(module['image_name']))
            
            utils.pull_docker_image(module['image_name'])
            
            test = importlib.import_module('test_docker.' + module['test_script'], '')
            python_path = os.path.abspath(os.path.join(repo_path, 'src'))
            test.run_test(python_path, module['image_name'], cfg.DEFAULT_PORT)
            stat_positive += 1
            
        except RuntimeError as expt:
            logger.info('Error during testing module: {}.'.format(module['image_name']))
            logger.info('Test script return code is: {}.'.format(expt))
            
        finally:
            try:
                test.clean()
            except:
                pass
    
    logger.info('=============== Summary: ')
    logger.info('Tests successfull: {}/{}.'.format(stat_positive, len(module_list)))
    
#############################################################################
            
# TODO: need wrapper scripts for each image.
# They should be put in tests of each component.
# For the matter of quickness create testing scripts for each container in this project.
    