# -*- coding: utf-8 -*-

#
# Author: Alex
# Created Time: 2017年01月17日 星期二 18时02分28秒

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print(u"参数个数不对")
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        text = [text_i.decode("utf8") for text_i in text]
        output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 1000 == 0):
            logger.info("Saved %d articles" % i)

    output.close()
    logger.info("Finished Saved %d articles" % i)
