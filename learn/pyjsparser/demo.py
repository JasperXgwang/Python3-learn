#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging

from pyjsparser import PyJsParser

text = '''
      $.ajax({
                type: "POST",
                url: "https://msec.flyme.cn/captcha/server/check", //访问的链接
                data: param,
                success: function (data) {  //成功的回调函数
                    console.info(data);
                },
                error: function (e) {
                    console.info(e);
                }
            });
'''

p = PyJsParser()
try:
    result = p.parse(text)
except Exception as e:
    logging.error(e)

result_json = json.dumps(result)

print(result_json)
