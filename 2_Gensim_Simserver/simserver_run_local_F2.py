# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:34:49 2018

@author: afcarl
"""
import os, sys
import time
import math
from shutil import copyfile
import shutil

from gensim import utils
from simserver import SessionServer

import gensim
import wordninja

from collections import defaultdict

# Importing Gensim
#import gensim
from gensim import corpora


folder_A = './my_server_A'
try:
    shutil.rmtree( folder_A )
except:
    time.sleep(1)
        

folder_B = './my_server_B'
try:
    shutil.rmtree( folder_B )
except:
    time.sleep(1)
        

def zpickle( obj, fname ):
    import pickle, gzip
    pickle.dump(obj=obj, file=gzip.open(fname, 'wb', compresslevel=3), protocol=2)

def zunpickle( fname ):
    import pickle, gzip
    return pickle.load(gzip.open(fname, "rb"))
    

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

bad_terms_list = ['1grams', '18f', '100bin', '200bin', '45', '63', '170', '252', '35', '39', '57', '731', '98', '125977', '128', '136', '2012', '28', '32', '95','0000000000000000e', '005', '006969', '0688477', '07', '09', '1000', '101', '103', '103027', '11377', '1234', '13', '15', '159658', '16', '172', '1760', '19', '196', '2010', '21', '22831', '24', '25', '255', '2560', '291', '3000', '34', '36', '374', '382617', '40', '4096', '42', '48', '50', '500', '500000', '5050', '52', '5500', '558', '58', '59', '60000', '64', '65', '75', '80', '85', '87', '88', '89', '99', 'd', 'f', 'i', 't0', 't1', 'v', '0', '00', '000', '01', '02', '03', '04', '05', '06', '08', '1', '10', '100', '11', '12', '1272', '128104', '14', '17', '18', '2', '20', '200', '2011', '2013', '2014', '2015', '2016', '2017', '2018', '2138', '23', '250', '2d', '3', '300', '4', '5', '5629', '6', '7', '8', '9', 'afcarl', 'b', 'c', 'copyright', 'e', 'g', 'git', 'github', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'py', 'q', 'r', 's', 'u', 'v0', 'v1', 'v11', 'v17', 'v18', 'v2', 'v3', 'v4', 'v5', 'v9', 'w', 'x', 'z']

 
i_tag_num_threshold = 5




#===========================
#===========================
i_1000_flag = 1
#i_1000_flag = 0
#===========================
#===========================



        
#server = SessionServer('/tmp/my_server') # resume server (or create a new one)
#server = SessionServer('./my_server') # resume server (or create a new one)
#server = SessionServer('./my_server_A') # resume server (or create a new one)
server = SessionServer( folder_A ) # resume server (or create a new one)

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

logger = logging.getLogger('gensim.similarities.simserver')



def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()
# demo print
print('fate' in english_words)
print("type(english_words) = ", type(english_words))
print("len(english_words) = ", len(english_words))
#sys.exit(0)


#output_tmp = open( "simserver_run_local_C.out" , 'w' )
#output_tmp = open( "simserver_run_local_D.out" , 'w' )
#output_tmp = open( "simserver_run_local_E.out" , 'w' )
output_tmp = open( "simserver_run_local_F2.out" , 'w' )



#input_doc_text = open( "html_parse_E_ALL.txt" , 'r' )
#input_doc_text = open( "html_parse_F_ALL.txt" , 'r' )
if i_1000_flag == 0:
    input_doc_text = open( "html_parse_H_ALL.txt" , 'r' )
else:
    input_doc_text = open( "html_parse_H_ALL_1000.txt" , 'r' )

#input_doc_label = open( "html_parse_E_ALL_LABELS.txt" , 'r' )
#input_doc_label = open( "html_parse_F_ALL_LABELS.txt" , 'r' )
if i_1000_flag == 0:
    input_doc_label = open( "html_parse_H_ALL_LABELS.txt" , 'r' )
else:
    input_doc_label = open( "html_parse_H_ALL_LABELS_1000.txt" , 'r' )

test_input_doc_text = input_doc_text.readline()
test_input_doc_label = input_doc_label.readline()

corpus = []
corpus_dict = defaultdict()
corpus_A = []

doc_title_list = []
entire_vocab_set = set()
doc_list_vocab_set = set()
not_in_vocab_set = set()
split_word_set = set()

doc_complete_dict = defaultdict()

i_accum = 0
i_accum_vocab = 0
i_num_tokens_max = -999999
i_num_tokens_min =  999999
while test_input_doc_text:
    i_accum += 1
    
    #print("label = ",test_input_doc_label.strip('\n'))
    #print("doc = ",test_input_doc_text.strip('\n'))
    
    #print("type(label) = ", type(test_input_doc_label.strip('\n')))
    #print("type(doc) = ", type(test_input_doc_text.strip('\n')))
    
    #corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)} for num, text in enumerate( str(test_input_doc_text.strip('\n'))) ]
    #print("corpus = ",corpus)
    #print(utils.simple_preprocess(test_input_doc_text.strip('\n')))
    
    doc_title_list.append( test_input_doc_label.strip('\n') )
    output_tmp.write( str( i_accum ) + ' :    ' + test_input_doc_label )
    
    document = {'id': test_input_doc_label.strip('\n') , 'tokens': utils.simple_preprocess( test_input_doc_text.strip('\n') )}
    #document = {'id': 'doc_%i' % (i_accum-1) , 'tokens': utils.simple_preprocess( test_input_doc_text.strip('\n') )}
    #print("document = " , document )
    #print("document['tokens'] = " , document['tokens'] )
    #print("len(document['tokens']) = " , len(document['tokens']) )
    #if i_num_tokens_max < len(document['tokens']):
    #    i_num_tokens_max = len(document['tokens'])
    #if i_num_tokens_min > len(document['tokens']):
    #    i_num_tokens_min = len(document['tokens'])
    
    #doc_complete.append( test_input_doc_text.strip('\n') )
        
    #not_in_vocab_set = set()
    doc_list = []
    doc_split_word_list = []
    for s_word in document['tokens']:
        
        split_word_list_tmp = []
        split_word_list_tmp = wordninja.split( s_word )
        #print("len(split_word_list_tmp) = " , len(split_word_list_tmp) )
        if len( split_word_list_tmp ) == 0:
            print("ZERO: ", s_word )
            sys.exit(0)
        for i_word in split_word_list_tmp:
            i_accum_vocab += 1
            split_word_set.add( i_word )
            doc_split_word_list.append( i_word )

        entire_vocab_set.add( s_word )
        
        #print(s_word in english_words)
        if not( s_word in english_words ):
            not_in_vocab_set.add( s_word )
        else:
            doc_list.append( s_word )
            doc_list_vocab_set.add( s_word )
            
    if i_num_tokens_max < len(doc_list):
        i_num_tokens_max = len(doc_list)
    if i_num_tokens_min > len(doc_list):
        i_num_tokens_min = len(doc_list)
        
    #print("len(doc_list) = " , len(doc_list) )
    #sys.exit(0)
    
    #document_A = {'id': 'doc_%i' % (i_accum-1) , 'tokens': doc_list }
    #document_A = {'id': test_input_doc_label.strip('\n') , 'tokens': doc_list }
    document_A = {'id': test_input_doc_label.strip('\n') , 'tokens': doc_split_word_list }

    #corpus.append( document )
    corpus.append( document_A )
    corpus_dict[ test_input_doc_label.strip('\n') ] = doc_split_word_list
    
    doc_complete_dict[ test_input_doc_label.strip('\n') ] = test_input_doc_text.strip('\n')
    
    #if i_accum >= 100:
    #if i_accum >= 10:
    #    break
    
    #sys.exit(0)
    
    test_input_doc_text = input_doc_text.readline()
    test_input_doc_label = input_doc_label.readline()

input_doc_text.close()
input_doc_label.close()

#print("not_in_vocab_set = " , not_in_vocab_set )
print("len(not_in_vocab_set) = " , len(not_in_vocab_set) )

print("len(entire_vocab_set) = " , len(entire_vocab_set) )
print("i_accum_vocab = " , i_accum_vocab )

print("len(doc_list_vocab_set) = " , len(doc_list_vocab_set) )

print("len(split_word_set) = " , len(split_word_set) )
#print("len(split_word_set) = " , len(split_word_set) )

print("i_accum = ", i_accum)
print("len(corpus) = ", len(corpus_A))
print("len(doc_title_list) = ", len(doc_title_list))
print("i_num_tokens_max = ", i_num_tokens_max)
print("i_num_tokens_min = ", i_num_tokens_min)
#sys.exit(0)




utils.upload_chunked(server, corpus, chunksize=1000) # send 1k docs at a time

        

#service = SessionServer('C:/0_afc_working/0_Doc2Vec/gensim-simserver-master/my_server/') # or wherever
service = SessionServer( folder_B ) # or wherever

logger.info("simberver_local_A: service.train(corpus, method='lsi')" )

service.train(corpus, method='lsi')

service.index(corpus) # index the same documents that we trained on...
#sys.exit(0)

#service.delete(['doc_5', 'doc_8']) # supply a list of document ids to be removed from the index

#service.index(corpus[:3]) # overall index size unchanged (just 3 docs overwritten)

##print(service.find_similar('doc_0'))
##print(service.find_similar('02456-deep-learning'))
#print(service.find_similar('02456-deep-learning', min_score=0.5, max_results=11))
##[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294259130954742, None), ('doc_1', 0.09881371259689331, None), ('doc_3', 0.08786647021770477, None)]
'''[('02456-deep-learning', 1.0, None), ('deep-docker', 0.8198882937431335, None), 
 ('nvidia-docker-compose', 0.8188392519950867, None), ('introtodeeplearning_labs', 0.8047046661376953, None), 
 ('dl-docker', 0.8002966642379761, None), ('pydocker-template', 0.7893627285957336, None), 
 ('nvidia-docker', 0.7853963375091553, None), ('-deep-deep', 0.7793657779693604, None), 
 ('DockerFiles-tdeboissiere', 0.7759870290756226, None), ('dockerfiles--Kaixhin', 0.7693668007850647, None), 
 ('play-with-docker', 0.7634270191192627, None)]'''


print("Similar: ", service.find_similar('02456-deep-learning', min_score=0.5, max_results=11))
#Similar:  [('02456-deep-learning', 1.0, None), ('awesome-docker', 0.7814108729362488, None), ('alpine-minikube', 0.7373288869857788, None), ('baseimage-docker', 0.7281696796417236, None), ('attalos', 0.69722580909729, None), ('bazel-docker', 0.6071430444717407, None), ('basic-docker-agent-build', 0.5810653567314148, None), ('async-deep-rl', 0.5226494073867798, None), ('altair-Lab41', 0.5212352275848389, None)]

print("DisSimilar: ", service.find_dissimilar('02456-deep-learning', max_score=0.5, max_results=10))
#DisSimilar:  [('attention-is-all-you-need-divyanshj16', 4.366040229797363e-05, None), ('allen', 0.00011094659566879272, None), ('bemkl', 0.00014548376202583313, None), ('backo', 0.00017013587057590485, None), ('aeropy-AeroPython', 0.000325517263263464, None), ('arduino-projects', 0.00038177333772182465, None), ('Asymmetric-Hashing-ANN', 0.000621844083070755, None), ('active-testing', 0.0006259661167860031, None), ('adaptive-neural-compilation', 0.0008356906473636627, None), ('amen', 0.0008382126688957214, None)]
#sys.exit(0)


#print(service.find_similar('doc_5')) # we deleted doc_5 and doc_8, remember?
#ValueError: document 'doc_5' not in index

doc = {'tokens': gensim.utils.simple_preprocess('Graph and minors and humans and trees.')}


#print(service.find_similar(doc, min_score=0.4, max_results=50))
print(service.find_similar(doc, min_score=0.5, max_results=11))
#[('ASTRAL', 0.5314284563064575, None), ('annoy', 0.5216116905212402, None)]
#sys.exit(0)


'''02456-deep-learning :    [('02456-deep-learning', 1.0, None), 
                          ('nvidia-docker-compose', 0.8273645043373108, None), 
                          ('deep-docker', 0.8203121423721313, None), 
                          ('dl-docker', 0.8129054307937622, None), 
                          ('pydocker-template', 0.7977149486541748, None), 
                          ('introtodeeplearning_labs', 0.7885313630104065, None), 
                          ('dockerfiles--Kaixhin', 0.7850551009178162, None), 
                          ('nvidia-docker', 0.7811123728752136, None), 
                          ('DockerFiles-tdeboissiere', 0.7808524370193481, None), 
                          ('chaste-docker', 0.7791703939437866, None), 
                          ('hh-deep-deep', 0.7777622938156128, None)]'''








#==========================================================================================
# START: Similar & TAGS
#==========================================================================================


doc_title_Similar_dict = defaultdict()

doc_title_Similar_TAGS_dict = defaultdict(list)
doc_title_Similar_TAGS_dict_all = defaultdict(list)

topic_Similar_set = set()
topic_Similar_set_all = set()

i_title_accum = 0
for s_title in doc_title_list:
    i_title_accum += 1
    list_tmp = []
    list_tmp = service.find_similar( s_title , min_score=0.5, max_results=11)
    #list_tmp = service.find_similar( s_title , min_score=0.4, max_results=11)
    doc_title_Similar_dict[ s_title ] = list_tmp
    output_tmp.write( s_title + ' :    ' + str( list_tmp ) + '\n'  )
    
    # Doc #:  1  :     02456-deep-learning
    #print( "Doc #: ", str( i_title_accum ) , ' :    ' , s_title )
          
    # list_tmp =  [('02456-deep-learning', 0.9999998807907104, None), ('nvidia-docker-compose', 0.8192633390426636, None), ('deep-docker', 0.8178911209106445, None), ('dl-docker', 0.8177721500396729, None), ('introtodeeplearning_labs', 0.8132678270339966, None), ('pydocker-template', 0.7918097376823425, None), ('DockerFiles-tdeboissiere', 0.7780857682228088, None), ('nvidia-docker', 0.7771468162536621, None), ('dockerfiles--Kaixhin', 0.7759393453598022, None), ('hh-deep-deep', 0.7746105790138245, None), ('chaste-docker', 0.7719804644584656, None)]
    #print("list_tmp = ", list_tmp)
    
    # list_tmp[0] =  ('02456-deep-learning', 0.9999998807907104, None)
    #print("list_tmp[0] = ", list_tmp[0])

    corpus_tmp = []
    doc_complete = []
    doc_complete_all = []
    i_doc_complete_accum = 0
    #for i_tup in list_tmp:
    #for i_tup in list( list_tmp[0] ):
    for i_tup in list_tmp:
        i_doc_complete_accum += 1

        #document_tmp = defaultdict()
        #document_tmp = {'id': i_tup[0] , 'tokens': corpus_dict[ i_tup[0] ] }
        
        # i_tup[0] =  0
        #print("i_tup[0] = ", i_tup[0] )
        
        # i_tup =  02456-deep-learning
        #print("i_tup = ", i_tup )
        
        #print("doc_complete_dict[ i_tup[0] = ", doc_complete_dict[ i_tup[0] ] )

        ##corpus_tmp.append( document_tmp )
        #doc_complete.append( doc_complete_dict[ i_tup[0] ] )
        #
        ## inserted to force exit after loading only the 1st tupl from list_tmp
        #break
        if i_doc_complete_accum == 1:
            doc_complete.append( doc_complete_dict[ i_tup[0] ] )
        doc_complete_all.append( doc_complete_dict[ i_tup[0] ] )

    # len(doc_complete) =  11
    #print("len(doc_complete) = ", len(doc_complete) )
    
    #print("len(corpus_tmp) = ", len(corpus_tmp) )
    #print("corpus_tmp = ", corpus_tmp )
    #sys.exit(0)
    
    #==========================================================================
    # START: TAGS for only the 1st repo
    #==========================================================================
    doc_clean = [clean(doc).split() for doc in doc_complete]  
    dictionary = corpora.Dictionary(doc_clean)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]


    #print("doc_term_matrix = ", doc_term_matrix)
    #doc_term_matrix =  [[(0, 1), (1, 9), (2, 3), (3, 2), (4, 3), (5, 1), (6, 3), (7, 5), (8, 1), (9, 1), (10, 5), ...
    # ...  , (1190, 2), (1191, 3), (1192, 1), (1193, 4), (1194, 1)]]
    
    #print("doc_term_matrix.sort(key=lambda tup: tup[1] , reverse=True ) = ", doc_term_matrix.sort(key=lambda tup: tup[1] , reverse=True ))
    #sys.exit(0)

    corpa_word_freq_dict = defaultdict()
    corpa_word_freq_list = []
    for i_doc in doc_term_matrix:
        for i_tup in i_doc:
            #print(i_tup)
            #if i_tup[0] in corpa_word_freq_dict:
            if dictionary[ i_tup[0] ] in corpa_word_freq_dict:
                #corpa_word_freq_dict[ i_tup[0] ] = corpa_word_freq_dict[ i_tup[0] ] + i_tup[1]
                corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] = corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] + i_tup[1]
            else:
                #corpa_word_freq_dict[ i_tup[0] ] = i_tup[1]
                corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] = i_tup[1]

    for i_word in corpa_word_freq_dict:
        #print("i_word = ",i_word," corpa_word_freq_dict[i_word]: ", corpa_word_freq_dict[i_word] )
        corpa_word_freq_list.append( ( corpa_word_freq_dict[i_word] , i_word ) )

    corpa_word_freq_list.sort( key=lambda tup: tup[0] , reverse=True )
    
    i_num_loops = 0
    i_term_num = 0
    i_term_sum = 0
    while i_term_sum < 5:
        i_num_loops += 1
        if corpa_word_freq_list[ i_term_num ][ 1 ] in bad_terms_list:
            i_term_num += 1
        else:
            #topic_Similar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
            #doc_title_Similar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
            #print("i_term_num = ", i_term_num, corpa_word_freq_list[ i_term_num ][ 1 ] )
            if ( corpa_word_freq_list[ i_term_num ][ 0 ] > i_tag_num_threshold ):
                topic_Similar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
                doc_title_Similar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
                i_term_num += 1
                i_term_sum += 1
                
        if i_num_loops >= len( corpa_word_freq_list ):
            break

    #==========================================================================
    # END: TAGS for only the 1st repo
    #==========================================================================

    
    #==========================================================================
    # START: TAGS for only the 1st group repos
    #==========================================================================
    doc_clean_all = [clean(doc).split() for doc in doc_complete_all]  
    dictionary_all = corpora.Dictionary(doc_clean_all)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix_all = [dictionary_all.doc2bow(doc) for doc in doc_clean_all]

    corpa_word_freq_dict_all = defaultdict()
    corpa_word_freq_list_all = []
    for i_doc in doc_term_matrix_all:
        for i_tup in i_doc:
            #print(i_tup)
            #if i_tup[0] in corpa_word_freq_dict:
            if dictionary_all[ i_tup[0] ] in corpa_word_freq_dict_all:
                #corpa_word_freq_dict[ i_tup[0] ] = corpa_word_freq_dict[ i_tup[0] ] + i_tup[1]
                corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] = corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] + i_tup[1]
            else:
                #corpa_word_freq_dict[ i_tup[0] ] = i_tup[1]
                corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] = i_tup[1]

    for i_word in corpa_word_freq_dict_all:
        #print("i_word = ",i_word," corpa_word_freq_dict[i_word]: ", corpa_word_freq_dict[i_word] )
        corpa_word_freq_list_all.append( ( corpa_word_freq_dict_all[i_word] , i_word ) )

    corpa_word_freq_list_all.sort( key=lambda tup: tup[0] , reverse=True )
    
    i_num_loops = 0
    i_term_num = 0
    i_term_sum = 0
    while i_term_sum < 5:
        i_num_loops += 1
        if corpa_word_freq_list_all[ i_term_num ][ 1 ] in bad_terms_list:
            i_term_num += 1
        else:
            #topic_Similar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
            #doc_title_Similar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
            #print("i_term_num = ", i_term_num, corpa_word_freq_list[ i_term_num ][ 1 ] )
            if ( corpa_word_freq_list_all[ i_term_num ][ 0 ] > i_tag_num_threshold ):
                topic_Similar_set_all.add( corpa_word_freq_list_all[ i_term_num ][ 1 ] )
                doc_title_Similar_TAGS_dict_all[ s_title ].append(  corpa_word_freq_list_all[ i_term_num ][ 1 ] )
                i_term_num += 1
                i_term_sum += 1
                
        if i_num_loops >= len( corpa_word_freq_list_all ):
            break

    #==========================================================================
    # END: TAGS for only the 1st group repos
    #==========================================================================







    
print( "len(topic_Similar_set) = " , len(topic_Similar_set) )
#sys.exit(0)
topic_Similar_list = []
topic_Similar_list = list( topic_Similar_set )
topic_Similar_list.sort()
output_tmp.write( str(topic_Similar_list) + '\n' )
print( "len(doc_title_Similar_dict) = " , len(doc_title_Similar_dict) )
output_tmp.write( str(doc_title_Similar_TAGS_dict) + '\n' )
output_tmp.write( "++++++" + '\n' )
output_tmp.write( str(doc_title_Similar_TAGS_dict_all) + '\n' )
#sys.exit(0)

#output_tmp.close()
output_tmp.write('\n')
output_tmp.write( '******' + '\n')
output_tmp.write('\n')

# Gen zpkl dist files
if i_1000_flag == 0:
    zpickle( doc_title_Similar_dict , 'doc_title_Similar_dict.zpkl' )
    zpickle( doc_title_Similar_TAGS_dict , 'doc_title_Similar_TAGS_dict.zpkl' )
    zpickle( doc_title_Similar_TAGS_dict_all , 'doc_title_Similar_TAGS_dict_all.zpkl' )
else:
    zpickle( doc_title_Similar_dict , 'doc_title_Similar_dict_1000.zpkl' )
    zpickle( doc_title_Similar_TAGS_dict , 'doc_title_Similar_TAGS_dict_1000.zpkl' )
    zpickle( doc_title_Similar_TAGS_dict_all , 'doc_title_Similar_TAGS_dict_all_1000.zpkl' )

#==========================================================================================
# END: Similar & TAGS
#==========================================================================================






#==========================================================================================
# START: DisSimilar & TAGS
#==========================================================================================

doc_title_DisSimilar_dict = defaultdict()

doc_title_DisSimilar_TAGS_dict = defaultdict(list)
doc_title_DisSimilar_TAGS_dict_all = defaultdict(list)

topic_DisSimilar_set = set()
topic_DisSimilar_set_all = set()

i_title_accum = 0
for s_title in doc_title_list:
    i_title_accum += 1
    list_tmp = []
    list_tmp = service.find_dissimilar( s_title , max_score=0.05, max_results=10)
    #list_tmp = service.find_dissimilar( s_title , min_score=0.4, max_results=11)
    doc_title_DisSimilar_dict[ s_title ] = list_tmp
    output_tmp.write( s_title + ' :    ' + str( list_tmp ) + '\n'  )
    
    # Doc #:  1  :     02456-deep-learning
    #print( "Doc #: ", str( i_title_accum ) , ' :    ' , s_title )
          
    # list_tmp =  [('02456-deep-learning', 0.9999998807907104, None), ('nvidia-docker-compose', 0.8192633390426636, None), ('deep-docker', 0.8178911209106445, None), ('dl-docker', 0.8177721500396729, None), ('introtodeeplearning_labs', 0.8132678270339966, None), ('pydocker-template', 0.7918097376823425, None), ('DockerFiles-tdeboissiere', 0.7780857682228088, None), ('nvidia-docker', 0.7771468162536621, None), ('dockerfiles--Kaixhin', 0.7759393453598022, None), ('hh-deep-deep', 0.7746105790138245, None), ('chaste-docker', 0.7719804644584656, None)]
    #print("list_tmp = ", list_tmp)
    
    # list_tmp[0] =  ('02456-deep-learning', 0.9999998807907104, None)
    #print("list_tmp[0] = ", list_tmp[0])

    corpus_tmp = []
    doc_complete = []
    doc_complete_all = []
    i_doc_complete_accum = 0
    #for i_tup in list_tmp:
    #for i_tup in list( list_tmp[0] ):
    for i_tup in list_tmp:
        i_doc_complete_accum += 1

        #document_tmp = defaultdict()
        #document_tmp = {'id': i_tup[0] , 'tokens': corpus_dict[ i_tup[0] ] }
        
        # i_tup[0] =  0
        #print("i_tup[0] = ", i_tup[0] )
        
        # i_tup =  02456-deep-learning
        #print("i_tup = ", i_tup )
        
        #print("doc_complete_dict[ i_tup[0] = ", doc_complete_dict[ i_tup[0] ] )

        ##corpus_tmp.append( document_tmp )
        #doc_complete.append( doc_complete_dict[ i_tup[0] ] )
        #
        ## inserted to force exit after loading only the 1st tupl from list_tmp
        #break
        if i_doc_complete_accum == 1:
            doc_complete.append( doc_complete_dict[ i_tup[0] ] )
        doc_complete_all.append( doc_complete_dict[ i_tup[0] ] )

    # len(doc_complete) =  11
    #print("len(doc_complete) = ", len(doc_complete) )
    
    #print("len(corpus_tmp) = ", len(corpus_tmp) )
    #print("corpus_tmp = ", corpus_tmp )
    #sys.exit(0)
    
    #==========================================================================
    # START: TAGS for only the 1st repo
    #==========================================================================
    doc_clean = [clean(doc).split() for doc in doc_complete]  
    dictionary = corpora.Dictionary(doc_clean)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]


    #print("doc_term_matrix = ", doc_term_matrix)
    #doc_term_matrix =  [[(0, 1), (1, 9), (2, 3), (3, 2), (4, 3), (5, 1), (6, 3), (7, 5), (8, 1), (9, 1), (10, 5), ...
    # ...  , (1190, 2), (1191, 3), (1192, 1), (1193, 4), (1194, 1)]]
    
    #print("doc_term_matrix.sort(key=lambda tup: tup[1] , reverse=True ) = ", doc_term_matrix.sort(key=lambda tup: tup[1] , reverse=True ))
    #sys.exit(0)

    corpa_word_freq_dict = defaultdict()
    corpa_word_freq_list = []
    for i_doc in doc_term_matrix:
        for i_tup in i_doc:
            #print(i_tup)
            #if i_tup[0] in corpa_word_freq_dict:
            if dictionary[ i_tup[0] ] in corpa_word_freq_dict:
                #corpa_word_freq_dict[ i_tup[0] ] = corpa_word_freq_dict[ i_tup[0] ] + i_tup[1]
                corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] = corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] + i_tup[1]
            else:
                #corpa_word_freq_dict[ i_tup[0] ] = i_tup[1]
                corpa_word_freq_dict[ dictionary[ i_tup[0] ] ] = i_tup[1]

    for i_word in corpa_word_freq_dict:
        #print("i_word = ",i_word," corpa_word_freq_dict[i_word]: ", corpa_word_freq_dict[i_word] )
        corpa_word_freq_list.append( ( corpa_word_freq_dict[i_word] , i_word ) )

    corpa_word_freq_list.sort( key=lambda tup: tup[0] , reverse=True )
    
    i_num_loops = 0
    i_term_num = 0
    i_term_sum = 0
    while i_term_sum < 5:
        i_num_loops += 1
        if corpa_word_freq_list[ i_term_num ][ 1 ] in bad_terms_list:
            i_term_num += 1
        else:
            #topic_DisSimilar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
            #doc_title_DisSimilar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
            #print("i_term_num = ", i_term_num, corpa_word_freq_list[ i_term_num ][ 1 ] )
            if ( corpa_word_freq_list[ i_term_num ][ 0 ] > i_tag_num_threshold ):
                topic_DisSimilar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
                doc_title_DisSimilar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
                i_term_num += 1
                i_term_sum += 1
                
        if i_num_loops >= len( corpa_word_freq_list ):
            break

    #==========================================================================
    # END: TAGS for only the 1st repo
    #==========================================================================

    
    #==========================================================================
    # START: TAGS for only the 1st group repos
    #==========================================================================
    doc_clean_all = [clean(doc).split() for doc in doc_complete_all]  
    dictionary_all = corpora.Dictionary(doc_clean_all)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix_all = [dictionary_all.doc2bow(doc) for doc in doc_clean_all]

    corpa_word_freq_dict_all = defaultdict()
    corpa_word_freq_list_all = []
    for i_doc in doc_term_matrix_all:
        for i_tup in i_doc:
            #print(i_tup)
            #if i_tup[0] in corpa_word_freq_dict:
            if dictionary_all[ i_tup[0] ] in corpa_word_freq_dict_all:
                #corpa_word_freq_dict[ i_tup[0] ] = corpa_word_freq_dict[ i_tup[0] ] + i_tup[1]
                corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] = corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] + i_tup[1]
            else:
                #corpa_word_freq_dict[ i_tup[0] ] = i_tup[1]
                corpa_word_freq_dict_all[ dictionary_all[ i_tup[0] ] ] = i_tup[1]

    for i_word in corpa_word_freq_dict_all:
        #print("i_word = ",i_word," corpa_word_freq_dict[i_word]: ", corpa_word_freq_dict[i_word] )
        corpa_word_freq_list_all.append( ( corpa_word_freq_dict_all[i_word] , i_word ) )

    corpa_word_freq_list_all.sort( key=lambda tup: tup[0] , reverse=True )
    
    i_num_loops = 0
    i_term_num = 0
    i_term_sum = 0
    while i_term_sum < 5:
        i_num_loops += 1
        if corpa_word_freq_list_all[ i_term_num ][ 1 ] in bad_terms_list:
            i_term_num += 1
        else:
            #topic_DisSimilar_set.add( corpa_word_freq_list[ i_term_num ][ 1 ] )
            #doc_title_DisSimilar_TAGS_dict[ s_title ].append(  corpa_word_freq_list[ i_term_num ][ 1 ] )
            #print("i_term_num = ", i_term_num, corpa_word_freq_list[ i_term_num ][ 1 ] )
            if ( corpa_word_freq_list_all[ i_term_num ][ 0 ] > i_tag_num_threshold ):
                topic_DisSimilar_set_all.add( corpa_word_freq_list_all[ i_term_num ][ 1 ] )
                doc_title_DisSimilar_TAGS_dict_all[ s_title ].append(  corpa_word_freq_list_all[ i_term_num ][ 1 ] )
                i_term_num += 1
                i_term_sum += 1
                
        if i_num_loops >= len( corpa_word_freq_list_all ):
            break

    #==========================================================================
    # END: TAGS for only the 1st group repos
    #==========================================================================



    
print( "len(topic_DisSimilar_set) = " , len(topic_DisSimilar_set) )
#sys.exit(0)
topic_DisSimilar_list = []
topic_DisSimilar_list = list( topic_DisSimilar_set )
topic_DisSimilar_list.sort()
output_tmp.write( str(topic_DisSimilar_list) + '\n' )
print( "len(doc_title_DisSimilar_dict) = " , len(doc_title_DisSimilar_dict) )
output_tmp.write( str(doc_title_DisSimilar_TAGS_dict) + '\n' )
output_tmp.write( "++++++" + '\n' )
output_tmp.write( str(doc_title_DisSimilar_TAGS_dict_all) + '\n' )
#sys.exit(0)

#output_tmp.close()
output_tmp.write('\n')
output_tmp.write( '******' + '\n')
output_tmp.write('\n')

# Gen zpkl dist files
if i_1000_flag == 0:
    zpickle( doc_title_DisSimilar_dict , 'doc_title_DisSimilar_dict.zpkl' )
    zpickle( doc_title_DisSimilar_TAGS_dict , 'doc_title_DisSimilar_TAGS_dict.zpkl' )
    zpickle( doc_title_DisSimilar_TAGS_dict_all , 'doc_title_DisSimilar_TAGS_dict_all.zpkl' )
else:
    zpickle( doc_title_DisSimilar_dict , 'doc_title_DisSimilar_dict_1000.zpkl' )
    zpickle( doc_title_DisSimilar_TAGS_dict , 'doc_title_DisSimilar_TAGS_dict_1000.zpkl' )
    zpickle( doc_title_DisSimilar_TAGS_dict_all , 'doc_title_DisSimilar_TAGS_dict_all_1000.zpkl' )

#==========================================================================================
# END: DisSimilar & TAGS
#==========================================================================================


















print("Done:")

