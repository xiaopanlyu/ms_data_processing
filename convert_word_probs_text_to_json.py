import json
import sys
import getopt
import time


def convert_txt_to_json(text_file, out_file):
    fp = open(text_file)
    word_probs = []
    i=10000
    for word_prob_data in fp:
        word_prob_dict = {}
        t = time.time()
        timestamp = int(round(t * 1000))
        word_prob_dict.setdefault('id', t)
        word_prob_dict.setdefault('index', i)
        word_prob_dict.setdefault('question', word_prob_data.replace('\n',''))
        word_prob_dict.setdefault('ans', "")
        word_prob_dict.setdefault('template', "")
        word_prob_dict.setdefault('type', "")
        word_prob_dict.setdefault('flag',1)
        i += 1
        word_probs.append(word_prob_dict)
    fp.close()
    fp = open(out_file, 'w')
    json.dump(word_probs, fp, indent = 2, ensure_ascii=False)
    fp.close()
    
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:o:')
    except getopt.GetoptError:
        print ('invalid input format')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            text_file = arg
        elif opt == "-o":
            out_file = arg
    convert_txt_to_json(text_file, out_file)