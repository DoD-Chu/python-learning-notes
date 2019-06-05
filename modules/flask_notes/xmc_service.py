# -*-coding: utf-8 -*-
"""
    @Project: python-learning-notes
    @File   : xmc_service.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-06-05 16:41:03
"""
from flask import Flask, request, redirect, url_for, render_template, jsonify
import err_msg
app = Flask(__name__)

imageprocesscb_api='/v1/engine/pipelinemanager/imageprocesscb'
@app.route(imageprocesscb_api, methods=['POST'])
def handle_async_cv_imageprocesscb():
    return http_api_async_imageprocesscb(request)

def http_api_async_imageprocesscb(request):
    if request.method == 'POST':
        # TODO
        params = request.json
        print("imageprocesscb:{}".format(params))
        return err_msg.util_make_response(err_msg.get_err_msg_dict(0))


def start_flask_server(host='127.0.0.1', port=8888, debug=True):
    app.run(host,port=port)

if __name__ == '__main__':
    start_flask_server()
