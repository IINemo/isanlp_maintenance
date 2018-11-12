import os
from isanlp.processor_remote import ProcessorRemote

port = int(os.environ['TEST_PORT'])
text_path = os.environ['TEST_PATH']

with open(text_path, encoding='utf8') as f:
    text = f.read()

proc = ProcessorRemote(host='localhost', port=port, pipeline_name='default')
annotations = proc(text)
