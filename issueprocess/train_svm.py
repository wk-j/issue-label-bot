def acuracy(listbug):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    import dill as pickle
    from pythainlp.tokenize import word_tokenize
    import codecs
    with open('Documents/vocabulary.data', 'rb') as file:
        vocabulary = pickle.load(file)
    with open('Documents/model.data', 'rb') as file:
        classifier = pickle.load(file)
    count = 0
    for test_sentence in listbug:
        featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}
        result = classifier.classify(featurized_test_sentence)
        if result=='bug':count+=1
    acc = count*100/len(listbug)
    logging.info("accuracy : ")
    logging.info(acc)
    logging.info('=============================================')

def saveModel(vocabulary,classifier):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    import dill
    with open('Documents/vocabulary.data', 'wb') as out_strm: 
        dill.dump(vocabulary,out_strm)
    out_strm.close()
    with open('Documents/model.data', 'wb') as out_strm: 
        dill.dump(classifier,out_strm)
    out_strm.close()
    logging.info('============ SAVE MODEL SUCCESS ============')

def trainModel(training_data):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    import nltk.classify
    from sklearn.svm import LinearSVC
    from pythainlp.tokenize import word_tokenize
    from pythainlp.corpus import thai_stopwords
    from itertools import chain
    logging.warning(' ============ TRAINNING MODEL ============')
    logging.info('split word ...')
    vocabulary = set(chain(*[(set(word_tokenize(i[0]))-set(thai_stopwords())) for i in training_data]))
    #vocabulary = set(chain(*[x for x in a if x not in [list(set(word_tokenize(i[0]))) for i in training_data]]))
    logging.info('exact feature ...')
    feature_set = [({i:(i in word_tokenize(sentence)) for i in vocabulary},tag) for sentence, tag in training_data]
    classifier = nltk.classify.SklearnClassifier(LinearSVC())
    classifier.train(feature_set)
    saveModel(vocabulary,classifier)
    
def accepdata(listbug,listdoc,listdup,listenh,listgood,listhelp,listinv):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info('accepdata ..')
    bug1=['bug']*len(listbug)
    doc1=['documentation']*len(listdoc)
    dup1 = ['duplicate']*len(listdup)
    enh1 = ['enhancement']*len(listenh)
    good1 = ['good first issue']*len(listgood)
    help1 = ['help wanted']*len(listhelp)
    inv1 = ['invalid']*len(listinv)
    training_data = list(zip(listbug,bug1)) + list(zip(listdoc,doc1))+ list(zip(listdup,dup1))+ list(zip(listenh,enh1))+ list(zip(listgood,good1))+ list(zip(listhelp,help1))+ list(zip(listinv,inv1))
    trainModel(training_data)
    logging.info('Check ACCURACY ...(Can close program if you not want check)')
    acuracy(listbug)
