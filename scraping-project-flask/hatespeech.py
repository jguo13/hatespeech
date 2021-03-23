from __future__ import print_function
import basc_py4chan
import pandas as pd
import os
import time
import sys
import copy
import csv 

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
hate_percentage = [
    {
        'percentage': 0
    }
]

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/get_hate', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        len_hate = check_hate()
        response_object["percentage"] = len_hate
        return jsonify(response_object)
#define important variables


def check_hate():
    print("here")
    board_name = 'pol'
    # filename = 'crawled_data.csv'
    # chinese_hate_speech_filename = "hatebase_vocab_chinese.csv"
    # asian_hate_speech_filename = "hatebase_vocab_asian.csv"

    ##########DONOT EDIT BELOW##################################################################

    # while True:
    try:
        # df_chinese = pd.read_csv(chinese_hate_speech_filename)
        # df_asian = pd.read_csv(asian_hate_speech_filename)
        # list_id = []
        # if os.path.isfile(filename):
        #     list_id = pd.read_csv(filename)["post_id"].to_list()
        
        # df_total = pd.concat([df_chinese, df_asian])
        # list_hate = df_total["term"]
        list_hate = ['ABCs', 'ABC', 'spinks', 'spink', 'slopey', 'winks', 'slopes', 'slopies', 'slants', 'slopeheads', 'slant eyes', 'sideways vaginas', 'sideways cooters', 'sideways pussies', 'coolies', 'chonkies', 'chunkies', 'Chinese wetbacks', 'ching chongs', 'chinigs', 'chink a billies', 'chiggers', 'celestials', 'bamboo coons', 'chinig', 'sideways cooter', 'slopehead', 'chink a billy', 'Chinese wetback', 'bamboo coon', 'ching chong', 'coolie', 'slopy', 'chonky', 'chunky', 'sideways pussy', 'sideways vagina', 'chigger', 'slope', 'slant', 'slant eye', 'wink', 'celestial', 'whoriental', 'whorientals', 'gooky eyes', 'gooklets', 'gooklet', 'gookettes', 'gookette', 'gook eyed', 'gookies', 'gookie', 'goloids', 'goloid', 'ginks', 'gink', 'dog eaters', 'dog eater', 'yellow invaders', 'rice niggers', 'yellow invader', 'rice nigger']
        # col_names = ["text_comment", "datetime", "post_id"]
        # df_asian_hate = pd.DataFrame(columns = col_names)
        # get the board we want
        board = basc_py4chan.Board(board_name)
        # select the first thread on the board
        all_thread_ids = board.get_all_thread_ids()
        # thread_list = []
        thread_count = 0
        hate_count = 0
        for id in all_thread_ids:

            first_thread_id = id
            thread = board.get_thread(first_thread_id)
            if thread == None:
                continue
            topic = thread.topic
            for thread in thread.all_posts:
                thread_count += 1
                if any(s.lower() in thread.comment.lower() for s in list_hate):
                    hate_count += 1
                    # temp_dict = {}
                    # temp_dict["text_comment"] = thread.text_comment
                    # temp_dict["datetime"] = thread.datetime
                    # temp_dict["post_id"] = thread.post_id
                    # df_asian_hate = df_asian_hate.append(temp_dict, ignore_index = True)

        percentage = "{:.2%}".format(hate_count / thread_count)
        return percentage
        # if not os.path.isfile(filename):
        #     df_asian_hate.to_csv(filename, header='column_names')

        # else: # else it exists so append without writing the header
        #     df_asian_hate.to_csv(filename, mode='a', header=False)
    except :
        return "error with the server, please refresh"
            # continue


if __name__ == '__main__':
    app.run()