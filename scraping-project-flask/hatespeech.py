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


DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    if request.method == 'GET':
        check_hate()
#define important variables


def check_hate():
    print("here")
    board_name = 'pol'
    filename = 'crawled_data.csv'
    chinese_hate_speech_filename = "hatebase_vocab_chinese.csv"
    asian_hate_speech_filename = "hatebase_vocab_asian.csv"

    ##########DONOT EDIT BELOW##################################################################

    while True:
        try:
            print("here2")
            df_chinese = pd.read_csv(chinese_hate_speech_filename)
            print("here4")
            df_asian = pd.read_csv(asian_hate_speech_filename)
            list_id = []
            if os.path.isfile(filename):
                list_id = pd.read_csv(filename)["post_id"].to_list()
            
            df_total = pd.concat([df_chinese, df_asian])
            list_hate = df_total["term"]

            col_names = ["text_comment", "datetime", "post_id"]
            df_asian_hate = pd.DataFrame(columns = col_names)
            print("here3")
            # get the board we want
            board = basc_py4chan.Board(board_name)
            print("this is board", board)
            # select the first thread on the board
            all_thread_ids = board.get_all_thread_ids()
            thread_list = []

            for id in all_thread_ids:

                first_thread_id = id
                thread = board.get_thread(first_thread_id)
                print("this is thread: ", thread)
                if thread == None:
                    continue
                topic = thread.topic
                for thread in thread.all_posts:
                    if any(s.lower() in thread.comment.lower() for s in list_hate) and thread.post_id not in list_id:
                        temp_dict = {}
                        temp_dict["text_comment"] = thread.text_comment
                        temp_dict["datetime"] = thread.datetime
                        temp_dict["post_id"] = thread.post_id
                        df_asian_hate = df_asian_hate.append(temp_dict, ignore_index = True)

            if not os.path.isfile(filename):
                df_asian_hate.to_csv(filename, header='column_names')

            else: # else it exists so append without writing the header
                df_asian_hate.to_csv(filename, mode='a', header=False)
        except:
            time.sleep(2)
            continue


if __name__ == '__main__':
    app.run()