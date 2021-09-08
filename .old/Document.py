import DataManager

def read_help_file():
    import codecs
    with codecs.open(DataManager.getPath('data/Document.txt'), encoding='utf-8') as help_file:
       print(help_file.read())
