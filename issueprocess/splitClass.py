
def splitclass(preTitle,preDescription,preLabel):
    import logging
    logging.getLogger().setLevel(logging.INFO)
    listbug = []
    listdoc = []
    listdup = []
    listenh = []
    listgood = []
    listhelp = []
    listinv = []
    i = 0
    for data in preLabel:
        if data == 'bug': listbug.append(preTitle[i]+preDescription[i])
        elif data == 'documentation': listdoc.append(preTitle[i]+preDescription[i])
        elif data == 'duplicate': listdup.append(preTitle[i]+preDescription[i])
        elif data == 'enhancement': listenh.append(preTitle[i]+preDescription[i])
        elif data == 'good first issue': listgood.append(preTitle[i]+preDescription[i])
        elif data == 'help wanted': listhelp.append(preTitle[i]+preDescription[i])
        elif data == 'invalid': listinv.append(preTitle[i]+preDescription[i])
        i = i +1
    logging.info('bug : '+str(len(listbug)))
    logging.info('documentation : '+str(len(listdoc)))
    logging.info('duplicate : '+str(len(listdup)))
    logging.info('enhancement : '+str(len(listenh)))
    logging.info('good first issue : '+str(len(listgood)))
    logging.info('help wanted : '+str(len(listhelp)))
    logging.info('invalid : '+str(len(listinv)))
    return listbug,listdoc,listdup,listenh,listgood,listhelp,listinv