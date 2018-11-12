import os
from isanlp.processor_remote import ProcessorRemote
from isanlp.processor_syntaxnet_remote import ProcessorSyntaxNetRemote
from isanlp import PipelineCommon


port_morph = int(os.environ['TEST_MORPH_PORT'])
port_syntax = int(os.environ['TEST_SYNTAX_PORT'])
text_path = os.environ['TEST_PATH']

with open(text_path, encoding='utf8') as f:
    text = f.read()

    
ppl = PipelineCommon([(ProcessorRemote(host='localhost', 
                                       port=port_morph, 
                                       pipeline_name='default'), 
                       ['text'], 
                       {'tokens' : 'tokens',
                        'sentences' : 'sentences',
                        'lemma' : 'lemma',
                        'postag' : 'postag'}),
                      (ProcessorSyntaxNetRemote(host='localhost', 
                                                port=port_syntax), 
                       ['tokens', 'sentences'], 
                       {'syntax_dep_tree' : 'syntax_dep_tree'})
                     ])

annotations = ppl(text)
