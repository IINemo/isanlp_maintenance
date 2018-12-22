import os

from isanlp import PipelineCommon
from isanlp.processor_remote import ProcessorRemote

host = 'localhost'

port_morph = int(os.environ['TEST_MORPH_PORT'])
port_srl = int(os.environ['TEST_SRL_PORT'])
text_path = os.environ['TEST_EN_PATH']

with open(text_path, encoding='utf8') as f:
    text = f.read()

ppl = PipelineCommon([(ProcessorRemote(host=host,
                                       port=port_morph,
                                       pipeline_name='default'),
                       ['text'],
                       {'tokens': 'tokens',
                        'sentences': 'sentences',
                        'lemma': 'lemma',
                        'postag': 'postag'}),
                      (ProcessorRemote(host=host,
                                       port=port_srl,
                                       pipeline_name='default'),
                       ['tokens', 'sentences'],
                       {'srl': 'srl'})
                      ])

annotations = ppl(text)
