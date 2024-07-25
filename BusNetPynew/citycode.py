import json
import pandas as pd
def codes_pip():
    citycode_json = '''[
        {
            "\u4e2d\u6587\u540d": "\u5317\u4eac\u5e02",
            "adcode": 110000,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u4eac\u5e02\u5e02\u8f96\u533a",
            "adcode": 110100,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u57ce\u533a",
            "adcode": 110101,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u57ce\u533a",
            "adcode": 110102,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u9633\u533a",
            "adcode": 110105,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u53f0\u533a",
            "adcode": 110106,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u666f\u5c71\u533a",
            "adcode": 110107,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u6dc0\u533a",
            "adcode": 110108,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u95e8\u5934\u6c9f\u533a",
            "adcode": 110109,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u623f\u5c71\u533a",
            "adcode": 110111,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5dde\u533a",
            "adcode": 110112,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u4e49\u533a",
            "adcode": 110113,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u5e73\u533a",
            "adcode": 110114,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5174\u533a",
            "adcode": 110115,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u67d4\u533a",
            "adcode": 110116,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u8c37\u533a",
            "adcode": 110117,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5bc6\u4e91\u533a",
            "adcode": 110118,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5e86\u533a",
            "adcode": 110119,
            "citycode": 10
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6d25\u5e02",
            "adcode": 120000,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6d25\u5e02\u5e02\u8f96\u533a",
            "adcode": 120100,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u5e73\u533a",
            "adcode": 120101,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u4e1c\u533a",
            "adcode": 120102,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u897f\u533a",
            "adcode": 120103,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5f00\u533a",
            "adcode": 120104,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u5317\u533a",
            "adcode": 120105,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u6865\u533a",
            "adcode": 120106,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u4e3d\u533a",
            "adcode": 120110,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u9752\u533a",
            "adcode": 120111,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6d25\u5357\u533a",
            "adcode": 120112,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u8fb0\u533a",
            "adcode": 120113,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u6e05\u533a",
            "adcode": 120114,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u577b\u533a",
            "adcode": 120115,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u6d77\u65b0\u533a",
            "adcode": 120116,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6cb3\u533a",
            "adcode": 120117,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u9759\u6d77\u533a",
            "adcode": 120118,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u84df\u5dde\u533a",
            "adcode": 120119,
            "citycode": 22
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5bb6\u5e84\u5e02",
            "adcode": 130100,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5bb6\u5e84\u5e02\u5e02\u8f96\u533a",
            "adcode": 130101,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5b89\u533a",
            "adcode": 130102,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u6865\u897f\u533a",
            "adcode": 130104,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u534e\u533a",
            "adcode": 130105,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u4e95\u9649\u77ff\u533a",
            "adcode": 130107,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u88d5\u534e\u533a",
            "adcode": 130108,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u85c1\u57ce\u533a",
            "adcode": 130109,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u9e7f\u6cc9\u533a",
            "adcode": 130110,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u683e\u57ce\u533a",
            "adcode": 130111,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u4e95\u9649\u53bf",
            "adcode": 130121,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u5b9a\u53bf",
            "adcode": 130123,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u884c\u5510\u53bf",
            "adcode": 130125,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u5bff\u53bf",
            "adcode": 130126,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u9091\u53bf",
            "adcode": 130127,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u6df1\u6cfd\u53bf",
            "adcode": 130128,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u8d5e\u7687\u53bf",
            "adcode": 130129,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u65e0\u6781\u53bf",
            "adcode": 130130,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5c71\u53bf",
            "adcode": 130131,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u6c0f\u53bf",
            "adcode": 130132,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u8d75\u53bf",
            "adcode": 130133,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u8f9b\u96c6\u5e02",
            "adcode": 130181,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u5dde\u5e02",
            "adcode": 130183,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4e50\u5e02",
            "adcode": 130184,
            "citycode": 311
        },
        {
            "\u4e2d\u6587\u540d": "\u5510\u5c71\u5e02",
            "adcode": 130200,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u5510\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 130201,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u8def\u5357\u533a",
            "adcode": 130202,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u8def\u5317\u533a",
            "adcode": 130203,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u51b6\u533a",
            "adcode": 130204,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5e73\u533a",
            "adcode": 130205,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u5357\u533a",
            "adcode": 130207,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u6da6\u533a",
            "adcode": 130208,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u66f9\u5983\u7538\u533a",
            "adcode": 130209,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee6\u5dde\u5e02",
            "adcode": 130284,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee6\u5357\u53bf",
            "adcode": 130224,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u4ead\u53bf",
            "adcode": 130225,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u8fc1\u897f\u53bf",
            "adcode": 130227,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u7530\u53bf",
            "adcode": 130229,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u9075\u5316\u5e02",
            "adcode": 130281,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u8fc1\u5b89\u5e02",
            "adcode": 130283,
            "citycode": 315
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u7687\u5c9b\u5e02",
            "adcode": 130300,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u7687\u5c9b\u5e02\u5e02\u8f96\u533a",
            "adcode": 130301,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u6e2f\u533a",
            "adcode": 130302,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u6d77\u5173\u533a",
            "adcode": 130303,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6234\u6cb3\u533a",
            "adcode": 130304,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u5b81\u533a",
            "adcode": 130306,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u9f99\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 130321,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u9ece\u53bf",
            "adcode": 130322,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u5362\u9f99\u53bf",
            "adcode": 130324,
            "citycode": 335
        },
        {
            "\u4e2d\u6587\u540d": "\u90af\u90f8\u5e02",
            "adcode": 130400,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u90af\u90f8\u5e02\u5e02\u8f96\u533a",
            "adcode": 130401,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u90af\u5c71\u533a",
            "adcode": 130402,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1b\u53f0\u533a",
            "adcode": 130403,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u590d\u5174\u533a",
            "adcode": 130404,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u5cf0\u5cf0\u77ff\u533a",
            "adcode": 130406,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u80a5\u4e61\u533a",
            "adcode": 130407,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5e74\u533a",
            "adcode": 130408,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6f33\u53bf",
            "adcode": 130423,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u5b89\u53bf",
            "adcode": 130424,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u540d\u53bf",
            "adcode": 130425,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u6d89\u53bf",
            "adcode": 130426,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u78c1\u53bf",
            "adcode": 130427,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u90b1\u53bf",
            "adcode": 130430,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u9e21\u6cfd\u53bf",
            "adcode": 130431,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5e73\u53bf",
            "adcode": 130432,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u9986\u9676\u53bf",
            "adcode": 130433,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u9b4f\u53bf",
            "adcode": 130434,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u5468\u53bf",
            "adcode": 130435,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5b89\u5e02",
            "adcode": 130481,
            "citycode": 310
        },
        {
            "\u4e2d\u6587\u540d": "\u90a2\u53f0\u5e02",
            "adcode": 130500,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u90a2\u53f0\u5e02\u5e02\u8f96\u533a",
            "adcode": 130501,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u6865\u4e1c\u533a",
            "adcode": 130502,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u6865\u897f\u533a",
            "adcode": 130503,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u90a2\u53f0\u53bf",
            "adcode": 130521,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u57ce\u53bf",
            "adcode": 130522,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5185\u4e18\u53bf",
            "adcode": 130523,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u67cf\u4e61\u53bf",
            "adcode": 130524,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u5c27\u53bf",
            "adcode": 130525,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u4efb\u53bf",
            "adcode": 130526,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u548c\u53bf",
            "adcode": 130527,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u664b\u53bf",
            "adcode": 130528,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5de8\u9e7f\u53bf",
            "adcode": 130529,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6cb3\u53bf",
            "adcode": 130530,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5b97\u53bf",
            "adcode": 130531,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u4e61\u53bf",
            "adcode": 130532,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u53bf",
            "adcode": 130533,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6cb3\u53bf",
            "adcode": 130534,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u897f\u53bf",
            "adcode": 130535,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5bab\u5e02",
            "adcode": 130581,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u6cb3\u5e02",
            "adcode": 130582,
            "citycode": 319
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5b9a\u5e02",
            "adcode": 130600,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5b9a\u5e02\u5e02\u8f96\u533a",
            "adcode": 130601,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u7ade\u79c0\u533a",
            "adcode": 130602,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u83b2\u6c60\u533a",
            "adcode": 130606,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee1\u57ce\u533a",
            "adcode": 130607,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u82d1\u533a",
            "adcode": 130608,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5f90\u6c34\u533a",
            "adcode": 130609,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6d9e\u6c34\u53bf",
            "adcode": 130623,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u5e73\u53bf",
            "adcode": 130624,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u5174\u53bf",
            "adcode": 130626,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5510\u53bf",
            "adcode": 130627,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u9633\u53bf",
            "adcode": 130628,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5bb9\u57ce\u53bf",
            "adcode": 130629,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6d9e\u6e90\u53bf",
            "adcode": 130630,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u90fd\u53bf",
            "adcode": 130631,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u65b0\u53bf",
            "adcode": 130632,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6613\u53bf",
            "adcode": 130633,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u9633\u53bf",
            "adcode": 130634,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u8821\u53bf",
            "adcode": 130635,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u5e73\u53bf",
            "adcode": 130636,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u91ce\u53bf",
            "adcode": 130637,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u96c4\u53bf",
            "adcode": 130638,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u6dbf\u5dde\u5e02",
            "adcode": 130681,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u5dde\u5e02",
            "adcode": 130682,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u56fd\u5e02",
            "adcode": 130683,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u7891\u5e97\u5e02",
            "adcode": 130684,
            "citycode": 312
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u53e3\u5e02",
            "adcode": 130700,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u53e3\u5e02\u5e02\u8f96\u533a",
            "adcode": 130701,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6865\u4e1c\u533a",
            "adcode": 130702,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6865\u897f\u533a",
            "adcode": 130703,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u5316\u533a",
            "adcode": 130705,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0b\u82b1\u56ed\u533a",
            "adcode": 130706,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5168\u533a",
            "adcode": 130708,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u793c\u533a",
            "adcode": 130709,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5317\u53bf",
            "adcode": 130722,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u4fdd\u53bf",
            "adcode": 130723,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbd\u6e90\u53bf",
            "adcode": 130724,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u5c1a\u4e49\u53bf",
            "adcode": 130725,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u851a\u53bf",
            "adcode": 130726,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u539f\u53bf",
            "adcode": 130727,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u5b89\u53bf",
            "adcode": 130728,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u6765\u53bf",
            "adcode": 130730,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u6dbf\u9e7f\u53bf",
            "adcode": 130731,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u57ce\u53bf",
            "adcode": 130732,
            "citycode": 313
        },
        {
            "\u4e2d\u6587\u540d": "\u627f\u5fb7\u5e02",
            "adcode": 130800,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u627f\u5fb7\u5e02\u5e02\u8f96\u533a",
            "adcode": 130801,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6865\u533a",
            "adcode": 130802,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6ee6\u533a",
            "adcode": 130803,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u9e70\u624b\u8425\u5b50\u77ff\u533a",
            "adcode": 130804,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u627f\u5fb7\u53bf",
            "adcode": 130821,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u9686\u53bf",
            "adcode": 130822,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee6\u5e73\u53bf",
            "adcode": 130824,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u5316\u53bf",
            "adcode": 130825,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u5b81\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 130826,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbd\u57ce\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 130827,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u56f4\u573a\u6ee1\u65cf\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 130828,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6cc9\u5e02",
            "adcode": 130881,
            "citycode": 314
        },
        {
            "\u4e2d\u6587\u540d": "\u6ca7\u5dde\u5e02",
            "adcode": 130900,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u6ca7\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 130901,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u534e\u533a",
            "adcode": 130902,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u8fd0\u6cb3\u533a",
            "adcode": 130903,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u6ca7\u53bf",
            "adcode": 130921,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u53bf",
            "adcode": 130922,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5149\u53bf",
            "adcode": 130923,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5174\u53bf",
            "adcode": 130924,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u5c71\u53bf",
            "adcode": 130925,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u8083\u5b81\u53bf",
            "adcode": 130926,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u76ae\u53bf",
            "adcode": 130927,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u6865\u53bf",
            "adcode": 130928,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u732e\u53bf",
            "adcode": 130929,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5f\u6751\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 130930,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u6cca\u5934\u5e02",
            "adcode": 130981,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u4efb\u4e18\u5e02",
            "adcode": 130982,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u9a85\u5e02",
            "adcode": 130983,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u95f4\u5e02",
            "adcode": 130984,
            "citycode": 317
        },
        {
            "\u4e2d\u6587\u540d": "\u5eca\u574a\u5e02",
            "adcode": 131000,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u5eca\u574a\u5e02\u5e02\u8f96\u533a",
            "adcode": 131001,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u6b21\u533a",
            "adcode": 131002,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u9633\u533a",
            "adcode": 131003,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u5b89\u53bf",
            "adcode": 131022,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u6e05\u53bf",
            "adcode": 131023,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u9999\u6cb3\u53bf",
            "adcode": 131024,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u57ce\u53bf",
            "adcode": 131025,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u5b89\u53bf",
            "adcode": 131026,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5382\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 131028,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u9738\u5dde\u5e02",
            "adcode": 131081,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u6cb3\u5e02",
            "adcode": 131082,
            "citycode": 316
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u6c34\u5e02",
            "adcode": 131100,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u6c34\u5e02\u5e02\u8f96\u533a",
            "adcode": 131101,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u6843\u57ce\u533a",
            "adcode": 131102,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u5180\u5dde\u533a",
            "adcode": 131103,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u67a3\u5f3a\u53bf",
            "adcode": 131121,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u9091\u53bf",
            "adcode": 131122,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5f3a\u53bf",
            "adcode": 131123,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u9976\u9633\u53bf",
            "adcode": 131124,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5e73\u53bf",
            "adcode": 131125,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u6545\u57ce\u53bf",
            "adcode": 131126,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u53bf",
            "adcode": 131127,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u57ce\u53bf",
            "adcode": 131128,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u6df1\u5dde\u5e02",
            "adcode": 131182,
            "citycode": 318
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u539f\u5e02",
            "adcode": 140100,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u539f\u5e02\u5e02\u8f96\u533a",
            "adcode": 140101,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u5c0f\u5e97\u533a",
            "adcode": 140105,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u8fce\u6cfd\u533a",
            "adcode": 140106,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u674f\u82b1\u5cad\u533a",
            "adcode": 140107,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u5c16\u8349\u576a\u533a",
            "adcode": 140108,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u67cf\u6797\u533a",
            "adcode": 140109,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u6e90\u533a",
            "adcode": 140110,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u5f90\u53bf",
            "adcode": 140121,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u66f2\u53bf",
            "adcode": 140122,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u5a04\u70e6\u53bf",
            "adcode": 140123,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u4ea4\u5e02",
            "adcode": 140181,
            "citycode": 351
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u540c\u5e02",
            "adcode": 140200,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u540c\u5e02\u5e02\u8f96\u533a",
            "adcode": 140201,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u57ce\u533a",
            "adcode": 140213,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u5188\u533a",
            "adcode": 140214,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u8363\u533a",
            "adcode": 140212,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u9ad8\u53bf",
            "adcode": 140221,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u9547\u53bf",
            "adcode": 140222,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u7075\u53bf",
            "adcode": 140223,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u4e18\u53bf",
            "adcode": 140224,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u6d51\u6e90\u53bf",
            "adcode": 140225,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u5de6\u4e91\u53bf",
            "adcode": 140226,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u5dde\u533a",
            "adcode": 140215,
            "citycode": 352
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6cc9\u5e02",
            "adcode": 140300,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6cc9\u5e02\u5e02\u8f96\u533a",
            "adcode": 140301,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u533a",
            "adcode": 140302,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u77ff\u533a",
            "adcode": 140303,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u90ca\u533a",
            "adcode": 140311,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5b9a\u53bf",
            "adcode": 140321,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u76c2\u53bf",
            "adcode": 140322,
            "citycode": 353
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6cbb\u5e02",
            "adcode": 140400,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6cbb\u5e02\u5e02\u8f96\u533a",
            "adcode": 140401,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u6f5e\u5dde\u533a",
            "adcode": 140403,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u515a\u533a",
            "adcode": 140404,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u57a3\u53bf",
            "adcode": 140423,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u5c6f\u7559\u533a",
            "adcode": 140405,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u987a\u53bf",
            "adcode": 140425,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u9ece\u57ce\u53bf",
            "adcode": 140426,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u58f6\u5173\u53bf",
            "adcode": 140427,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5b50\u53bf",
            "adcode": 140428,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u4e61\u53bf",
            "adcode": 140429,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u6c81\u53bf",
            "adcode": 140430,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u6c81\u6e90\u53bf",
            "adcode": 140431,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u6f5e\u57ce\u533a",
            "adcode": 140406,
            "citycode": 355
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u57ce\u5e02",
            "adcode": 140500,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 140501,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u533a",
            "adcode": 140502,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u6c81\u6c34\u53bf",
            "adcode": 140521,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u57ce\u53bf",
            "adcode": 140522,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u9675\u5ddd\u53bf",
            "adcode": 140524,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfd\u5dde\u53bf",
            "adcode": 140525,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u5e73\u5e02",
            "adcode": 140581,
            "citycode": 356
        },
        {
            "\u4e2d\u6587\u540d": "\u6714\u5dde\u5e02",
            "adcode": 140600,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u6714\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 140601,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u6714\u57ce\u533a",
            "adcode": 140602,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9c81\u533a",
            "adcode": 140603,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u9634\u53bf",
            "adcode": 140621,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u5e94\u53bf",
            "adcode": 140622,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u53f3\u7389\u53bf",
            "adcode": 140623,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u4ec1\u5e02",
            "adcode": 140681,
            "citycode": 349
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u4e2d\u5e02",
            "adcode": 140700,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u4e2d\u5e02\u5e02\u8f96\u533a",
            "adcode": 140701,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u6b21\u533a",
            "adcode": 140702,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u793e\u53bf",
            "adcode": 140721,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u5de6\u6743\u53bf",
            "adcode": 140722,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u987a\u53bf",
            "adcode": 140723,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u6614\u9633\u53bf",
            "adcode": 140724,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u5bff\u9633\u53bf",
            "adcode": 140725,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u8c37\u533a",
            "adcode": 140703,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u7941\u53bf",
            "adcode": 140727,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9065\u53bf",
            "adcode": 140728,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u77f3\u53bf",
            "adcode": 140729,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u4ecb\u4f11\u5e02",
            "adcode": 140781,
            "citycode": 354
        },
        {
            "\u4e2d\u6587\u540d": "\u8fd0\u57ce\u5e02",
            "adcode": 140800,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u8fd0\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 140801,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u6e56\u533a",
            "adcode": 140802,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u7317\u53bf",
            "adcode": 140821,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u8363\u53bf",
            "adcode": 140822,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u95fb\u559c\u53bf",
            "adcode": 140823,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u7a37\u5c71\u53bf",
            "adcode": 140824,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u7edb\u53bf",
            "adcode": 140825,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u7edb\u53bf",
            "adcode": 140826,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u57a3\u66f2\u53bf",
            "adcode": 140827,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u590f\u53bf",
            "adcode": 140828,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9646\u53bf",
            "adcode": 140829,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u82ae\u57ce\u53bf",
            "adcode": 140830,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u6d4e\u5e02",
            "adcode": 140881,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u6d25\u5e02",
            "adcode": 140882,
            "citycode": 359
        },
        {
            "\u4e2d\u6587\u540d": "\u5ffb\u5dde\u5e02",
            "adcode": 140900,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u5ffb\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 140901,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u5ffb\u5e9c\u533a",
            "adcode": 140902,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u8944\u53bf",
            "adcode": 140921,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u53f0\u53bf",
            "adcode": 140922,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u4ee3\u53bf",
            "adcode": 140923,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u7e41\u5cd9\u53bf",
            "adcode": 140924,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6b66\u53bf",
            "adcode": 140925,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u9759\u4e50\u53bf",
            "adcode": 140926,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u795e\u6c60\u53bf",
            "adcode": 140927,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u5be8\u53bf",
            "adcode": 140928,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u5ca2\u5c9a\u53bf",
            "adcode": 140929,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u66f2\u53bf",
            "adcode": 140930,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5fb7\u53bf",
            "adcode": 140931,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u504f\u5173\u53bf",
            "adcode": 140932,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u539f\u5e73\u5e02",
            "adcode": 140981,
            "citycode": 350
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6c7e\u5e02",
            "adcode": 141000,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6c7e\u5e02\u5e02\u8f96\u533a",
            "adcode": 141001,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u5c27\u90fd\u533a",
            "adcode": 141002,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u6c83\u53bf",
            "adcode": 141021,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u7ffc\u57ce\u53bf",
            "adcode": 141022,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u6c7e\u53bf",
            "adcode": 141023,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u6d1e\u53bf",
            "adcode": 141024,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u53bf",
            "adcode": 141025,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u6cfd\u53bf",
            "adcode": 141026,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u6d6e\u5c71\u53bf",
            "adcode": 141027,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u53bf",
            "adcode": 141028,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u4e61\u5b81\u53bf",
            "adcode": 141029,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5b81\u53bf",
            "adcode": 141030,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u96b0\u53bf",
            "adcode": 141031,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u548c\u53bf",
            "adcode": 141032,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u84b2\u53bf",
            "adcode": 141033,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u6c7e\u897f\u53bf",
            "adcode": 141034,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u4faf\u9a6c\u5e02",
            "adcode": 141081,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u5dde\u5e02",
            "adcode": 141082,
            "citycode": 357
        },
        {
            "\u4e2d\u6587\u540d": "\u5415\u6881\u5e02",
            "adcode": 141100,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u5415\u6881\u5e02\u5e02\u8f96\u533a",
            "adcode": 141101,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u79bb\u77f3\u533a",
            "adcode": 141102,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u6c34\u53bf",
            "adcode": 141121,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u4ea4\u57ce\u53bf",
            "adcode": 141122,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u53bf",
            "adcode": 141123,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u53bf",
            "adcode": 141124,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u6797\u53bf",
            "adcode": 141125,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u697c\u53bf",
            "adcode": 141126,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u5c9a\u53bf",
            "adcode": 141127,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u65b9\u5c71\u53bf",
            "adcode": 141128,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u9633\u53bf",
            "adcode": 141129,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u4ea4\u53e3\u53bf",
            "adcode": 141130,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5d\u4e49\u5e02",
            "adcode": 141181,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u6c7e\u9633\u5e02",
            "adcode": 141182,
            "citycode": 358
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u548c\u6d69\u7279\u5e02",
            "adcode": 150100,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u548c\u6d69\u7279\u5e02\u5e02\u8f96\u533a",
            "adcode": 150101,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u57ce\u533a",
            "adcode": 150102,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u56de\u6c11\u533a",
            "adcode": 150103,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6cc9\u533a",
            "adcode": 150104,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u8d5b\u7f55\u533a",
            "adcode": 150105,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u571f\u9ed8\u7279\u5de6\u65d7",
            "adcode": 150121,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u6258\u514b\u6258\u53bf",
            "adcode": 150122,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u6797\u683c\u5c14\u53bf",
            "adcode": 150123,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6c34\u6cb3\u53bf",
            "adcode": 150124,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5ddd\u53bf",
            "adcode": 150125,
            "citycode": 471
        },
        {
            "\u4e2d\u6587\u540d": "\u5305\u5934\u5e02",
            "adcode": 150200,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u5305\u5934\u5e02\u5e02\u8f96\u533a",
            "adcode": 150201,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6cb3\u533a",
            "adcode": 150202,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u6606\u90fd\u4ed1\u533a",
            "adcode": 150203,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5c71\u533a",
            "adcode": 150204,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u62d0\u533a",
            "adcode": 150205,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u4e91\u9102\u535a\u77ff\u533a",
            "adcode": 150206,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u539f\u533a",
            "adcode": 150207,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u571f\u9ed8\u7279\u53f3\u65d7",
            "adcode": 150221,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u9633\u53bf",
            "adcode": 150222,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5c14\u7f55\u8302\u660e\u5b89\u8054\u5408\u65d7",
            "adcode": 150223,
            "citycode": 472
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u6d77\u5e02",
            "adcode": 150300,
            "citycode": 473
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u6d77\u5e02\u5e02\u8f96\u533a",
            "adcode": 150301,
            "citycode": 473
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u52c3\u6e7e\u533a",
            "adcode": 150302,
            "citycode": 473
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5357\u533a",
            "adcode": 150303,
            "citycode": 473
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u8fbe\u533a",
            "adcode": 150304,
            "citycode": 473
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u5cf0\u5e02",
            "adcode": 150400,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u5cf0\u5e02\u5e02\u8f96\u533a",
            "adcode": 150401,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u5c71\u533a",
            "adcode": 150402,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u5b9d\u5c71\u533a",
            "adcode": 150403,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u5c71\u533a",
            "adcode": 150404,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u9c81\u79d1\u5c14\u6c81\u65d7",
            "adcode": 150421,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u6797\u5de6\u65d7",
            "adcode": 150422,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u6797\u53f3\u65d7",
            "adcode": 150423,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u897f\u53bf",
            "adcode": 150424,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u4ec0\u514b\u817e\u65d7",
            "adcode": 150425,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u7fc1\u725b\u7279\u65d7",
            "adcode": 150426,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u5580\u5587\u6c81\u65d7",
            "adcode": 150428,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u57ce\u53bf",
            "adcode": 150429,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u6556\u6c49\u65d7",
            "adcode": 150430,
            "citycode": 476
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u8fbd\u5e02",
            "adcode": 150500,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u8fbd\u5e02\u5e02\u8f96\u533a",
            "adcode": 150501,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u79d1\u5c14\u6c81\u533a",
            "adcode": 150502,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u79d1\u5c14\u6c81\u5de6\u7ffc\u4e2d\u65d7",
            "adcode": 150521,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u79d1\u5c14\u6c81\u5de6\u7ffc\u540e\u65d7",
            "adcode": 150522,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u9c81\u53bf",
            "adcode": 150523,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u5e93\u4f26\u65d7",
            "adcode": 150524,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u5948\u66fc\u65d7",
            "adcode": 150525,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u624e\u9c81\u7279\u65d7",
            "adcode": 150526,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u6797\u90ed\u52d2\u5e02",
            "adcode": 150581,
            "citycode": 475
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u5c14\u591a\u65af\u5e02",
            "adcode": 150600,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u5c14\u591a\u65af\u5e02\u5e02\u8f96\u533a",
            "adcode": 150601,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u80dc\u533a",
            "adcode": 150602,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u5df4\u4ec0\u533a",
            "adcode": 150603,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u62c9\u7279\u65d7",
            "adcode": 150621,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u51c6\u683c\u5c14\u65d7",
            "adcode": 150622,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u6258\u514b\u524d\u65d7",
            "adcode": 150623,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u6258\u514b\u65d7",
            "adcode": 150624,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u676d\u9526\u65d7",
            "adcode": 150625,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5ba1\u65d7",
            "adcode": 150626,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u91d1\u970d\u6d1b\u65d7",
            "adcode": 150627,
            "citycode": 477
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u4f26\u8d1d\u5c14\u5e02",
            "adcode": 150700,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u4f26\u8d1d\u5c14\u5e02\u5e02\u8f96\u533a",
            "adcode": 150701,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u62c9\u5c14\u533a",
            "adcode": 150702,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u624e\u8d49\u8bfa\u5c14\u533a",
            "adcode": 150703,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u8363\u65d7",
            "adcode": 150721,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u83ab\u529b\u8fbe\u74e6\u8fbe\u65a1\u5c14\u65cf\u81ea\u6cbb\u65d7",
            "adcode": 150722,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u4f26\u6625\u81ea\u6cbb\u65d7",
            "adcode": 150723,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u6e29\u514b\u65cf\u81ea\u6cbb\u65d7",
            "adcode": 150724,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u9648\u5df4\u5c14\u864e\u65d7",
            "adcode": 150725,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5df4\u5c14\u864e\u5de6\u65d7",
            "adcode": 150726,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5df4\u5c14\u864e\u53f3\u65d7",
            "adcode": 150727,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee1\u6d32\u91cc\u5e02",
            "adcode": 150781,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u7259\u514b\u77f3\u5e02",
            "adcode": 150782,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u624e\u5170\u5c6f\u5e02",
            "adcode": 150783,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u989d\u5c14\u53e4\u7eb3\u5e02",
            "adcode": 150784,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u6839\u6cb3\u5e02",
            "adcode": 150785,
            "citycode": 470
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5f66\u6dd6\u5c14\u5e02",
            "adcode": 150800,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5f66\u6dd6\u5c14\u5e02\u5e02\u8f96\u533a",
            "adcode": 150801,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6cb3\u533a",
            "adcode": 150802,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u539f\u53bf",
            "adcode": 150821,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u78f4\u53e3\u53bf",
            "adcode": 150822,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u62c9\u7279\u524d\u65d7",
            "adcode": 150823,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u62c9\u7279\u4e2d\u65d7",
            "adcode": 150824,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u62c9\u7279\u540e\u65d7",
            "adcode": 150825,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u676d\u9526\u540e\u65d7",
            "adcode": 150826,
            "citycode": 478
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5170\u5bdf\u5e03\u5e02",
            "adcode": 150900,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5170\u5bdf\u5e03\u5e02\u5e02\u8f96\u533a",
            "adcode": 150901,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u96c6\u5b81\u533a",
            "adcode": 150902,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5353\u8d44\u53bf",
            "adcode": 150921,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5316\u5fb7\u53bf",
            "adcode": 150922,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u90fd\u53bf",
            "adcode": 150923,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u548c\u53bf",
            "adcode": 150924,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u51c9\u57ce\u53bf",
            "adcode": 150925,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u54c8\u5c14\u53f3\u7ffc\u524d\u65d7",
            "adcode": 150926,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u54c8\u5c14\u53f3\u7ffc\u4e2d\u65d7",
            "adcode": 150927,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u54c8\u5c14\u53f3\u7ffc\u540e\u65d7",
            "adcode": 150928,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u56db\u5b50\u738b\u65d7",
            "adcode": 150929,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u9547\u5e02",
            "adcode": 150981,
            "citycode": 474
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5b89\u76df",
            "adcode": 152200,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5170\u6d69\u7279\u5e02",
            "adcode": 152201,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u5c14\u5c71\u5e02",
            "adcode": 152202,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u79d1\u5c14\u6c81\u53f3\u7ffc\u524d\u65d7",
            "adcode": 152221,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u79d1\u5c14\u6c81\u53f3\u7ffc\u4e2d\u65d7",
            "adcode": 152222,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u624e\u8d49\u7279\u65d7",
            "adcode": 152223,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u7a81\u6cc9\u53bf",
            "adcode": 152224,
            "citycode": 482
        },
        {
            "\u4e2d\u6587\u540d": "\u9521\u6797\u90ed\u52d2\u76df",
            "adcode": 152500,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8c\u8fde\u6d69\u7279\u5e02",
            "adcode": 152501,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u9521\u6797\u6d69\u7279\u5e02",
            "adcode": 152502,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u5df4\u560e\u65d7",
            "adcode": 152522,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5c3c\u7279\u5de6\u65d7",
            "adcode": 152523,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5c3c\u7279\u53f3\u65d7",
            "adcode": 152524,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u4e4c\u73e0\u7a46\u6c81\u65d7",
            "adcode": 152525,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u4e4c\u73e0\u7a46\u6c81\u65d7",
            "adcode": 152526,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u4ec6\u5bfa\u65d7",
            "adcode": 152527,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u9576\u9ec4\u65d7",
            "adcode": 152528,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u9576\u767d\u65d7",
            "adcode": 152529,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u84dd\u65d7",
            "adcode": 152530,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u591a\u4f26\u53bf",
            "adcode": 152531,
            "citycode": 479
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u62c9\u5584\u76df",
            "adcode": 152900,
            "citycode": 483
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u62c9\u5584\u5de6\u65d7",
            "adcode": 152921,
            "citycode": 483
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u62c9\u5584\u53f3\u65d7",
            "adcode": 152922,
            "citycode": 483
        },
        {
            "\u4e2d\u6587\u540d": "\u989d\u6d4e\u7eb3\u65d7",
            "adcode": 152923,
            "citycode": 483
        },
        {
            "\u4e2d\u6587\u540d": "\u6c88\u9633\u5e02",
            "adcode": 210100,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u6c88\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 210101,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u5e73\u533a",
            "adcode": 210102,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u6c88\u6cb3\u533a",
            "adcode": 210103,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u4e1c\u533a",
            "adcode": 210104,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u7687\u59d1\u533a",
            "adcode": 210105,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u897f\u533a",
            "adcode": 210106,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5bb6\u5c6f\u533a",
            "adcode": 210111,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u6d51\u5357\u533a",
            "adcode": 210112,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u6c88\u5317\u65b0\u533a",
            "adcode": 210113,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8e\u6d2a\u533a",
            "adcode": 210114,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u4e2d\u533a",
            "adcode": 210115,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u5e73\u53bf",
            "adcode": 210123,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u6cd5\u5e93\u53bf",
            "adcode": 210124,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6c11\u5e02",
            "adcode": 210181,
            "citycode": 24
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u8fde\u5e02",
            "adcode": 210200,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u8fde\u5e02\u5e02\u8f96\u533a",
            "adcode": 210201,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u5c71\u533a",
            "adcode": 210202,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5c97\u533a",
            "adcode": 210203,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u6cb3\u53e3\u533a",
            "adcode": 210204,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u4e95\u5b50\u533a",
            "adcode": 210211,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u65c5\u987a\u53e3\u533a",
            "adcode": 210212,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5dde\u533a",
            "adcode": 210213,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u5170\u5e97\u533a",
            "adcode": 210214,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6d77\u53bf",
            "adcode": 210224,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u74e6\u623f\u5e97\u5e02",
            "adcode": 210281,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u5e84\u6cb3\u5e02",
            "adcode": 210283,
            "citycode": 411
        },
        {
            "\u4e2d\u6587\u540d": "\u978d\u5c71\u5e02",
            "adcode": 210300,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u978d\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 210301,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u4e1c\u533a",
            "adcode": 210302,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u897f\u533a",
            "adcode": 210303,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u7acb\u5c71\u533a",
            "adcode": 210304,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u5343\u5c71\u533a",
            "adcode": 210311,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u5b89\u53bf",
            "adcode": 210321,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u5cab\u5ca9\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210323,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u57ce\u5e02",
            "adcode": 210381,
            "citycode": 412
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u987a\u5e02",
            "adcode": 210400,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u987a\u5e02\u5e02\u8f96\u533a",
            "adcode": 210401,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u629a\u533a",
            "adcode": 210402,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6d32\u533a",
            "adcode": 210403,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u82b1\u533a",
            "adcode": 210404,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u57ce\u533a",
            "adcode": 210411,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u987a\u53bf",
            "adcode": 210421,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5bbe\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210422,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u539f\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210423,
            "citycode": 413
        },
        {
            "\u4e2d\u6587\u540d": "\u672c\u6eaa\u5e02",
            "adcode": 210500,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u672c\u6eaa\u5e02\u5e02\u8f96\u533a",
            "adcode": 210501,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5c71\u533a",
            "adcode": 210502,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u6eaa\u6e56\u533a",
            "adcode": 210503,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u660e\u5c71\u533a",
            "adcode": 210504,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u82ac\u533a",
            "adcode": 210505,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u672c\u6eaa\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210521,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u6853\u4ec1\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210522,
            "citycode": 414
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u4e1c\u5e02",
            "adcode": 210600,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u4e1c\u5e02\u5e02\u8f96\u533a",
            "adcode": 210601,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u5b9d\u533a",
            "adcode": 210602,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u632f\u5174\u533a",
            "adcode": 210603,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u632f\u5b89\u533a",
            "adcode": 210604,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbd\u7538\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210624,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6e2f\u5e02",
            "adcode": 210681,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u57ce\u5e02",
            "adcode": 210682,
            "citycode": 415
        },
        {
            "\u4e2d\u6587\u540d": "\u9526\u5dde\u5e02",
            "adcode": 210700,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u9526\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 210701,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u5854\u533a",
            "adcode": 210702,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u51cc\u6cb3\u533a",
            "adcode": 210703,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u548c\u533a",
            "adcode": 210711,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed1\u5c71\u53bf",
            "adcode": 210726,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u4e49\u53bf",
            "adcode": 210727,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u51cc\u6d77\u5e02",
            "adcode": 210781,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u9547\u5e02",
            "adcode": 210782,
            "citycode": 416
        },
        {
            "\u4e2d\u6587\u540d": "\u8425\u53e3\u5e02",
            "adcode": 210800,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u8425\u53e3\u5e02\u5e02\u8f96\u533a",
            "adcode": 210801,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u7ad9\u524d\u533a",
            "adcode": 210802,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5e02\u533a",
            "adcode": 210803,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u9c85\u9c7c\u5708\u533a",
            "adcode": 210804,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u8001\u8fb9\u533a",
            "adcode": 210811,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u76d6\u5dde\u5e02",
            "adcode": 210881,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u77f3\u6865\u5e02",
            "adcode": 210882,
            "citycode": 417
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u65b0\u5e02",
            "adcode": 210900,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u65b0\u5e02\u5e02\u8f96\u533a",
            "adcode": 210901,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5dde\u533a",
            "adcode": 210902,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u90b1\u533a",
            "adcode": 210903,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u5e73\u533a",
            "adcode": 210904,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6cb3\u95e8\u533a",
            "adcode": 210905,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u7ec6\u6cb3\u533a",
            "adcode": 210911,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u65b0\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 210921,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u5f70\u6b66\u53bf",
            "adcode": 210922,
            "citycode": 418
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u9633\u5e02",
            "adcode": 211000,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 211001,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u5854\u533a",
            "adcode": 211002,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u5723\u533a",
            "adcode": 211003,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u5b8f\u4f1f\u533a",
            "adcode": 211004,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u5f13\u957f\u5cad\u533a",
            "adcode": 211005,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u5b50\u6cb3\u533a",
            "adcode": 211011,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u9633\u53bf",
            "adcode": 211021,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u706f\u5854\u5e02",
            "adcode": 211081,
            "citycode": 419
        },
        {
            "\u4e2d\u6587\u540d": "\u76d8\u9526\u5e02",
            "adcode": 211100,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u76d8\u9526\u5e02\u5e02\u8f96\u533a",
            "adcode": 211101,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u53f0\u5b50\u533a",
            "adcode": 211102,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u9686\u53f0\u533a",
            "adcode": 211103,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u6d3c\u533a",
            "adcode": 211104,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u76d8\u5c71\u53bf",
            "adcode": 211122,
            "citycode": 427
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u5cad\u5e02",
            "adcode": 211200,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u5cad\u5e02\u5e02\u8f96\u533a",
            "adcode": 211201,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u94f6\u5dde\u533a",
            "adcode": 211202,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6cb3\u533a",
            "adcode": 211204,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u5cad\u53bf",
            "adcode": 211221,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u4e30\u53bf",
            "adcode": 211223,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u56fe\u53bf",
            "adcode": 211224,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u8c03\u5175\u5c71\u5e02",
            "adcode": 211281,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u539f\u5e02",
            "adcode": 211282,
            "citycode": 410
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u9633\u5e02",
            "adcode": 211300,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 211301,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u5854\u533a",
            "adcode": 211302,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u57ce\u533a",
            "adcode": 211303,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u9633\u53bf",
            "adcode": 211321,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u5e73\u53bf",
            "adcode": 211322,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u5580\u5587\u6c81\u5de6\u7ffc\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 211324,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u7968\u5e02",
            "adcode": 211381,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u51cc\u6e90\u5e02",
            "adcode": 211382,
            "citycode": 421
        },
        {
            "\u4e2d\u6587\u540d": "\u846b\u82a6\u5c9b\u5e02",
            "adcode": 211400,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u846b\u82a6\u5c9b\u5e02\u5e02\u8f96\u533a",
            "adcode": 211401,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u5c71\u533a",
            "adcode": 211402,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6e2f\u533a",
            "adcode": 211403,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u7968\u533a",
            "adcode": 211404,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u4e2d\u53bf",
            "adcode": 211421,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u660c\u53bf",
            "adcode": 211422,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u57ce\u5e02",
            "adcode": 211481,
            "citycode": 429
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6625\u5e02",
            "adcode": 220100,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6625\u5e02\u5e02\u8f96\u533a",
            "adcode": 220101,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5173\u533a",
            "adcode": 220102,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbd\u57ce\u533a",
            "adcode": 220103,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u9633\u533a",
            "adcode": 220104,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8c\u9053\u533a",
            "adcode": 220105,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u7eff\u56ed\u533a",
            "adcode": 220106,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u9633\u533a",
            "adcode": 220112,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u53f0\u533a",
            "adcode": 220113,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u519c\u5b89\u53bf",
            "adcode": 220122,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u6811\u5e02",
            "adcode": 220182,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u60e0\u5e02",
            "adcode": 220183,
            "citycode": 431
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u6797\u5e02",
            "adcode": 220200,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u6797\u5e02\u5e02\u8f96\u533a",
            "adcode": 220201,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u9091\u533a",
            "adcode": 220202,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6f6d\u533a",
            "adcode": 220203,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u8239\u8425\u533a",
            "adcode": 220204,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u6ee1\u533a",
            "adcode": 220211,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5409\u53bf",
            "adcode": 220221,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u86df\u6cb3\u5e02",
            "adcode": 220281,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u6866\u7538\u5e02",
            "adcode": 220282,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u8212\u5170\u5e02",
            "adcode": 220283,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u78d0\u77f3\u5e02",
            "adcode": 220284,
            "citycode": 432
        },
        {
            "\u4e2d\u6587\u540d": "\u56db\u5e73\u5e02",
            "adcode": 220300,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u56db\u5e73\u5e02\u5e02\u8f96\u533a",
            "adcode": 220301,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u897f\u533a",
            "adcode": 220302,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u4e1c\u533a",
            "adcode": 220303,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u68a8\u6811\u53bf",
            "adcode": 220322,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u901a\u6ee1\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 220323,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u516c\u4e3b\u5cad\u5e02",
            "adcode": 220381,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u8fbd\u5e02",
            "adcode": 220382,
            "citycode": 434
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u6e90\u5e02",
            "adcode": 220400,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbd\u6e90\u5e02\u5e02\u8f96\u533a",
            "adcode": 220401,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5c71\u533a",
            "adcode": 220402,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b89\u533a",
            "adcode": 220403,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u4e30\u53bf",
            "adcode": 220421,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u8fbd\u53bf",
            "adcode": 220422,
            "citycode": 437
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5316\u5e02",
            "adcode": 220500,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5316\u5e02\u5e02\u8f96\u533a",
            "adcode": 220501,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u660c\u533a",
            "adcode": 220502,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8c\u9053\u6c5f\u533a",
            "adcode": 220503,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5316\u53bf",
            "adcode": 220521,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u8f89\u5357\u53bf",
            "adcode": 220523,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u6cb3\u53bf",
            "adcode": 220524,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u6cb3\u53e3\u5e02",
            "adcode": 220581,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u96c6\u5b89\u5e02",
            "adcode": 220582,
            "citycode": 435
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u5c71\u5e02",
            "adcode": 220600,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 220601,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u6d51\u6c5f\u533a",
            "adcode": 220602,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6e90\u533a",
            "adcode": 220605,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u677e\u53bf",
            "adcode": 220621,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u5b87\u53bf",
            "adcode": 220622,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u767d\u671d\u9c9c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 220623,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6c5f\u5e02",
            "adcode": 220681,
            "citycode": 439
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u539f\u5e02",
            "adcode": 220700,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u539f\u5e02\u5e02\u8f96\u533a",
            "adcode": 220701,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6c5f\u533a",
            "adcode": 220702,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u524d\u90ed\u5c14\u7f57\u65af\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 220721,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5cad\u53bf",
            "adcode": 220722,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u4e7e\u5b89\u53bf",
            "adcode": 220723,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u6276\u4f59\u5e02",
            "adcode": 220781,
            "citycode": 438
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u57ce\u5e02",
            "adcode": 220800,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 220801,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2e\u5317\u533a",
            "adcode": 220802,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u8d49\u53bf",
            "adcode": 220821,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u6986\u53bf",
            "adcode": 220822,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2e\u5357\u5e02",
            "adcode": 220881,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5b89\u5e02",
            "adcode": 220882,
            "citycode": 436
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u8fb9\u671d\u9c9c\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 222400,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5409\u5e02",
            "adcode": 222401,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u56fe\u4eec\u5e02",
            "adcode": 222402,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u6566\u5316\u5e02",
            "adcode": 222403,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u73f2\u6625\u5e02",
            "adcode": 222404,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u4e95\u5e02",
            "adcode": 222405,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u9f99\u5e02",
            "adcode": 222406,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u6c6a\u6e05\u53bf",
            "adcode": 222424,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u56fe\u53bf",
            "adcode": 222426,
            "citycode": 1433
        },
        {
            "\u4e2d\u6587\u540d": "\u54c8\u5c14\u6ee8\u5e02",
            "adcode": 230100,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u54c8\u5c14\u6ee8\u5e02\u5e02\u8f96\u533a",
            "adcode": 230101,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u9053\u91cc\u533a",
            "adcode": 230102,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5c97\u533a",
            "adcode": 230103,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u9053\u5916\u533a",
            "adcode": 230104,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u623f\u533a",
            "adcode": 230108,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u5317\u533a",
            "adcode": 230109,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u9999\u574a\u533a",
            "adcode": 230110,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u5170\u533a",
            "adcode": 230111,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u57ce\u533a",
            "adcode": 230112,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u57ce\u533a",
            "adcode": 230113,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u4f9d\u5170\u53bf",
            "adcode": 230123,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u65b9\u6b63\u53bf",
            "adcode": 230124,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbe\u53bf",
            "adcode": 230125,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5f66\u53bf",
            "adcode": 230126,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u6728\u5170\u53bf",
            "adcode": 230127,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u6cb3\u53bf",
            "adcode": 230128,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5bff\u53bf",
            "adcode": 230129,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u5c1a\u5fd7\u5e02",
            "adcode": 230183,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u5e38\u5e02",
            "adcode": 230184,
            "citycode": 451
        },
        {
            "\u4e2d\u6587\u540d": "\u9f50\u9f50\u54c8\u5c14\u5e02",
            "adcode": 230200,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u9f50\u9f50\u54c8\u5c14\u5e02\u5e02\u8f96\u533a",
            "adcode": 230201,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6c99\u533a",
            "adcode": 230202,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u534e\u533a",
            "adcode": 230203,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u950b\u533a",
            "adcode": 230204,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u6602\u6602\u6eaa\u533a",
            "adcode": 230205,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u62c9\u5c14\u57fa\u533a",
            "adcode": 230206,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u78be\u5b50\u5c71\u533a",
            "adcode": 230207,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u91cc\u65af\u8fbe\u65a1\u5c14\u65cf\u533a",
            "adcode": 230208,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6c5f\u53bf",
            "adcode": 230221,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u4f9d\u5b89\u53bf",
            "adcode": 230223,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u6765\u53bf",
            "adcode": 230224,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5357\u53bf",
            "adcode": 230225,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u88d5\u53bf",
            "adcode": 230227,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u5c71\u53bf",
            "adcode": 230229,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u4e1c\u53bf",
            "adcode": 230230,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u62dc\u6cc9\u53bf",
            "adcode": 230231,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u8bb7\u6cb3\u5e02",
            "adcode": 230281,
            "citycode": 452
        },
        {
            "\u4e2d\u6587\u540d": "\u9e21\u897f\u5e02",
            "adcode": 230300,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u9e21\u897f\u5e02\u5e02\u8f96\u533a",
            "adcode": 230301,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u9e21\u51a0\u533a",
            "adcode": 230302,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u6052\u5c71\u533a",
            "adcode": 230303,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u6ef4\u9053\u533a",
            "adcode": 230304,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u68a8\u6811\u533a",
            "adcode": 230305,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u5b50\u6cb3\u533a",
            "adcode": 230306,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u5c71\u533a",
            "adcode": 230307,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u9e21\u4e1c\u53bf",
            "adcode": 230321,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u864e\u6797\u5e02",
            "adcode": 230381,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u5bc6\u5c71\u5e02",
            "adcode": 230382,
            "citycode": 467
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5c97\u5e02",
            "adcode": 230400,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5c97\u5e02\u5e02\u8f96\u533a",
            "adcode": 230401,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u5411\u9633\u533a",
            "adcode": 230402,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u5de5\u519c\u533a",
            "adcode": 230403,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5c71\u533a",
            "adcode": 230404,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5b89\u533a",
            "adcode": 230405,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5c71\u533a",
            "adcode": 230406,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5c71\u533a",
            "adcode": 230407,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u841d\u5317\u53bf",
            "adcode": 230421,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u6ee8\u53bf",
            "adcode": 230422,
            "citycode": 468
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u9e2d\u5c71\u5e02",
            "adcode": 230500,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u9e2d\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 230501,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u5c16\u5c71\u533a",
            "adcode": 230502,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u5cad\u4e1c\u533a",
            "adcode": 230503,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u56db\u65b9\u53f0\u533a",
            "adcode": 230505,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5c71\u533a",
            "adcode": 230506,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u96c6\u8d24\u53bf",
            "adcode": 230521,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u53cb\u8c0a\u53bf",
            "adcode": 230522,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u6e05\u53bf",
            "adcode": 230523,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u9976\u6cb3\u53bf",
            "adcode": 230524,
            "citycode": 469
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5e86\u5e02",
            "adcode": 230600,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5e86\u5e02\u5e02\u8f96\u533a",
            "adcode": 230601,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u8428\u5c14\u56fe\u533a",
            "adcode": 230602,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u51e4\u533a",
            "adcode": 230603,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u8ba9\u80e1\u8def\u533a",
            "adcode": 230604,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u5c97\u533a",
            "adcode": 230605,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u540c\u533a",
            "adcode": 230606,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u8087\u5dde\u53bf",
            "adcode": 230621,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u8087\u6e90\u53bf",
            "adcode": 230622,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u7538\u53bf",
            "adcode": 230623,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u675c\u5c14\u4f2f\u7279\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 230624,
            "citycode": 459
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u6625\u5e02",
            "adcode": 230700,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u6625\u5e02\u5e02\u8f96\u533a",
            "adcode": 230701,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u6c64\u65fa\u6cb3\u533a",
            "adcode": 230712,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u7f8e\u533a",
            "adcode": 230717,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u7fe0\u533a",
            "adcode": 230718,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u53cb\u597d\u533a",
            "adcode": 230719,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u836b\u53bf",
            "adcode": 230722,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u6c64\u65fa\u53bf",
            "adcode": 230723,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u6797\u53bf",
            "adcode": 230724,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7b90\u5c71\u53bf",
            "adcode": 230725,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5c94\u53bf",
            "adcode": 230726,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6797\u533a",
            "adcode": 230751,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u529b\u5e02",
            "adcode": 230781,
            "citycode": 458
        },
        {
            "\u4e2d\u6587\u540d": "\u4f73\u6728\u65af\u5e02",
            "adcode": 230800,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u4f73\u6728\u65af\u5e02\u5e02\u8f96\u533a",
            "adcode": 230801,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u5411\u9633\u533a",
            "adcode": 230803,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u524d\u8fdb\u533a",
            "adcode": 230804,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u98ce\u533a",
            "adcode": 230805,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u90ca\u533a",
            "adcode": 230811,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u6866\u5357\u53bf",
            "adcode": 230822,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u6866\u5ddd\u53bf",
            "adcode": 230826,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u6c64\u539f\u53bf",
            "adcode": 230828,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u540c\u6c5f\u5e02",
            "adcode": 230881,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u9526\u5e02",
            "adcode": 230882,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u8fdc\u5e02",
            "adcode": 230883,
            "citycode": 454
        },
        {
            "\u4e2d\u6587\u540d": "\u4e03\u53f0\u6cb3\u5e02",
            "adcode": 230900,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u4e03\u53f0\u6cb3\u5e02\u5e02\u8f96\u533a",
            "adcode": 230901,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5174\u533a",
            "adcode": 230902,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u6843\u5c71\u533a",
            "adcode": 230903,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u8304\u5b50\u6cb3\u533a",
            "adcode": 230904,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u52c3\u5229\u53bf",
            "adcode": 230921,
            "citycode": 464
        },
        {
            "\u4e2d\u6587\u540d": "\u7261\u4e39\u6c5f\u5e02",
            "adcode": 231000,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u7261\u4e39\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 231001,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5b89\u533a",
            "adcode": 231002,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u660e\u533a",
            "adcode": 231003,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u7231\u6c11\u533a",
            "adcode": 231004,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b89\u533a",
            "adcode": 231005,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u53e3\u53bf",
            "adcode": 231025,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u82ac\u6cb3\u5e02",
            "adcode": 231081,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u6797\u5e02",
            "adcode": 231083,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5b89\u5e02",
            "adcode": 231084,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u7a46\u68f1\u5e02",
            "adcode": 231085,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5b81\u5e02",
            "adcode": 231086,
            "citycode": 453
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed1\u6cb3\u5e02",
            "adcode": 231100,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed1\u6cb3\u5e02\u5e02\u8f96\u533a",
            "adcode": 231101,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u7231\u8f89\u533a",
            "adcode": 231102,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u5ae9\u6c5f\u5e02",
            "adcode": 231183,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u900a\u514b\u53bf",
            "adcode": 231123,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u5b59\u5434\u53bf",
            "adcode": 231124,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u5b89\u5e02",
            "adcode": 231181,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u5927\u8fde\u6c60\u5e02",
            "adcode": 231182,
            "citycode": 456
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u5316\u5e02",
            "adcode": 231200,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u5316\u5e02\u5e02\u8f96\u533a",
            "adcode": 231201,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6797\u533a",
            "adcode": 231202,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u594e\u53bf",
            "adcode": 231221,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u897f\u53bf",
            "adcode": 231222,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5188\u53bf",
            "adcode": 231223,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u5b89\u53bf",
            "adcode": 231224,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u660e\u6c34\u53bf",
            "adcode": 231225,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u68f1\u53bf",
            "adcode": 231226,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u8fbe\u5e02",
            "adcode": 231281,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u8087\u4e1c\u5e02",
            "adcode": 231282,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u4f26\u5e02",
            "adcode": 231283,
            "citycode": 455
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5174\u5b89\u5cad\u5730\u533a",
            "adcode": 232700,
            "citycode": 457
        },
        {
            "\u4e2d\u6587\u540d": "\u52a0\u683c\u8fbe\u5947\u533a",
            "adcode": 232718,
            "citycode": 457
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u739b\u53bf",
            "adcode": 232721,
            "citycode": 457
        },
        {
            "\u4e2d\u6587\u540d": "\u5854\u6cb3\u53bf",
            "adcode": 232722,
            "citycode": 457
        },
        {
            "\u4e2d\u6587\u540d": "\u6f20\u6cb3\u5e02",
            "adcode": 232701,
            "citycode": 457
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u6d77\u5e02",
            "adcode": 310000,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u6d77\u5e02\u5e02\u8f96\u533a",
            "adcode": 310100,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u6d66\u533a",
            "adcode": 310101,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5f90\u6c47\u533a",
            "adcode": 310104,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5b81\u533a",
            "adcode": 310105,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u9759\u5b89\u533a",
            "adcode": 310106,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u9640\u533a",
            "adcode": 310107,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u8679\u53e3\u533a",
            "adcode": 310109,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u6768\u6d66\u533a",
            "adcode": 310110,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u95f5\u884c\u533a",
            "adcode": 310112,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5c71\u533a",
            "adcode": 310113,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5b9a\u533a",
            "adcode": 310114,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u6d66\u4e1c\u65b0\u533a",
            "adcode": 310115,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5c71\u533a",
            "adcode": 310116,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u6c5f\u533a",
            "adcode": 310117,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u6d66\u533a",
            "adcode": 310118,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5949\u8d24\u533a",
            "adcode": 310120,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u660e\u533a",
            "adcode": 310151,
            "citycode": 21
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u4eac\u5e02",
            "adcode": 320100,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u4eac\u5e02\u5e02\u8f96\u533a",
            "adcode": 320101,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u7384\u6b66\u533a",
            "adcode": 320102,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u6dee\u533a",
            "adcode": 320104,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u90ba\u533a",
            "adcode": 320105,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u9f13\u697c\u533a",
            "adcode": 320106,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u6d66\u53e3\u533a",
            "adcode": 320111,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u6816\u971e\u533a",
            "adcode": 320113,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u96e8\u82b1\u53f0\u533a",
            "adcode": 320114,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5b81\u533a",
            "adcode": 320115,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u516d\u5408\u533a",
            "adcode": 320116,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u6ea7\u6c34\u533a",
            "adcode": 320117,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u6df3\u533a",
            "adcode": 320118,
            "citycode": 25
        },
        {
            "\u4e2d\u6587\u540d": "\u65e0\u9521\u5e02",
            "adcode": 320200,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u65e0\u9521\u5e02\u5e02\u8f96\u533a",
            "adcode": 320201,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u9521\u5c71\u533a",
            "adcode": 320205,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u5c71\u533a",
            "adcode": 320206,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u6e56\u533a",
            "adcode": 320211,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u6eaa\u533a",
            "adcode": 320213,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5434\u533a",
            "adcode": 320214,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u9634\u5e02",
            "adcode": 320281,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u5174\u5e02",
            "adcode": 320282,
            "citycode": 510
        },
        {
            "\u4e2d\u6587\u540d": "\u5f90\u5dde\u5e02",
            "adcode": 320300,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u5f90\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 320301,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u9f13\u697c\u533a",
            "adcode": 320302,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u9f99\u533a",
            "adcode": 320303,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u8d3e\u6c6a\u533a",
            "adcode": 320305,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u6cc9\u5c71\u533a",
            "adcode": 320311,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u5c71\u533a",
            "adcode": 320312,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u53bf",
            "adcode": 320321,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u6c9b\u53bf",
            "adcode": 320322,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u7762\u5b81\u53bf",
            "adcode": 320324,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6c82\u5e02",
            "adcode": 320381,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u90b3\u5dde\u5e02",
            "adcode": 320382,
            "citycode": 516
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5dde\u5e02",
            "adcode": 320400,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 320401,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5b81\u533a",
            "adcode": 320402,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u949f\u697c\u533a",
            "adcode": 320404,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5317\u533a",
            "adcode": 320411,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u8fdb\u533a",
            "adcode": 320412,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u575b\u533a",
            "adcode": 320413,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u6ea7\u9633\u5e02",
            "adcode": 320481,
            "citycode": 519
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5dde\u5e02",
            "adcode": 320500,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 320501,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u864e\u4e18\u533a",
            "adcode": 320505,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u4e2d\u533a",
            "adcode": 320506,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u76f8\u57ce\u533a",
            "adcode": 320507,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u59d1\u82cf\u533a",
            "adcode": 320508,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u6c5f\u533a",
            "adcode": 320509,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a",
            "adcode": 320571,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u719f\u5e02",
            "adcode": 320581,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u6e2f\u5e02",
            "adcode": 320582,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u6606\u5c71\u5e02",
            "adcode": 320583,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u4ed3\u5e02",
            "adcode": 320585,
            "citycode": 512
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u901a\u5e02",
            "adcode": 320600,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u901a\u5e02\u5e02\u8f96\u533a",
            "adcode": 320601,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u5ddd\u533a",
            "adcode": 320602,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2f\u95f8\u533a",
            "adcode": 320611,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5dde\u533a",
            "adcode": 320612,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5b89\u5e02",
            "adcode": 320685,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u5982\u4e1c\u53bf",
            "adcode": 320623,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u542f\u4e1c\u5e02",
            "adcode": 320681,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u5982\u768b\u5e02",
            "adcode": 320682,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u95e8\u5e02",
            "adcode": 320684,
            "citycode": 513
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u4e91\u6e2f\u5e02",
            "adcode": 320700,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u4e91\u6e2f\u5e02\u5e02\u8f96\u533a",
            "adcode": 320701,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u4e91\u533a",
            "adcode": 320703,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5dde\u533a",
            "adcode": 320706,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u8d63\u6986\u533a",
            "adcode": 320707,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6d77\u53bf",
            "adcode": 320722,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u704c\u4e91\u53bf",
            "adcode": 320723,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u704c\u5357\u53bf",
            "adcode": 320724,
            "citycode": 518
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5b89\u5e02",
            "adcode": 320800,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 320801,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5b89\u533a",
            "adcode": 320803,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u9634\u533a",
            "adcode": 320804,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6c5f\u6d66\u533a",
            "adcode": 320812,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u6cfd\u533a",
            "adcode": 320813,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u6d9f\u6c34\u53bf",
            "adcode": 320826,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u76f1\u7719\u53bf",
            "adcode": 320830,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6e56\u53bf",
            "adcode": 320831,
            "citycode": 517
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u57ce\u5e02",
            "adcode": 320900,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 320901,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u4ead\u6e56\u533a",
            "adcode": 320902,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u90fd\u533a",
            "adcode": 320903,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u4e30\u533a",
            "adcode": 320904,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u54cd\u6c34\u53bf",
            "adcode": 320921,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u6d77\u53bf",
            "adcode": 320922,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u5b81\u53bf",
            "adcode": 320923,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u5c04\u9633\u53bf",
            "adcode": 320924,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u6e56\u53bf",
            "adcode": 320925,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u53f0\u5e02",
            "adcode": 320981,
            "citycode": 515
        },
        {
            "\u4e2d\u6587\u540d": "\u626c\u5dde\u5e02",
            "adcode": 321000,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u626c\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 321001,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u9675\u533a",
            "adcode": 321002,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u9097\u6c5f\u533a",
            "adcode": 321003,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u90fd\u533a",
            "adcode": 321012,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5e94\u53bf",
            "adcode": 321023,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u4eea\u5f81\u5e02",
            "adcode": 321081,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u90ae\u5e02",
            "adcode": 321084,
            "citycode": 514
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u6c5f\u5e02",
            "adcode": 321100,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 321101,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u4eac\u53e3\u533a",
            "adcode": 321102,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u6da6\u5dde\u533a",
            "adcode": 321111,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u5f92\u533a",
            "adcode": 321112,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u9633\u5e02",
            "adcode": 321181,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u626c\u4e2d\u5e02",
            "adcode": 321182,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u53e5\u5bb9\u5e02",
            "adcode": 321183,
            "citycode": 511
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5dde\u5e02",
            "adcode": 321200,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 321201,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u9675\u533a",
            "adcode": 321202,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u6e2f\u533a",
            "adcode": 321203,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u59dc\u5830\u533a",
            "adcode": 321204,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5316\u5e02",
            "adcode": 321281,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u6c5f\u5e02",
            "adcode": 321282,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5174\u5e02",
            "adcode": 321283,
            "citycode": 523
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u8fc1\u5e02",
            "adcode": 321300,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u8fc1\u5e02\u5e02\u8f96\u533a",
            "adcode": 321301,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u57ce\u533a",
            "adcode": 321302,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u8c6b\u533a",
            "adcode": 321311,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u6cad\u9633\u53bf",
            "adcode": 321322,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u6cd7\u9633\u53bf",
            "adcode": 321323,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u6cd7\u6d2a\u53bf",
            "adcode": 321324,
            "citycode": 527
        },
        {
            "\u4e2d\u6587\u540d": "\u676d\u5dde\u5e02",
            "adcode": 330100,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u676d\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 330101,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u57ce\u533a",
            "adcode": 330102,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0b\u57ce\u533a",
            "adcode": 330103,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5e72\u533a",
            "adcode": 330104,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u62f1\u5885\u533a",
            "adcode": 330105,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u6e56\u533a",
            "adcode": 330106,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u6c5f\u533a",
            "adcode": 330108,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u8427\u5c71\u533a",
            "adcode": 330109,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u4f59\u676d\u533a",
            "adcode": 330110,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u9633\u533a",
            "adcode": 330111,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u5b89\u533a",
            "adcode": 330112,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u6850\u5e90\u53bf",
            "adcode": 330122,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u6df3\u5b89\u53bf",
            "adcode": 330127,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u5fb7\u5e02",
            "adcode": 330182,
            "citycode": 571
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6ce2\u5e02",
            "adcode": 330200,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6ce2\u5e02\u5e02\u8f96\u533a",
            "adcode": 330201,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u66d9\u533a",
            "adcode": 330203,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5317\u533a",
            "adcode": 330205,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u4ed1\u533a",
            "adcode": 330206,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u6d77\u533a",
            "adcode": 330211,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u911e\u5dde\u533a",
            "adcode": 330212,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u5949\u5316\u533a",
            "adcode": 330213,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u8c61\u5c71\u53bf",
            "adcode": 330225,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6d77\u53bf",
            "adcode": 330226,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u4f59\u59da\u5e02",
            "adcode": 330281,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u6148\u6eaa\u5e02",
            "adcode": 330282,
            "citycode": 574
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u5dde\u5e02",
            "adcode": 330300,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 330301,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u9e7f\u57ce\u533a",
            "adcode": 330302,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6e7e\u533a",
            "adcode": 330303,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u74ef\u6d77\u533a",
            "adcode": 330304,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1e\u5934\u533a",
            "adcode": 330305,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5609\u53bf",
            "adcode": 330324,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9633\u53bf",
            "adcode": 330326,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u82cd\u5357\u53bf",
            "adcode": 330327,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u6210\u53bf",
            "adcode": 330328,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u987a\u53bf",
            "adcode": 330329,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u745e\u5b89\u5e02",
            "adcode": 330381,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u6e05\u5e02",
            "adcode": 330382,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6e2f\u5e02",
            "adcode": 330383,
            "citycode": 577
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5174\u5e02",
            "adcode": 330400,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5174\u5e02\u5e02\u8f96\u533a",
            "adcode": 330401,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6e56\u533a",
            "adcode": 330402,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u79c0\u6d32\u533a",
            "adcode": 330411,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5584\u53bf",
            "adcode": 330421,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u76d0\u53bf",
            "adcode": 330424,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5b81\u5e02",
            "adcode": 330481,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6e56\u5e02",
            "adcode": 330482,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u6850\u4e61\u5e02",
            "adcode": 330483,
            "citycode": 573
        },
        {
            "\u4e2d\u6587\u540d": "\u6e56\u5dde\u5e02",
            "adcode": 330500,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u6e56\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 330501,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u5174\u533a",
            "adcode": 330502,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6d54\u533a",
            "adcode": 330503,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u6e05\u53bf",
            "adcode": 330521,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5174\u53bf",
            "adcode": 330522,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5409\u53bf",
            "adcode": 330523,
            "citycode": 572
        },
        {
            "\u4e2d\u6587\u540d": "\u7ecd\u5174\u5e02",
            "adcode": 330600,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u7ecd\u5174\u5e02\u5e02\u8f96\u533a",
            "adcode": 330601,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u8d8a\u57ce\u533a",
            "adcode": 330602,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u67ef\u6865\u533a",
            "adcode": 330603,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u865e\u533a",
            "adcode": 330604,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u660c\u53bf",
            "adcode": 330624,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u8bf8\u66a8\u5e02",
            "adcode": 330681,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u5d4a\u5dde\u5e02",
            "adcode": 330683,
            "citycode": 575
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u534e\u5e02",
            "adcode": 330700,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u534e\u5e02\u5e02\u8f96\u533a",
            "adcode": 330701,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u5a7a\u57ce\u533a",
            "adcode": 330702,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u4e1c\u533a",
            "adcode": 330703,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u4e49\u53bf",
            "adcode": 330723,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u6d66\u6c5f\u53bf",
            "adcode": 330726,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u78d0\u5b89\u53bf",
            "adcode": 330727,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u6eaa\u5e02",
            "adcode": 330781,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u4e49\u4e4c\u5e02",
            "adcode": 330782,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u9633\u5e02",
            "adcode": 330783,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5eb7\u5e02",
            "adcode": 330784,
            "citycode": 579
        },
        {
            "\u4e2d\u6587\u540d": "\u8862\u5dde\u5e02",
            "adcode": 330800,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u8862\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 330801,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u67ef\u57ce\u533a",
            "adcode": 330802,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u8862\u6c5f\u533a",
            "adcode": 330803,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5c71\u53bf",
            "adcode": 330822,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5316\u53bf",
            "adcode": 330824,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6e38\u53bf",
            "adcode": 330825,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5c71\u5e02",
            "adcode": 330881,
            "citycode": 570
        },
        {
            "\u4e2d\u6587\u540d": "\u821f\u5c71\u5e02",
            "adcode": 330900,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u821f\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 330901,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u6d77\u533a",
            "adcode": 330902,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u9640\u533a",
            "adcode": 330903,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb1\u5c71\u53bf",
            "adcode": 330921,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u5d4a\u6cd7\u53bf",
            "adcode": 330922,
            "citycode": 580
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u5dde\u5e02",
            "adcode": 331000,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 331001,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u6912\u6c5f\u533a",
            "adcode": 331002,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5ca9\u533a",
            "adcode": 331003,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u8def\u6865\u533a",
            "adcode": 331004,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u95e8\u53bf",
            "adcode": 331022,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u53f0\u53bf",
            "adcode": 331023,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u4ed9\u5c45\u53bf",
            "adcode": 331024,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u5cad\u5e02",
            "adcode": 331081,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6d77\u5e02",
            "adcode": 331082,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u73af\u5e02",
            "adcode": 331083,
            "citycode": 576
        },
        {
            "\u4e2d\u6587\u540d": "\u4e3d\u6c34\u5e02",
            "adcode": 331100,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u4e3d\u6c34\u5e02\u5e02\u8f96\u533a",
            "adcode": 331101,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u83b2\u90fd\u533a",
            "adcode": 331102,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u7530\u53bf",
            "adcode": 331121,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u7f19\u4e91\u53bf",
            "adcode": 331122,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u660c\u53bf",
            "adcode": 331123,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u9633\u53bf",
            "adcode": 331124,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u548c\u53bf",
            "adcode": 331125,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u5143\u53bf",
            "adcode": 331126,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u5b81\u7572\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 331127,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6cc9\u5e02",
            "adcode": 331181,
            "citycode": 578
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u80a5\u5e02",
            "adcode": 340100,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u80a5\u5e02\u5e02\u8f96\u533a",
            "adcode": 340101,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u7476\u6d77\u533a",
            "adcode": 340102,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u5e90\u9633\u533a",
            "adcode": 340103,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u8700\u5c71\u533a",
            "adcode": 340104,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u5305\u6cb3\u533a",
            "adcode": 340111,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u4e30\u53bf",
            "adcode": 340121,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u80a5\u4e1c\u53bf",
            "adcode": 340122,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u80a5\u897f\u53bf",
            "adcode": 340123,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u5e90\u6c5f\u53bf",
            "adcode": 340124,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u5de2\u6e56\u5e02",
            "adcode": 340181,
            "citycode": 551
        },
        {
            "\u4e2d\u6587\u540d": "\u829c\u6e56\u5e02",
            "adcode": 340200,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u829c\u6e56\u5e02\u5e02\u8f96\u533a",
            "adcode": 340201,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u955c\u6e56\u533a",
            "adcode": 340202,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u5f0b\u6c5f\u533a",
            "adcode": 340203,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u9e20\u6c5f\u533a",
            "adcode": 340207,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u5c71\u533a",
            "adcode": 340208,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u829c\u6e56\u53bf",
            "adcode": 340221,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u7e41\u660c\u53bf",
            "adcode": 340222,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u9675\u53bf",
            "adcode": 340223,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u65e0\u4e3a\u5e02",
            "adcode": 340281,
            "citycode": 553
        },
        {
            "\u4e2d\u6587\u540d": "\u868c\u57e0\u5e02",
            "adcode": 340300,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u868c\u57e0\u5e02\u5e02\u8f96\u533a",
            "adcode": 340301,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5b50\u6e56\u533a",
            "adcode": 340302,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u868c\u5c71\u533a",
            "adcode": 340303,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u79b9\u4f1a\u533a",
            "adcode": 340304,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u4e0a\u533a",
            "adcode": 340311,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u8fdc\u53bf",
            "adcode": 340321,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u6cb3\u53bf",
            "adcode": 340322,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u9547\u53bf",
            "adcode": 340323,
            "citycode": 552
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5357\u5e02",
            "adcode": 340400,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5357\u5e02\u5e02\u8f96\u533a",
            "adcode": 340401,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u901a\u533a",
            "adcode": 340402,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u7530\u5bb6\u5eb5\u533a",
            "adcode": 340403,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u8c22\u5bb6\u96c6\u533a",
            "adcode": 340404,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u516b\u516c\u5c71\u533a",
            "adcode": 340405,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u6f58\u96c6\u533a",
            "adcode": 340406,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u53f0\u53bf",
            "adcode": 340421,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u5bff\u53bf",
            "adcode": 340422,
            "citycode": 554
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u978d\u5c71\u5e02",
            "adcode": 340500,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u978d\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 340501,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u5c71\u533a",
            "adcode": 340503,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u96e8\u5c71\u533a",
            "adcode": 340504,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u671b\u533a",
            "adcode": 340506,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u5f53\u6d82\u53bf",
            "adcode": 340521,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u542b\u5c71\u53bf",
            "adcode": 340522,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u53bf",
            "adcode": 340523,
            "citycode": 555
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5317\u5e02",
            "adcode": 340600,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u5317\u5e02\u5e02\u8f96\u533a",
            "adcode": 340601,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u675c\u96c6\u533a",
            "adcode": 340602,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u76f8\u5c71\u533a",
            "adcode": 340603,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u70c8\u5c71\u533a",
            "adcode": 340604,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u6fc9\u6eaa\u53bf",
            "adcode": 340621,
            "citycode": 561
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u9675\u5e02",
            "adcode": 340700,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u9675\u5e02\u5e02\u8f96\u533a",
            "adcode": 340701,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u5b98\u533a",
            "adcode": 340705,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u4e49\u5b89\u533a",
            "adcode": 340706,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u90ca\u533a",
            "adcode": 340711,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u679e\u9633\u53bf",
            "adcode": 340722,
            "citycode": 562
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5e86\u5e02",
            "adcode": 340800,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5e86\u5e02\u5e02\u8f96\u533a",
            "adcode": 340801,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u8fce\u6c5f\u533a",
            "adcode": 340802,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u89c2\u533a",
            "adcode": 340803,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u79c0\u533a",
            "adcode": 340811,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u5b81\u53bf",
            "adcode": 340822,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u6f5c\u5c71\u5e02",
            "adcode": 340882,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u6e56\u53bf",
            "adcode": 340825,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u677e\u53bf",
            "adcode": 340826,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u6c5f\u53bf",
            "adcode": 340827,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u897f\u53bf",
            "adcode": 340828,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u6850\u57ce\u5e02",
            "adcode": 340881,
            "citycode": 556
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5c71\u5e02",
            "adcode": 341000,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 341001,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u5c6f\u6eaa\u533a",
            "adcode": 341002,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5c71\u533a",
            "adcode": 341003,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u5fbd\u5dde\u533a",
            "adcode": 341004,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u6b59\u53bf",
            "adcode": 341021,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u4f11\u5b81\u53bf",
            "adcode": 341022,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u9edf\u53bf",
            "adcode": 341023,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u7941\u95e8\u53bf",
            "adcode": 341024,
            "citycode": 559
        },
        {
            "\u4e2d\u6587\u540d": "\u6ec1\u5dde\u5e02",
            "adcode": 341100,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u6ec1\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 341101,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u7405\u740a\u533a",
            "adcode": 341102,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u8c2f\u533a",
            "adcode": 341103,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u6765\u5b89\u53bf",
            "adcode": 341122,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u5168\u6912\u53bf",
            "adcode": 341124,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u8fdc\u53bf",
            "adcode": 341125,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u9633\u53bf",
            "adcode": 341126,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u957f\u5e02",
            "adcode": 341181,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u660e\u5149\u5e02",
            "adcode": 341182,
            "citycode": 550
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u9633\u5e02",
            "adcode": 341200,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 341201,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u988d\u5dde\u533a",
            "adcode": 341202,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u988d\u4e1c\u533a",
            "adcode": 341203,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u988d\u6cc9\u533a",
            "adcode": 341204,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6cc9\u53bf",
            "adcode": 341221,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u548c\u53bf",
            "adcode": 341222,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u5357\u53bf",
            "adcode": 341225,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u988d\u4e0a\u53bf",
            "adcode": 341226,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u754c\u9996\u5e02",
            "adcode": 341282,
            "citycode": 1558
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u5dde\u5e02",
            "adcode": 341300,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbf\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 341301,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u57c7\u6865\u533a",
            "adcode": 341302,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u7800\u5c71\u53bf",
            "adcode": 341321,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u8427\u53bf",
            "adcode": 341322,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u74a7\u53bf",
            "adcode": 341323,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u6cd7\u53bf",
            "adcode": 341324,
            "citycode": 557
        },
        {
            "\u4e2d\u6587\u540d": "\u516d\u5b89\u5e02",
            "adcode": 341500,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u516d\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 341501,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5b89\u533a",
            "adcode": 341502,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u88d5\u5b89\u533a",
            "adcode": 341503,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u53f6\u96c6\u533a",
            "adcode": 341504,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u90b1\u53bf",
            "adcode": 341522,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u8212\u57ce\u53bf",
            "adcode": 341523,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5be8\u53bf",
            "adcode": 341524,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u5c71\u53bf",
            "adcode": 341525,
            "citycode": 564
        },
        {
            "\u4e2d\u6587\u540d": "\u4eb3\u5dde\u5e02",
            "adcode": 341600,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u4eb3\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 341601,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u8c2f\u57ce\u533a",
            "adcode": 341602,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u6da1\u9633\u53bf",
            "adcode": 341621,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u8499\u57ce\u53bf",
            "adcode": 341622,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u5229\u8f9b\u53bf",
            "adcode": 341623,
            "citycode": 558
        },
        {
            "\u4e2d\u6587\u540d": "\u6c60\u5dde\u5e02",
            "adcode": 341700,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u6c60\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 341701,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u6c60\u533a",
            "adcode": 341702,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u81f3\u53bf",
            "adcode": 341721,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u53f0\u53bf",
            "adcode": 341722,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u9633\u53bf",
            "adcode": 341723,
            "citycode": 566
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u57ce\u5e02",
            "adcode": 341800,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 341801,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u5dde\u533a",
            "adcode": 341802,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u90ce\u6eaa\u53bf",
            "adcode": 341821,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5fb7\u5e02",
            "adcode": 341822,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfe\u53bf",
            "adcode": 341823,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee9\u6eaa\u53bf",
            "adcode": 341824,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u65cc\u5fb7\u53bf",
            "adcode": 341825,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u56fd\u5e02",
            "adcode": 341881,
            "citycode": 563
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u5dde\u5e02",
            "adcode": 350100,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 350101,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u9f13\u697c\u533a",
            "adcode": 350102,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u6c5f\u533a",
            "adcode": 350103,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u4ed3\u5c71\u533a",
            "adcode": 350104,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u5c3e\u533a",
            "adcode": 350105,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u5b89\u533a",
            "adcode": 350111,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u4e50\u533a",
            "adcode": 350112,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u95fd\u4faf\u53bf",
            "adcode": 350121,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u6c5f\u53bf",
            "adcode": 350122,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u6e90\u53bf",
            "adcode": 350123,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u95fd\u6e05\u53bf",
            "adcode": 350124,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u6cf0\u53bf",
            "adcode": 350125,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6f6d\u53bf",
            "adcode": 350128,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u6e05\u5e02",
            "adcode": 350181,
            "citycode": 591
        },
        {
            "\u4e2d\u6587\u540d": "\u53a6\u95e8\u5e02",
            "adcode": 350200,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u53a6\u95e8\u5e02\u5e02\u8f96\u533a",
            "adcode": 350201,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u601d\u660e\u533a",
            "adcode": 350203,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u6ca7\u533a",
            "adcode": 350205,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u6e56\u91cc\u533a",
            "adcode": 350206,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u96c6\u7f8e\u533a",
            "adcode": 350211,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u540c\u5b89\u533a",
            "adcode": 350212,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u7fd4\u5b89\u533a",
            "adcode": 350213,
            "citycode": 592
        },
        {
            "\u4e2d\u6587\u540d": "\u8386\u7530\u5e02",
            "adcode": 350300,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u8386\u7530\u5e02\u5e02\u8f96\u533a",
            "adcode": 350301,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u53a2\u533a",
            "adcode": 350302,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u6db5\u6c5f\u533a",
            "adcode": 350303,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u8354\u57ce\u533a",
            "adcode": 350304,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u79c0\u5c7f\u533a",
            "adcode": 350305,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u4ed9\u6e38\u53bf",
            "adcode": 350322,
            "citycode": 594
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u660e\u5e02",
            "adcode": 350400,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u660e\u5e02\u5e02\u8f96\u533a",
            "adcode": 350401,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u5217\u533a",
            "adcode": 350402,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u5143\u533a",
            "adcode": 350403,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u660e\u6eaa\u53bf",
            "adcode": 350421,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6d41\u53bf",
            "adcode": 350423,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5316\u53bf",
            "adcode": 350424,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7530\u53bf",
            "adcode": 350425,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u5c24\u6eaa\u53bf",
            "adcode": 350426,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u53bf",
            "adcode": 350427,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u5c06\u4e50\u53bf",
            "adcode": 350428,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5b81\u53bf",
            "adcode": 350429,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u5b81\u53bf",
            "adcode": 350430,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5b89\u5e02",
            "adcode": 350481,
            "citycode": 598
        },
        {
            "\u4e2d\u6587\u540d": "\u6cc9\u5dde\u5e02",
            "adcode": 350500,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u6cc9\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 350501,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u9ca4\u57ce\u533a",
            "adcode": 350502,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u6cfd\u533a",
            "adcode": 350503,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u6c5f\u533a",
            "adcode": 350504,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u6cc9\u6e2f\u533a",
            "adcode": 350505,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u5b89\u53bf",
            "adcode": 350521,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u6eaa\u53bf",
            "adcode": 350524,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u6625\u53bf",
            "adcode": 350525,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5316\u53bf",
            "adcode": 350526,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u95e8\u53bf",
            "adcode": 350527,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u72ee\u5e02",
            "adcode": 350581,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u6c5f\u5e02",
            "adcode": 350582,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5b89\u5e02",
            "adcode": 350583,
            "citycode": 595
        },
        {
            "\u4e2d\u6587\u540d": "\u6f33\u5dde\u5e02",
            "adcode": 350600,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u6f33\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 350601,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u8297\u57ce\u533a",
            "adcode": 350602,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6587\u533a",
            "adcode": 350603,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u9704\u53bf",
            "adcode": 350622,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u6f33\u6d66\u53bf",
            "adcode": 350623,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u8bcf\u5b89\u53bf",
            "adcode": 350624,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6cf0\u53bf",
            "adcode": 350625,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5c71\u53bf",
            "adcode": 350626,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u9756\u53bf",
            "adcode": 350627,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u548c\u53bf",
            "adcode": 350628,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u5b89\u53bf",
            "adcode": 350629,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6d77\u5e02",
            "adcode": 350681,
            "citycode": 596
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5e73\u5e02",
            "adcode": 350700,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5e73\u5e02\u5e02\u8f96\u533a",
            "adcode": 350701,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5e73\u533a",
            "adcode": 350702,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u9633\u533a",
            "adcode": 350703,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u660c\u53bf",
            "adcode": 350721,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u6d66\u57ce\u53bf",
            "adcode": 350722,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u5149\u6cfd\u53bf",
            "adcode": 350723,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u6eaa\u53bf",
            "adcode": 350724,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u653f\u548c\u53bf",
            "adcode": 350725,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u90b5\u6b66\u5e02",
            "adcode": 350781,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5937\u5c71\u5e02",
            "adcode": 350782,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u74ef\u5e02",
            "adcode": 350783,
            "citycode": 599
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5ca9\u5e02",
            "adcode": 350800,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5ca9\u5e02\u5e02\u8f96\u533a",
            "adcode": 350801,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u7f57\u533a",
            "adcode": 350802,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5b9a\u533a",
            "adcode": 350803,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6c40\u53bf",
            "adcode": 350821,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u676d\u53bf",
            "adcode": 350823,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5e73\u53bf",
            "adcode": 350824,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u57ce\u53bf",
            "adcode": 350825,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u6f33\u5e73\u5e02",
            "adcode": 350881,
            "citycode": 597
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5fb7\u5e02",
            "adcode": 350900,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5fb7\u5e02\u5e02\u8f96\u533a",
            "adcode": 350901,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u8549\u57ce\u533a",
            "adcode": 350902,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u971e\u6d66\u53bf",
            "adcode": 350921,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u7530\u53bf",
            "adcode": 350922,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u5c4f\u5357\u53bf",
            "adcode": 350923,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u5bff\u5b81\u53bf",
            "adcode": 350924,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u5468\u5b81\u53bf",
            "adcode": 350925,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u67d8\u8363\u53bf",
            "adcode": 350926,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u5b89\u5e02",
            "adcode": 350981,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u9f0e\u5e02",
            "adcode": 350982,
            "citycode": 593
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u660c\u5e02",
            "adcode": 360100,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u660c\u5e02\u5e02\u8f96\u533a",
            "adcode": 360101,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6e56\u533a",
            "adcode": 360102,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u6e56\u533a",
            "adcode": 360103,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u4e91\u8c31\u533a",
            "adcode": 360104,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5c71\u6e56\u533a",
            "adcode": 360111,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u8c37\u6ee9\u533a",
            "adcode": 360113,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5efa\u533a",
            "adcode": 360112,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u660c\u53bf",
            "adcode": 360121,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u4e49\u53bf",
            "adcode": 360123,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u8fdb\u8d24\u53bf",
            "adcode": 360124,
            "citycode": 791
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u5fb7\u9547\u5e02",
            "adcode": 360200,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u5fb7\u9547\u5e02\u5e02\u8f96\u533a",
            "adcode": 360201,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u6c5f\u533a",
            "adcode": 360202,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u73e0\u5c71\u533a",
            "adcode": 360203,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u6d6e\u6881\u53bf",
            "adcode": 360222,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u5e73\u5e02",
            "adcode": 360281,
            "citycode": 798
        },
        {
            "\u4e2d\u6587\u540d": "\u840d\u4e61\u5e02",
            "adcode": 360300,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u840d\u4e61\u5e02\u5e02\u8f96\u533a",
            "adcode": 360301,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u6e90\u533a",
            "adcode": 360302,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u4e1c\u533a",
            "adcode": 360313,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u83b2\u82b1\u53bf",
            "adcode": 360321,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u6817\u53bf",
            "adcode": 360322,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u82a6\u6eaa\u53bf",
            "adcode": 360323,
            "citycode": 799
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u6c5f\u5e02",
            "adcode": 360400,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 360401,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u6fc2\u6eaa\u533a",
            "adcode": 360402,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u6d54\u9633\u533a",
            "adcode": 360403,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u67f4\u6851\u533a",
            "adcode": 360404,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5b81\u53bf",
            "adcode": 360423,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u4fee\u6c34\u53bf",
            "adcode": 360424,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u4fee\u53bf",
            "adcode": 360425,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5b89\u53bf",
            "adcode": 360426,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u90fd\u660c\u53bf",
            "adcode": 360428,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u6e56\u53e3\u53bf",
            "adcode": 360429,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6d\u6cfd\u53bf",
            "adcode": 360430,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u745e\u660c\u5e02",
            "adcode": 360481,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u5171\u9752\u57ce\u5e02",
            "adcode": 360482,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u5e90\u5c71\u5e02",
            "adcode": 360483,
            "citycode": 792
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4f59\u5e02",
            "adcode": 360500,
            "citycode": 790
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4f59\u5e02\u5e02\u8f96\u533a",
            "adcode": 360501,
            "citycode": 790
        },
        {
            "\u4e2d\u6587\u540d": "\u6e1d\u6c34\u533a",
            "adcode": 360502,
            "citycode": 790
        },
        {
            "\u4e2d\u6587\u540d": "\u5206\u5b9c\u53bf",
            "adcode": 360521,
            "citycode": 790
        },
        {
            "\u4e2d\u6587\u540d": "\u9e70\u6f6d\u5e02",
            "adcode": 360600,
            "citycode": 701
        },
        {
            "\u4e2d\u6587\u540d": "\u9e70\u6f6d\u5e02\u5e02\u8f96\u533a",
            "adcode": 360601,
            "citycode": 701
        },
        {
            "\u4e2d\u6587\u540d": "\u6708\u6e56\u533a",
            "adcode": 360602,
            "citycode": 701
        },
        {
            "\u4e2d\u6587\u540d": "\u4f59\u6c5f\u533a",
            "adcode": 360603,
            "citycode": 701
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u6eaa\u5e02",
            "adcode": 360681,
            "citycode": 701
        },
        {
            "\u4e2d\u6587\u540d": "\u8d63\u5dde\u5e02",
            "adcode": 360700,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u8d63\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 360701,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u7ae0\u8d21\u533a",
            "adcode": 360702,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5eb7\u533a",
            "adcode": 360703,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u8d63\u53bf\u533a",
            "adcode": 360704,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u4fe1\u4e30\u53bf",
            "adcode": 360722,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u4f59\u53bf",
            "adcode": 360723,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u72b9\u53bf",
            "adcode": 360724,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u4e49\u53bf",
            "adcode": 360725,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u8fdc\u53bf",
            "adcode": 360726,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5357\u53bf",
            "adcode": 360727,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u5357\u53bf",
            "adcode": 360728,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5168\u5357\u53bf",
            "adcode": 360729,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u90fd\u53bf",
            "adcode": 360730,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8e\u90fd\u53bf",
            "adcode": 360731,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u56fd\u53bf",
            "adcode": 360732,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u660c\u53bf",
            "adcode": 360733,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5bfb\u4e4c\u53bf",
            "adcode": 360734,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u57ce\u53bf",
            "adcode": 360735,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u745e\u91d1\u5e02",
            "adcode": 360781,
            "citycode": 797
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u5b89\u5e02",
            "adcode": 360800,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 360801,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u5dde\u533a",
            "adcode": 360802,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u539f\u533a",
            "adcode": 360803,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u5b89\u53bf",
            "adcode": 360821,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u6c34\u53bf",
            "adcode": 360822,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5ce1\u6c5f\u53bf",
            "adcode": 360823,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5e72\u53bf",
            "adcode": 360824,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u4e30\u53bf",
            "adcode": 360825,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u548c\u53bf",
            "adcode": 360826,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u5ddd\u53bf",
            "adcode": 360827,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5b89\u53bf",
            "adcode": 360828,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u798f\u53bf",
            "adcode": 360829,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u65b0\u53bf",
            "adcode": 360830,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u4e95\u5188\u5c71\u5e02",
            "adcode": 360881,
            "citycode": 796
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u6625\u5e02",
            "adcode": 360900,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u6625\u5e02\u5e02\u8f96\u533a",
            "adcode": 360901,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u8881\u5dde\u533a",
            "adcode": 360902,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u5949\u65b0\u53bf",
            "adcode": 360921,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u8f7d\u53bf",
            "adcode": 360922,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u9ad8\u53bf",
            "adcode": 360923,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u4e30\u53bf",
            "adcode": 360924,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u5b89\u53bf",
            "adcode": 360925,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u9f13\u53bf",
            "adcode": 360926,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u57ce\u5e02",
            "adcode": 360981,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u6a1f\u6811\u5e02",
            "adcode": 360982,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u5b89\u5e02",
            "adcode": 360983,
            "citycode": 795
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u5dde\u5e02",
            "adcode": 361000,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u629a\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 361001,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u5ddd\u533a",
            "adcode": 361002,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u4e61\u533a",
            "adcode": 361003,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u57ce\u53bf",
            "adcode": 361021,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u9ece\u5ddd\u53bf",
            "adcode": 361022,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u4e30\u53bf",
            "adcode": 361023,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u4ec1\u53bf",
            "adcode": 361024,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u5b89\u53bf",
            "adcode": 361025,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u9ec4\u53bf",
            "adcode": 361026,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6eaa\u53bf",
            "adcode": 361027,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u6eaa\u53bf",
            "adcode": 361028,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u660c\u53bf",
            "adcode": 361030,
            "citycode": 794
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u9976\u5e02",
            "adcode": 361100,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u9976\u5e02\u5e02\u8f96\u533a",
            "adcode": 361101,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u4fe1\u5dde\u533a",
            "adcode": 361102,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u4e30\u533a",
            "adcode": 361103,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u4fe1\u533a",
            "adcode": 361104,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u5c71\u53bf",
            "adcode": 361123,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u94c5\u5c71\u53bf",
            "adcode": 361124,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u6a2a\u5cf0\u53bf",
            "adcode": 361125,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u5f0b\u9633\u53bf",
            "adcode": 361126,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u4f59\u5e72\u53bf",
            "adcode": 361127,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u9131\u9633\u53bf",
            "adcode": 361128,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5e74\u53bf",
            "adcode": 361129,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u5a7a\u6e90\u53bf",
            "adcode": 361130,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5174\u5e02",
            "adcode": 361181,
            "citycode": 793
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u5357\u5e02",
            "adcode": 370100,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u5357\u5e02\u5e02\u8f96\u533a",
            "adcode": 370101,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5386\u4e0b\u533a",
            "adcode": 370102,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u4e2d\u533a",
            "adcode": 370103,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u69d0\u836b\u533a",
            "adcode": 370104,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6865\u533a",
            "adcode": 370105,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5386\u57ce\u533a",
            "adcode": 370112,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6e05\u533a",
            "adcode": 370113,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u7ae0\u4e18\u533a",
            "adcode": 370114,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9634\u53bf",
            "adcode": 370124,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u9633\u533a",
            "adcode": 370115,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u6cb3\u53bf",
            "adcode": 370126,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5c9b\u5e02",
            "adcode": 370200,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5c9b\u5e02\u5e02\u8f96\u533a",
            "adcode": 370201,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u5357\u533a",
            "adcode": 370202,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u5317\u533a",
            "adcode": 370203,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5c9b\u533a",
            "adcode": 370211,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u5d02\u5c71\u533a",
            "adcode": 370212,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u674e\u6ca7\u533a",
            "adcode": 370213,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u9633\u533a",
            "adcode": 370214,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u5373\u58a8\u533a",
            "adcode": 370215,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u80f6\u5dde\u5e02",
            "adcode": 370281,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5ea6\u5e02",
            "adcode": 370283,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u83b1\u897f\u5e02",
            "adcode": 370285,
            "citycode": 532
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc4\u535a\u5e02",
            "adcode": 370300,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc4\u535a\u5e02\u5e02\u8f96\u533a",
            "adcode": 370301,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc4\u5ddd\u533a",
            "adcode": 370302,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5e97\u533a",
            "adcode": 370303,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u5c71\u533a",
            "adcode": 370304,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6dc4\u533a",
            "adcode": 370305,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u5468\u6751\u533a",
            "adcode": 370306,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u6853\u53f0\u53bf",
            "adcode": 370321,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u9752\u53bf",
            "adcode": 370322,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u6c82\u6e90\u53bf",
            "adcode": 370323,
            "citycode": 533
        },
        {
            "\u4e2d\u6587\u540d": "\u67a3\u5e84\u5e02",
            "adcode": 370400,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u67a3\u5e84\u5e02\u5e02\u8f96\u533a",
            "adcode": 370401,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u4e2d\u533a",
            "adcode": 370402,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u859b\u57ce\u533a",
            "adcode": 370403,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u5cc4\u57ce\u533a",
            "adcode": 370404,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u513f\u5e84\u533a",
            "adcode": 370405,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u4ead\u533a",
            "adcode": 370406,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u6ed5\u5dde\u5e02",
            "adcode": 370481,
            "citycode": 632
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u8425\u5e02",
            "adcode": 370500,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u8425\u5e02\u5e02\u8f96\u533a",
            "adcode": 370501,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u8425\u533a",
            "adcode": 370502,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u53e3\u533a",
            "adcode": 370503,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u57a6\u5229\u533a",
            "adcode": 370505,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u5229\u6d25\u53bf",
            "adcode": 370522,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u9976\u53bf",
            "adcode": 370523,
            "citycode": 546
        },
        {
            "\u4e2d\u6587\u540d": "\u70df\u53f0\u5e02",
            "adcode": 370600,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u70df\u53f0\u5e02\u5e02\u8f96\u533a",
            "adcode": 370601,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u829d\u7f58\u533a",
            "adcode": 370602,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u5c71\u533a",
            "adcode": 370611,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u725f\u5e73\u533a",
            "adcode": 370612,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u83b1\u5c71\u533a",
            "adcode": 370613,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5c9b\u53bf",
            "adcode": 370634,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u53e3\u5e02",
            "adcode": 370681,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u83b1\u9633\u5e02",
            "adcode": 370682,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u83b1\u5dde\u5e02",
            "adcode": 370683,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u84ec\u83b1\u5e02",
            "adcode": 370684,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u62db\u8fdc\u5e02",
            "adcode": 370685,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u6816\u971e\u5e02",
            "adcode": 370686,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u9633\u5e02",
            "adcode": 370687,
            "citycode": 535
        },
        {
            "\u4e2d\u6587\u540d": "\u6f4d\u574a\u5e02",
            "adcode": 370700,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u6f4d\u574a\u5e02\u5e02\u8f96\u533a",
            "adcode": 370701,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u6f4d\u57ce\u533a",
            "adcode": 370702,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u5bd2\u4ead\u533a",
            "adcode": 370703,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u574a\u5b50\u533a",
            "adcode": 370704,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u594e\u6587\u533a",
            "adcode": 370705,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6710\u53bf",
            "adcode": 370724,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u4e50\u53bf",
            "adcode": 370725,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5dde\u5e02",
            "adcode": 370781,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u8bf8\u57ce\u5e02",
            "adcode": 370782,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u5bff\u5149\u5e02",
            "adcode": 370783,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u4e18\u5e02",
            "adcode": 370784,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u5bc6\u5e02",
            "adcode": 370785,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u9091\u5e02",
            "adcode": 370786,
            "citycode": 536
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u5b81\u5e02",
            "adcode": 370800,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u5b81\u5e02\u5e02\u8f96\u533a",
            "adcode": 370801,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u4efb\u57ce\u533a",
            "adcode": 370811,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u5156\u5dde\u533a",
            "adcode": 370812,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u5fae\u5c71\u53bf",
            "adcode": 370826,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u9c7c\u53f0\u53bf",
            "adcode": 370827,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u4e61\u53bf",
            "adcode": 370828,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u7965\u53bf",
            "adcode": 370829,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u6c76\u4e0a\u53bf",
            "adcode": 370830,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u6cd7\u6c34\u53bf",
            "adcode": 370831,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u5c71\u53bf",
            "adcode": 370832,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u961c\u5e02",
            "adcode": 370881,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u90b9\u57ce\u5e02",
            "adcode": 370883,
            "citycode": 537
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5b89\u5e02",
            "adcode": 370900,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 370901,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf0\u5c71\u533a",
            "adcode": 370902,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb1\u5cb3\u533a",
            "adcode": 370911,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u9633\u53bf",
            "adcode": 370921,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5e73\u53bf",
            "adcode": 370923,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6cf0\u5e02",
            "adcode": 370982,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u80a5\u57ce\u5e02",
            "adcode": 370983,
            "citycode": 538
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u6d77\u5e02",
            "adcode": 371000,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u6d77\u5e02\u5e02\u8f96\u533a",
            "adcode": 371001,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u73af\u7fe0\u533a",
            "adcode": 371002,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u767b\u533a",
            "adcode": 371003,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u8363\u6210\u5e02",
            "adcode": 371082,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u4e73\u5c71\u5e02",
            "adcode": 371083,
            "citycode": 631
        },
        {
            "\u4e2d\u6587\u540d": "\u65e5\u7167\u5e02",
            "adcode": 371100,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u65e5\u7167\u5e02\u5e02\u8f96\u533a",
            "adcode": 371101,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6e2f\u533a",
            "adcode": 371102,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u5c9a\u5c71\u533a",
            "adcode": 371103,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u83b2\u53bf",
            "adcode": 371121,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u8392\u53bf",
            "adcode": 371122,
            "citycode": 633
        },
        {
            "\u4e2d\u6587\u540d": "\u83b1\u829c\u533a",
            "adcode": 370116,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u94a2\u57ce\u533a",
            "adcode": 370117,
            "citycode": 531
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6c82\u5e02",
            "adcode": 371300,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6c82\u5e02\u5e02\u8f96\u533a",
            "adcode": 371301,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u5c71\u533a",
            "adcode": 371302,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u5e84\u533a",
            "adcode": 371311,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u4e1c\u533a",
            "adcode": 371312,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u6c82\u5357\u53bf",
            "adcode": 371321,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u90ef\u57ce\u53bf",
            "adcode": 371322,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u6c82\u6c34\u53bf",
            "adcode": 371323,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u9675\u53bf",
            "adcode": 371324,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u8d39\u53bf",
            "adcode": 371325,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9091\u53bf",
            "adcode": 371326,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u8392\u5357\u53bf",
            "adcode": 371327,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u8499\u9634\u53bf",
            "adcode": 371328,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6cad\u53bf",
            "adcode": 371329,
            "citycode": 539
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5dde\u5e02",
            "adcode": 371400,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 371401,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u57ce\u533a",
            "adcode": 371402,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u9675\u57ce\u533a",
            "adcode": 371403,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6d25\u53bf",
            "adcode": 371422,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u4e91\u53bf",
            "adcode": 371423,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u9091\u53bf",
            "adcode": 371424,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u9f50\u6cb3\u53bf",
            "adcode": 371425,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u539f\u53bf",
            "adcode": 371426,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u590f\u6d25\u53bf",
            "adcode": 371427,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u57ce\u53bf",
            "adcode": 371428,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u9675\u5e02",
            "adcode": 371481,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u79b9\u57ce\u5e02",
            "adcode": 371482,
            "citycode": 534
        },
        {
            "\u4e2d\u6587\u540d": "\u804a\u57ce\u5e02",
            "adcode": 371500,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u804a\u57ce\u5e02\u5e02\u8f96\u533a",
            "adcode": 371501,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u660c\u5e9c\u533a",
            "adcode": 371502,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u8c37\u53bf",
            "adcode": 371521,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u8398\u53bf",
            "adcode": 371522,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u830c\u5e73\u533a",
            "adcode": 371503,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u963f\u53bf",
            "adcode": 371524,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u51a0\u53bf",
            "adcode": 371525,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u5510\u53bf",
            "adcode": 371526,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6e05\u5e02",
            "adcode": 371581,
            "citycode": 635
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u5dde\u5e02",
            "adcode": 371600,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 371601,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u6ee8\u57ce\u533a",
            "adcode": 371602,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbe\u5316\u533a",
            "adcode": 371603,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u6c11\u53bf",
            "adcode": 371621,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u4fe1\u53bf",
            "adcode": 371622,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u65e0\u68e3\u53bf",
            "adcode": 371623,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u5174\u53bf",
            "adcode": 371625,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u90b9\u5e73\u5e02",
            "adcode": 371681,
            "citycode": 543
        },
        {
            "\u4e2d\u6587\u540d": "\u83cf\u6cfd\u5e02",
            "adcode": 371700,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u83cf\u6cfd\u5e02\u5e02\u8f96\u533a",
            "adcode": 371701,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u7261\u4e39\u533a",
            "adcode": 371702,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u9676\u533a",
            "adcode": 371703,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u66f9\u53bf",
            "adcode": 371721,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u5355\u53bf",
            "adcode": 371722,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u6b66\u53bf",
            "adcode": 371723,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u5de8\u91ce\u53bf",
            "adcode": 371724,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u90d3\u57ce\u53bf",
            "adcode": 371725,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u9104\u57ce\u53bf",
            "adcode": 371726,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u660e\u53bf",
            "adcode": 371728,
            "citycode": 530
        },
        {
            "\u4e2d\u6587\u540d": "\u90d1\u5dde\u5e02",
            "adcode": 410100,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u90d1\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 410101,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u539f\u533a",
            "adcode": 410102,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8c\u4e03\u533a",
            "adcode": 410103,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u7ba1\u57ce\u56de\u65cf\u533a",
            "adcode": 410104,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6c34\u533a",
            "adcode": 410105,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u8857\u533a",
            "adcode": 410106,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u6d4e\u533a",
            "adcode": 410108,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u725f\u53bf",
            "adcode": 410122,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u5de9\u4e49\u5e02",
            "adcode": 410181,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u8365\u9633\u5e02",
            "adcode": 410182,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5bc6\u5e02",
            "adcode": 410183,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u90d1\u5e02",
            "adcode": 410184,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u767b\u5c01\u5e02",
            "adcode": 410185,
            "citycode": 371
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5c01\u5e02",
            "adcode": 410200,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5c01\u5e02\u5e02\u8f96\u533a",
            "adcode": 410201,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u4ead\u533a",
            "adcode": 410202,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u6cb3\u56de\u65cf\u533a",
            "adcode": 410203,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u9f13\u697c\u533a",
            "adcode": 410204,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u79b9\u738b\u53f0\u533a",
            "adcode": 410205,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u7965\u7b26\u533a",
            "adcode": 410212,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u675e\u53bf",
            "adcode": 410221,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u8bb8\u53bf",
            "adcode": 410222,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u5c09\u6c0f\u53bf",
            "adcode": 410223,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u8003\u53bf",
            "adcode": 410225,
            "citycode": 378
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u9633\u5e02",
            "adcode": 410300,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 410301,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u8001\u57ce\u533a",
            "adcode": 410302,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5de5\u533a",
            "adcode": 410303,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u700d\u6cb3\u56de\u65cf\u533a",
            "adcode": 410304,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u6da7\u897f\u533a",
            "adcode": 410305,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u5229\u533a",
            "adcode": 410306,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u9f99\u533a",
            "adcode": 410311,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5f\u6d25\u53bf",
            "adcode": 410322,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5b89\u53bf",
            "adcode": 410323,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u683e\u5ddd\u53bf",
            "adcode": 410324,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5d69\u53bf",
            "adcode": 410325,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5d\u9633\u53bf",
            "adcode": 410326,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u9633\u53bf",
            "adcode": 410327,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u5b81\u53bf",
            "adcode": 410328,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u5ddd\u53bf",
            "adcode": 410329,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5043\u5e08\u5e02",
            "adcode": 410381,
            "citycode": 379
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9876\u5c71\u5e02",
            "adcode": 410400,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u9876\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 410401,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u534e\u533a",
            "adcode": 410402,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u536b\u4e1c\u533a",
            "adcode": 410403,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u9f99\u533a",
            "adcode": 410404,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u6e5b\u6cb3\u533a",
            "adcode": 410411,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u4e30\u53bf",
            "adcode": 410421,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u53f6\u53bf",
            "adcode": 410422,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u9c81\u5c71\u53bf",
            "adcode": 410423,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u90cf\u53bf",
            "adcode": 410425,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u821e\u94a2\u5e02",
            "adcode": 410481,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5d\u5dde\u5e02",
            "adcode": 410482,
            "citycode": 375
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u9633\u5e02",
            "adcode": 410500,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 410501,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u5cf0\u533a",
            "adcode": 410502,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u5173\u533a",
            "adcode": 410503,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u6bb7\u90fd\u533a",
            "adcode": 410505,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5b89\u533a",
            "adcode": 410506,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u9633\u53bf",
            "adcode": 410522,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u6c64\u9634\u53bf",
            "adcode": 410523,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u6ed1\u53bf",
            "adcode": 410526,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u5185\u9ec4\u53bf",
            "adcode": 410527,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u5dde\u5e02",
            "adcode": 410581,
            "citycode": 372
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u58c1\u5e02",
            "adcode": 410600,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u58c1\u5e02\u5e02\u8f96\u533a",
            "adcode": 410601,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5c71\u533a",
            "adcode": 410602,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u57ce\u533a",
            "adcode": 410603,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc7\u6ee8\u533a",
            "adcode": 410611,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u6d5a\u53bf",
            "adcode": 410621,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc7\u53bf",
            "adcode": 410622,
            "citycode": 392
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4e61\u5e02",
            "adcode": 410700,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4e61\u5e02\u5e02\u8f96\u533a",
            "adcode": 410701,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u65d7\u533a",
            "adcode": 410702,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u536b\u6ee8\u533a",
            "adcode": 410703,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u6cc9\u533a",
            "adcode": 410704,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u7267\u91ce\u533a",
            "adcode": 410711,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4e61\u53bf",
            "adcode": 410721,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u83b7\u5609\u53bf",
            "adcode": 410724,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u539f\u9633\u53bf",
            "adcode": 410725,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u6d25\u53bf",
            "adcode": 410726,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u5c01\u4e18\u53bf",
            "adcode": 410727,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u57a3\u5e02",
            "adcode": 410783,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u536b\u8f89\u5e02",
            "adcode": 410781,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u8f89\u53bf\u5e02",
            "adcode": 410782,
            "citycode": 373
        },
        {
            "\u4e2d\u6587\u540d": "\u7126\u4f5c\u5e02",
            "adcode": 410800,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u7126\u4f5c\u5e02\u5e02\u8f96\u533a",
            "adcode": 410801,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u89e3\u653e\u533a",
            "adcode": 410802,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u7ad9\u533a",
            "adcode": 410803,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u6751\u533a",
            "adcode": 410804,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u9633\u533a",
            "adcode": 410811,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u4fee\u6b66\u53bf",
            "adcode": 410821,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u7231\u53bf",
            "adcode": 410822,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u965f\u53bf",
            "adcode": 410823,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u53bf",
            "adcode": 410825,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u6c81\u9633\u5e02",
            "adcode": 410882,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5f\u5dde\u5e02",
            "adcode": 410883,
            "citycode": 391
        },
        {
            "\u4e2d\u6587\u540d": "\u6fee\u9633\u5e02",
            "adcode": 410900,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u6fee\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 410901,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u9f99\u533a",
            "adcode": 410902,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u4e30\u53bf",
            "adcode": 410922,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u4e50\u53bf",
            "adcode": 410923,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u8303\u53bf",
            "adcode": 410926,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u524d\u53bf",
            "adcode": 410927,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u6fee\u9633\u53bf",
            "adcode": 410928,
            "citycode": 393
        },
        {
            "\u4e2d\u6587\u540d": "\u8bb8\u660c\u5e02",
            "adcode": 411000,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u8bb8\u660c\u5e02\u5e02\u8f96\u533a",
            "adcode": 411001,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u9b4f\u90fd\u533a",
            "adcode": 411002,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u5b89\u533a",
            "adcode": 411003,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u9122\u9675\u53bf",
            "adcode": 411024,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u57ce\u53bf",
            "adcode": 411025,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u79b9\u5dde\u5e02",
            "adcode": 411081,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u845b\u5e02",
            "adcode": 411082,
            "citycode": 374
        },
        {
            "\u4e2d\u6587\u540d": "\u6f2f\u6cb3\u5e02",
            "adcode": 411100,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u6f2f\u6cb3\u5e02\u5e02\u8f96\u533a",
            "adcode": 411101,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u6e90\u6c47\u533a",
            "adcode": 411102,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u90fe\u57ce\u533a",
            "adcode": 411103,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u53ec\u9675\u533a",
            "adcode": 411104,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u821e\u9633\u53bf",
            "adcode": 411121,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u988d\u53bf",
            "adcode": 411122,
            "citycode": 395
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u95e8\u5ce1\u5e02",
            "adcode": 411200,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u95e8\u5ce1\u5e02\u5e02\u8f96\u533a",
            "adcode": 411201,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u6e56\u6ee8\u533a",
            "adcode": 411202,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u9655\u5dde\u533a",
            "adcode": 411203,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u6e11\u6c60\u53bf",
            "adcode": 411221,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u5362\u6c0f\u53bf",
            "adcode": 411224,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u4e49\u9a6c\u5e02",
            "adcode": 411281,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u5b9d\u5e02",
            "adcode": 411282,
            "citycode": 398
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u9633\u5e02",
            "adcode": 411300,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 411301,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9b\u57ce\u533a",
            "adcode": 411302,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5367\u9f99\u533a",
            "adcode": 411303,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u53ec\u53bf",
            "adcode": 411321,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u65b9\u57ce\u53bf",
            "adcode": 411322,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5ce1\u53bf",
            "adcode": 411323,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u5e73\u53bf",
            "adcode": 411324,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5185\u4e61\u53bf",
            "adcode": 411325,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u6dc5\u5ddd\u53bf",
            "adcode": 411326,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u793e\u65d7\u53bf",
            "adcode": 411327,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5510\u6cb3\u53bf",
            "adcode": 411328,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u91ce\u53bf",
            "adcode": 411329,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u6850\u67cf\u53bf",
            "adcode": 411330,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u9093\u5dde\u5e02",
            "adcode": 411381,
            "citycode": 377
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u4e18\u5e02",
            "adcode": 411400,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u4e18\u5e02\u5e02\u8f96\u533a",
            "adcode": 411401,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u56ed\u533a",
            "adcode": 411402,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u7762\u9633\u533a",
            "adcode": 411403,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u6c11\u6743\u53bf",
            "adcode": 411421,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u7762\u53bf",
            "adcode": 411422,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u9675\u53bf",
            "adcode": 411423,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u67d8\u57ce\u53bf",
            "adcode": 411424,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u865e\u57ce\u53bf",
            "adcode": 411425,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u590f\u9091\u53bf",
            "adcode": 411426,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u57ce\u5e02",
            "adcode": 411481,
            "citycode": 370
        },
        {
            "\u4e2d\u6587\u540d": "\u4fe1\u9633\u5e02",
            "adcode": 411500,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u4fe1\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 411501,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u6d49\u6cb3\u533a",
            "adcode": 411502,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6865\u533a",
            "adcode": 411503,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u5c71\u53bf",
            "adcode": 411521,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u5149\u5c71\u53bf",
            "adcode": 411522,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u53bf",
            "adcode": 411523,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u57ce\u53bf",
            "adcode": 411524,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u59cb\u53bf",
            "adcode": 411525,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u6f62\u5ddd\u53bf",
            "adcode": 411526,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u6ee8\u53bf",
            "adcode": 411527,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u606f\u53bf",
            "adcode": 411528,
            "citycode": 376
        },
        {
            "\u4e2d\u6587\u540d": "\u5468\u53e3\u5e02",
            "adcode": 411600,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u5468\u53e3\u5e02\u5e02\u8f96\u533a",
            "adcode": 411601,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u5ddd\u6c47\u533a",
            "adcode": 411602,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u6276\u6c9f\u53bf",
            "adcode": 411621,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u534e\u53bf",
            "adcode": 411622,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u6c34\u53bf",
            "adcode": 411623,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u6c88\u4e18\u53bf",
            "adcode": 411624,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u90f8\u57ce\u53bf",
            "adcode": 411625,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u6dee\u9633\u533a",
            "adcode": 411603,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u5eb7\u53bf",
            "adcode": 411627,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u9e7f\u9091\u53bf",
            "adcode": 411628,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u9879\u57ce\u5e02",
            "adcode": 411681,
            "citycode": 394
        },
        {
            "\u4e2d\u6587\u540d": "\u9a7b\u9a6c\u5e97\u5e02",
            "adcode": 411700,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u9a7b\u9a6c\u5e97\u5e02\u5e02\u8f96\u533a",
            "adcode": 411701,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u9a7f\u57ce\u533a",
            "adcode": 411702,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5e73\u53bf",
            "adcode": 411721,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u8521\u53bf",
            "adcode": 411722,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u8206\u53bf",
            "adcode": 411723,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u9633\u53bf",
            "adcode": 411724,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u786e\u5c71\u53bf",
            "adcode": 411725,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u6ccc\u9633\u53bf",
            "adcode": 411726,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5d\u5357\u53bf",
            "adcode": 411727,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u5e73\u53bf",
            "adcode": 411728,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u8521\u53bf",
            "adcode": 411729,
            "citycode": 396
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4e\u6e90\u5e02",
            "adcode": 419001,
            "citycode": 1391
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u6c49\u5e02",
            "adcode": 420100,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u6c49\u5e02\u5e02\u8f96\u533a",
            "adcode": 420101,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5cb8\u533a",
            "adcode": 420102,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6c49\u533a",
            "adcode": 420103,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u785a\u53e3\u533a",
            "adcode": 420104,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u9633\u533a",
            "adcode": 420105,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u660c\u533a",
            "adcode": 420106,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5c71\u533a",
            "adcode": 420107,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u5c71\u533a",
            "adcode": 420111,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u897f\u6e56\u533a",
            "adcode": 420112,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u5357\u533a",
            "adcode": 420113,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u8521\u7538\u533a",
            "adcode": 420114,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u590f\u533a",
            "adcode": 420115,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u9642\u533a",
            "adcode": 420116,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6d32\u533a",
            "adcode": 420117,
            "citycode": 27
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u77f3\u5e02",
            "adcode": 420200,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u77f3\u5e02\u5e02\u8f96\u533a",
            "adcode": 420201,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u77f3\u6e2f\u533a",
            "adcode": 420202,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u585e\u5c71\u533a",
            "adcode": 420203,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0b\u9646\u533a",
            "adcode": 420204,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u5c71\u533a",
            "adcode": 420205,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u65b0\u53bf",
            "adcode": 420222,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u51b6\u5e02",
            "adcode": 420281,
            "citycode": 714
        },
        {
            "\u4e2d\u6587\u540d": "\u5341\u5830\u5e02",
            "adcode": 420300,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u5341\u5830\u5e02\u5e02\u8f96\u533a",
            "adcode": 420301,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u8305\u7bad\u533a",
            "adcode": 420302,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u6e7e\u533a",
            "adcode": 420303,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u90e7\u9633\u533a",
            "adcode": 420304,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u90e7\u897f\u53bf",
            "adcode": 420322,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u7af9\u5c71\u53bf",
            "adcode": 420323,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u7af9\u6eaa\u53bf",
            "adcode": 420324,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u623f\u53bf",
            "adcode": 420325,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u6c5f\u53e3\u5e02",
            "adcode": 420381,
            "citycode": 719
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u660c\u5e02",
            "adcode": 420500,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u660c\u5e02\u5e02\u8f96\u533a",
            "adcode": 420501,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u9675\u533a",
            "adcode": 420502,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0d\u5bb6\u5c97\u533a",
            "adcode": 420503,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u70b9\u519b\u533a",
            "adcode": 420504,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u7307\u4ead\u533a",
            "adcode": 420505,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u5937\u9675\u533a",
            "adcode": 420506,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u8fdc\u5b89\u53bf",
            "adcode": 420525,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5c71\u53bf",
            "adcode": 420526,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u79ed\u5f52\u53bf",
            "adcode": 420527,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u9633\u571f\u5bb6\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 420528,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u5cf0\u571f\u5bb6\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 420529,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u90fd\u5e02",
            "adcode": 420581,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u5f53\u9633\u5e02",
            "adcode": 420582,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u679d\u6c5f\u5e02",
            "adcode": 420583,
            "citycode": 717
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u9633\u5e02",
            "adcode": 420600,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 420601,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u57ce\u533a",
            "adcode": 420602,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u6a0a\u57ce\u533a",
            "adcode": 420606,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u8944\u5dde\u533a",
            "adcode": 420607,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6f33\u53bf",
            "adcode": 420624,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u8c37\u57ce\u53bf",
            "adcode": 420625,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5eb7\u53bf",
            "adcode": 420626,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u8001\u6cb3\u53e3\u5e02",
            "adcode": 420682,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u67a3\u9633\u5e02",
            "adcode": 420683,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u57ce\u5e02",
            "adcode": 420684,
            "citycode": 710
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u5dde\u5e02",
            "adcode": 420700,
            "citycode": 711
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 420701,
            "citycode": 711
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u5b50\u6e56\u533a",
            "adcode": 420702,
            "citycode": 711
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u5bb9\u533a",
            "adcode": 420703,
            "citycode": 711
        },
        {
            "\u4e2d\u6587\u540d": "\u9102\u57ce\u533a",
            "adcode": 420704,
            "citycode": 711
        },
        {
            "\u4e2d\u6587\u540d": "\u8346\u95e8\u5e02",
            "adcode": 420800,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u8346\u95e8\u5e02\u5e02\u8f96\u533a",
            "adcode": 420801,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5b9d\u533a",
            "adcode": 420802,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u6387\u5200\u533a",
            "adcode": 420804,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u4eac\u5c71\u5e02",
            "adcode": 420882,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u6d0b\u53bf",
            "adcode": 420822,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u949f\u7965\u5e02",
            "adcode": 420881,
            "citycode": 724
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5d\u611f\u5e02",
            "adcode": 420900,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5d\u611f\u5e02\u5e02\u8f96\u533a",
            "adcode": 420901,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5d\u5357\u533a",
            "adcode": 420902,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5d\u660c\u53bf",
            "adcode": 420921,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u609f\u53bf",
            "adcode": 420922,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u68a6\u53bf",
            "adcode": 420923,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5e94\u57ce\u5e02",
            "adcode": 420981,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u9646\u5e02",
            "adcode": 420982,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u5ddd\u5e02",
            "adcode": 420984,
            "citycode": 712
        },
        {
            "\u4e2d\u6587\u540d": "\u8346\u5dde\u5e02",
            "adcode": 421000,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u8346\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 421001,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u5e02\u533a",
            "adcode": 421002,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u8346\u5dde\u533a",
            "adcode": 421003,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u516c\u5b89\u53bf",
            "adcode": 421022,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u76d1\u5229\u53bf",
            "adcode": 421023,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u9675\u53bf",
            "adcode": 421024,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u9996\u5e02",
            "adcode": 421081,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u6e56\u5e02",
            "adcode": 421083,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u6ecb\u5e02",
            "adcode": 421087,
            "citycode": 716
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5188\u5e02",
            "adcode": 421100,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5188\u5e02\u5e02\u8f96\u533a",
            "adcode": 421101,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5dde\u533a",
            "adcode": 421102,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u56e2\u98ce\u53bf",
            "adcode": 421121,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u5b89\u53bf",
            "adcode": 421122,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u7530\u53bf",
            "adcode": 421123,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u82f1\u5c71\u53bf",
            "adcode": 421124,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u6d60\u6c34\u53bf",
            "adcode": 421125,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u8572\u6625\u53bf",
            "adcode": 421126,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u6885\u53bf",
            "adcode": 421127,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u57ce\u5e02",
            "adcode": 421181,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u7a74\u5e02",
            "adcode": 421182,
            "citycode": 713
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u5b81\u5e02",
            "adcode": 421200,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u5b81\u5e02\u5e02\u8f96\u533a",
            "adcode": 421201,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u5b89\u533a",
            "adcode": 421202,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u9c7c\u53bf",
            "adcode": 421221,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u57ce\u53bf",
            "adcode": 421222,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u9633\u53bf",
            "adcode": 421223,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5c71\u53bf",
            "adcode": 421224,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u58c1\u5e02",
            "adcode": 421281,
            "citycode": 715
        },
        {
            "\u4e2d\u6587\u540d": "\u968f\u5dde\u5e02",
            "adcode": 421300,
            "citycode": 722
        },
        {
            "\u4e2d\u6587\u540d": "\u968f\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 421301,
            "citycode": 722
        },
        {
            "\u4e2d\u6587\u540d": "\u66fe\u90fd\u533a",
            "adcode": 421303,
            "citycode": 722
        },
        {
            "\u4e2d\u6587\u540d": "\u968f\u53bf",
            "adcode": 421321,
            "citycode": 722
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u6c34\u5e02",
            "adcode": 421381,
            "citycode": 722
        },
        {
            "\u4e2d\u6587\u540d": "\u6069\u65bd\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 422800,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u6069\u65bd\u5e02",
            "adcode": 422801,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u5229\u5ddd\u5e02",
            "adcode": 422802,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u59cb\u53bf",
            "adcode": 422822,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u4e1c\u53bf",
            "adcode": 422823,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u6069\u53bf",
            "adcode": 422825,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u4e30\u53bf",
            "adcode": 422826,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u6765\u51e4\u53bf",
            "adcode": 422827,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5cf0\u53bf",
            "adcode": 422828,
            "citycode": 718
        },
        {
            "\u4e2d\u6587\u540d": "\u4ed9\u6843\u5e02",
            "adcode": 429004,
            "citycode": 728
        },
        {
            "\u4e2d\u6587\u540d": "\u6f5c\u6c5f\u5e02",
            "adcode": 429005,
            "citycode": 2728
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u95e8\u5e02",
            "adcode": 429006,
            "citycode": 1728
        },
        {
            "\u4e2d\u6587\u540d": "\u795e\u519c\u67b6\u6797\u533a",
            "adcode": 429021,
            "citycode": 1719
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6c99\u5e02",
            "adcode": 430100,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6c99\u5e02\u5e02\u8f96\u533a",
            "adcode": 430101,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u8299\u84c9\u533a",
            "adcode": 430102,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5fc3\u533a",
            "adcode": 430103,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u9e93\u533a",
            "adcode": 430104,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u798f\u533a",
            "adcode": 430105,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u96e8\u82b1\u533a",
            "adcode": 430111,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u57ce\u533a",
            "adcode": 430112,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6c99\u53bf",
            "adcode": 430121,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u6d4f\u9633\u5e02",
            "adcode": 430181,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u4e61\u5e02",
            "adcode": 430182,
            "citycode": 731
        },
        {
            "\u4e2d\u6587\u540d": "\u682a\u6d32\u5e02",
            "adcode": 430200,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u682a\u6d32\u5e02\u5e02\u8f96\u533a",
            "adcode": 430201,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u8377\u5858\u533a",
            "adcode": 430202,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u82a6\u6dde\u533a",
            "adcode": 430203,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5cf0\u533a",
            "adcode": 430204,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5143\u533a",
            "adcode": 430211,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u6e0c\u53e3\u533a",
            "adcode": 430212,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u6538\u53bf",
            "adcode": 430223,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u8336\u9675\u53bf",
            "adcode": 430224,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u708e\u9675\u53bf",
            "adcode": 430225,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u91b4\u9675\u5e02",
            "adcode": 430281,
            "citycode": 733
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u6f6d\u5e02",
            "adcode": 430300,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u6f6d\u5e02\u5e02\u8f96\u533a",
            "adcode": 430301,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u96e8\u6e56\u533a",
            "adcode": 430302,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u5858\u533a",
            "adcode": 430304,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u6f6d\u53bf",
            "adcode": 430321,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u4e61\u5e02",
            "adcode": 430381,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u97f6\u5c71\u5e02",
            "adcode": 430382,
            "citycode": 732
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u9633\u5e02",
            "adcode": 430400,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 430401,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u73e0\u6656\u533a",
            "adcode": 430405,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u96c1\u5cf0\u533a",
            "adcode": 430406,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u9f13\u533a",
            "adcode": 430407,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u84b8\u6e58\u533a",
            "adcode": 430408,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5cb3\u533a",
            "adcode": 430412,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u9633\u53bf",
            "adcode": 430421,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u5357\u53bf",
            "adcode": 430422,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u5c71\u53bf",
            "adcode": 430423,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8861\u4e1c\u53bf",
            "adcode": 430424,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u7941\u4e1c\u53bf",
            "adcode": 430426,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u8012\u9633\u5e02",
            "adcode": 430481,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5b81\u5e02",
            "adcode": 430482,
            "citycode": 734
        },
        {
            "\u4e2d\u6587\u540d": "\u90b5\u9633\u5e02",
            "adcode": 430500,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u90b5\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 430501,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6e05\u533a",
            "adcode": 430502,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7965\u533a",
            "adcode": 430503,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u5854\u533a",
            "adcode": 430511,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u90b5\u4e1c\u5e02",
            "adcode": 430582,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u90b5\u53bf",
            "adcode": 430522,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u90b5\u9633\u53bf",
            "adcode": 430523,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u56de\u53bf",
            "adcode": 430524,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1e\u53e3\u53bf",
            "adcode": 430525,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u5b81\u53bf",
            "adcode": 430527,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5b81\u53bf",
            "adcode": 430528,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u6b65\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 430529,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5188\u5e02",
            "adcode": 430581,
            "citycode": 739
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u9633\u5e02",
            "adcode": 430600,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 430601,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u9633\u697c\u533a",
            "adcode": 430602,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u6eaa\u533a",
            "adcode": 430603,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u541b\u5c71\u533a",
            "adcode": 430611,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u9633\u53bf",
            "adcode": 430621,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u5bb9\u53bf",
            "adcode": 430623,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u9634\u53bf",
            "adcode": 430624,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6c5f\u53bf",
            "adcode": 430626,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u6c68\u7f57\u5e02",
            "adcode": 430681,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6e58\u5e02",
            "adcode": 430682,
            "citycode": 730
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5fb7\u5e02",
            "adcode": 430700,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u5e38\u5fb7\u5e02\u5e02\u8f96\u533a",
            "adcode": 430701,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u9675\u533a",
            "adcode": 430702,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u9f0e\u57ce\u533a",
            "adcode": 430703,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u4e61\u53bf",
            "adcode": 430721,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u5bff\u53bf",
            "adcode": 430722,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u6fa7\u53bf",
            "adcode": 430723,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6fa7\u53bf",
            "adcode": 430724,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u6843\u6e90\u53bf",
            "adcode": 430725,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u95e8\u53bf",
            "adcode": 430726,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u6d25\u5e02\u5e02",
            "adcode": 430781,
            "citycode": 736
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u754c\u5e02",
            "adcode": 430800,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u754c\u5e02\u5e02\u8f96\u533a",
            "adcode": 430801,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5b9a\u533a",
            "adcode": 430802,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u9675\u6e90\u533a",
            "adcode": 430811,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u6148\u5229\u53bf",
            "adcode": 430821,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u6851\u690d\u53bf",
            "adcode": 430822,
            "citycode": 744
        },
        {
            "\u4e2d\u6587\u540d": "\u76ca\u9633\u5e02",
            "adcode": 430900,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u76ca\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 430901,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u9633\u533a",
            "adcode": 430902,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u8d6b\u5c71\u533a",
            "adcode": 430903,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u53bf",
            "adcode": 430921,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u6843\u6c5f\u53bf",
            "adcode": 430922,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5316\u53bf",
            "adcode": 430923,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u6c85\u6c5f\u5e02",
            "adcode": 430981,
            "citycode": 737
        },
        {
            "\u4e2d\u6587\u540d": "\u90f4\u5dde\u5e02",
            "adcode": 431000,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u90f4\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 431001,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6e56\u533a",
            "adcode": 431002,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u82cf\u4ed9\u533a",
            "adcode": 431003,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u6842\u9633\u53bf",
            "adcode": 431021,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u7ae0\u53bf",
            "adcode": 431022,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5174\u53bf",
            "adcode": 431023,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u79be\u53bf",
            "adcode": 431024,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6b66\u53bf",
            "adcode": 431025,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5d\u57ce\u53bf",
            "adcode": 431026,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u6842\u4e1c\u53bf",
            "adcode": 431027,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u4ec1\u53bf",
            "adcode": 431028,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u5174\u5e02",
            "adcode": 431081,
            "citycode": 735
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5dde\u5e02",
            "adcode": 431100,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 431101,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u96f6\u9675\u533a",
            "adcode": 431102,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u51b7\u6c34\u6ee9\u533a",
            "adcode": 431103,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u7941\u9633\u53bf",
            "adcode": 431121,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5b89\u53bf",
            "adcode": 431122,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u724c\u53bf",
            "adcode": 431123,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u9053\u53bf",
            "adcode": 431124,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6c38\u53bf",
            "adcode": 431125,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u8fdc\u53bf",
            "adcode": 431126,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u84dd\u5c71\u53bf",
            "adcode": 431127,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u7530\u53bf",
            "adcode": 431128,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u534e\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431129,
            "citycode": 746
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u5316\u5e02",
            "adcode": 431200,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u5316\u5e02\u5e02\u8f96\u533a",
            "adcode": 431201,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u57ce\u533a",
            "adcode": 431202,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u65b9\u53bf",
            "adcode": 431221,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u6c85\u9675\u53bf",
            "adcode": 431222,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u8fb0\u6eaa\u53bf",
            "adcode": 431223,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u6e86\u6d66\u53bf",
            "adcode": 431224,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u540c\u53bf",
            "adcode": 431225,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u9633\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431226,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6643\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431227,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u82b7\u6c5f\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431228,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u5dde\u82d7\u65cf\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431229,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u9053\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 431230,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u6c5f\u5e02",
            "adcode": 431281,
            "citycode": 745
        },
        {
            "\u4e2d\u6587\u540d": "\u5a04\u5e95\u5e02",
            "adcode": 431300,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u5a04\u5e95\u5e02\u5e02\u8f96\u533a",
            "adcode": 431301,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u5a04\u661f\u533a",
            "adcode": 431302,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u5cf0\u53bf",
            "adcode": 431321,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5316\u53bf",
            "adcode": 431322,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u51b7\u6c34\u6c5f\u5e02",
            "adcode": 431381,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u6d9f\u6e90\u5e02",
            "adcode": 431382,
            "citycode": 738
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u897f\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 433100,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u9996\u5e02",
            "adcode": 433101,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u6eaa\u53bf",
            "adcode": 433122,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u51f0\u53bf",
            "adcode": 433123,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u57a3\u53bf",
            "adcode": 433124,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u9756\u53bf",
            "adcode": 433125,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u4e08\u53bf",
            "adcode": 433126,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u987a\u53bf",
            "adcode": 433127,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5c71\u53bf",
            "adcode": 433130,
            "citycode": 743
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5dde\u5e02",
            "adcode": 440100,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 440101,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u8354\u6e7e\u533a",
            "adcode": 440103,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u8d8a\u79c0\u533a",
            "adcode": 440104,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u73e0\u533a",
            "adcode": 440105,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6cb3\u533a",
            "adcode": 440106,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u4e91\u533a",
            "adcode": 440111,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u57d4\u533a",
            "adcode": 440112,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u756a\u79ba\u533a",
            "adcode": 440113,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u90fd\u533a",
            "adcode": 440114,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6c99\u533a",
            "adcode": 440115,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u4ece\u5316\u533a",
            "adcode": 440117,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u589e\u57ce\u533a",
            "adcode": 440118,
            "citycode": 20
        },
        {
            "\u4e2d\u6587\u540d": "\u97f6\u5173\u5e02",
            "adcode": 440200,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u97f6\u5173\u5e02\u5e02\u8f96\u533a",
            "adcode": 440201,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u6c5f\u533a",
            "adcode": 440203,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u6d48\u6c5f\u533a",
            "adcode": 440204,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u6c5f\u533a",
            "adcode": 440205,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u59cb\u5174\u53bf",
            "adcode": 440222,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec1\u5316\u53bf",
            "adcode": 440224,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u7fc1\u6e90\u53bf",
            "adcode": 440229,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u4e73\u6e90\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 440232,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4e30\u53bf",
            "adcode": 440233,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u660c\u5e02",
            "adcode": 440281,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u96c4\u5e02",
            "adcode": 440282,
            "citycode": 751
        },
        {
            "\u4e2d\u6587\u540d": "\u6df1\u5733\u5e02",
            "adcode": 440300,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u6df1\u5733\u5e02\u5e02\u8f96\u533a",
            "adcode": 440301,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u6e56\u533a",
            "adcode": 440303,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u7530\u533a",
            "adcode": 440304,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5c71\u533a",
            "adcode": 440305,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5b89\u533a",
            "adcode": 440306,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5c97\u533a",
            "adcode": 440307,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u7530\u533a",
            "adcode": 440308,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u534e\u533a",
            "adcode": 440309,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u576a\u5c71\u533a",
            "adcode": 440310,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u5149\u660e\u533a",
            "adcode": 440311,
            "citycode": 755
        },
        {
            "\u4e2d\u6587\u540d": "\u73e0\u6d77\u5e02",
            "adcode": 440400,
            "citycode": 756
        },
        {
            "\u4e2d\u6587\u540d": "\u73e0\u6d77\u5e02\u5e02\u8f96\u533a",
            "adcode": 440401,
            "citycode": 756
        },
        {
            "\u4e2d\u6587\u540d": "\u9999\u6d32\u533a",
            "adcode": 440402,
            "citycode": 756
        },
        {
            "\u4e2d\u6587\u540d": "\u6597\u95e8\u533a",
            "adcode": 440403,
            "citycode": 756
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6e7e\u533a",
            "adcode": 440404,
            "citycode": 756
        },
        {
            "\u4e2d\u6587\u540d": "\u6c55\u5934\u5e02",
            "adcode": 440500,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u6c55\u5934\u5e02\u5e02\u8f96\u533a",
            "adcode": 440501,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6e56\u533a",
            "adcode": 440507,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5e73\u533a",
            "adcode": 440511,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u6fe0\u6c5f\u533a",
            "adcode": 440512,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u6f6e\u9633\u533a",
            "adcode": 440513,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u6f6e\u5357\u533a",
            "adcode": 440514,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u6f84\u6d77\u533a",
            "adcode": 440515,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6fb3\u53bf",
            "adcode": 440523,
            "citycode": 754
        },
        {
            "\u4e2d\u6587\u540d": "\u4f5b\u5c71\u5e02",
            "adcode": 440600,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u4f5b\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 440601,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u7985\u57ce\u533a",
            "adcode": 440604,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6d77\u533a",
            "adcode": 440605,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u5fb7\u533a",
            "adcode": 440606,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u6c34\u533a",
            "adcode": 440607,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u660e\u533a",
            "adcode": 440608,
            "citycode": 757
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u95e8\u5e02",
            "adcode": 440700,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u95e8\u5e02\u5e02\u8f96\u533a",
            "adcode": 440701,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u84ec\u6c5f\u533a",
            "adcode": 440703,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6d77\u533a",
            "adcode": 440704,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u4f1a\u533a",
            "adcode": 440705,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u5c71\u5e02",
            "adcode": 440781,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5e73\u5e02",
            "adcode": 440783,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5c71\u5e02",
            "adcode": 440784,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u6069\u5e73\u5e02",
            "adcode": 440785,
            "citycode": 750
        },
        {
            "\u4e2d\u6587\u540d": "\u6e5b\u6c5f\u5e02",
            "adcode": 440800,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u6e5b\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 440801,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u574e\u533a",
            "adcode": 440802,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u971e\u5c71\u533a",
            "adcode": 440803,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u5761\u5934\u533a",
            "adcode": 440804,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u7ae0\u533a",
            "adcode": 440811,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u6eaa\u53bf",
            "adcode": 440823,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u5f90\u95fb\u53bf",
            "adcode": 440825,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u5ec9\u6c5f\u5e02",
            "adcode": 440881,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u96f7\u5dde\u5e02",
            "adcode": 440882,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u5ddd\u5e02",
            "adcode": 440883,
            "citycode": 759
        },
        {
            "\u4e2d\u6587\u540d": "\u8302\u540d\u5e02",
            "adcode": 440900,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u8302\u540d\u5e02\u5e02\u8f96\u533a",
            "adcode": 440901,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u8302\u5357\u533a",
            "adcode": 440902,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u7535\u767d\u533a",
            "adcode": 440904,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u5dde\u5e02",
            "adcode": 440981,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u5316\u5dde\u5e02",
            "adcode": 440982,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u4fe1\u5b9c\u5e02",
            "adcode": 440983,
            "citycode": 668
        },
        {
            "\u4e2d\u6587\u540d": "\u8087\u5e86\u5e02",
            "adcode": 441200,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u8087\u5e86\u5e02\u5e02\u8f96\u533a",
            "adcode": 441201,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u7aef\u5dde\u533a",
            "adcode": 441202,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u9f0e\u6e56\u533a",
            "adcode": 441203,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u8981\u533a",
            "adcode": 441204,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5b81\u53bf",
            "adcode": 441223,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u6000\u96c6\u53bf",
            "adcode": 441224,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u5c01\u5f00\u53bf",
            "adcode": 441225,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5e86\u53bf",
            "adcode": 441226,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u56db\u4f1a\u5e02",
            "adcode": 441284,
            "citycode": 758
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u5dde\u5e02",
            "adcode": 441300,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 441301,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u57ce\u533a",
            "adcode": 441302,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u9633\u533a",
            "adcode": 441303,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u7f57\u53bf",
            "adcode": 441322,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u4e1c\u53bf",
            "adcode": 441323,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u95e8\u53bf",
            "adcode": 441324,
            "citycode": 752
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u5dde\u5e02",
            "adcode": 441400,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 441401,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u6c5f\u533a",
            "adcode": 441402,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u6885\u53bf\u533a",
            "adcode": 441403,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u57d4\u53bf",
            "adcode": 441422,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u987a\u53bf",
            "adcode": 441423,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u534e\u53bf",
            "adcode": 441424,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u8fdc\u53bf",
            "adcode": 441426,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u8549\u5cad\u53bf",
            "adcode": 441427,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5b81\u5e02",
            "adcode": 441481,
            "citycode": 753
        },
        {
            "\u4e2d\u6587\u540d": "\u6c55\u5c3e\u5e02",
            "adcode": 441500,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u6c55\u5c3e\u5e02\u5e02\u8f96\u533a",
            "adcode": 441501,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u533a",
            "adcode": 441502,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u4e30\u53bf",
            "adcode": 441521,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u9646\u6cb3\u53bf",
            "adcode": 441523,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u9646\u4e30\u5e02",
            "adcode": 441581,
            "citycode": 660
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u6e90\u5e02",
            "adcode": 441600,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u6e90\u5e02\u5e02\u8f96\u533a",
            "adcode": 441601,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u6e90\u57ce\u533a",
            "adcode": 441602,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u7d2b\u91d1\u53bf",
            "adcode": 441621,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5ddd\u53bf",
            "adcode": 441622,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u5e73\u53bf",
            "adcode": 441623,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u5e73\u53bf",
            "adcode": 441624,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u6e90\u53bf",
            "adcode": 441625,
            "citycode": 762
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6c5f\u5e02",
            "adcode": 441700,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 441701,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u57ce\u533a",
            "adcode": 441702,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u4e1c\u533a",
            "adcode": 441704,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u897f\u53bf",
            "adcode": 441721,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6625\u5e02",
            "adcode": 441781,
            "citycode": 662
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u8fdc\u5e02",
            "adcode": 441800,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u8fdc\u5e02\u5e02\u8f96\u533a",
            "adcode": 441801,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u57ce\u533a",
            "adcode": 441802,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u65b0\u533a",
            "adcode": 441803,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u4f5b\u5188\u53bf",
            "adcode": 441821,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u5c71\u53bf",
            "adcode": 441823,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u5c71\u58ee\u65cf\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 441825,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u5357\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 441826,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u82f1\u5fb7\u5e02",
            "adcode": 441881,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u8fde\u5dde\u5e02",
            "adcode": 441882,
            "citycode": 763
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u839e\u5e02",
            "adcode": 441900,
            "citycode": 769
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u5c71\u5e02",
            "adcode": 442000,
            "citycode": 760
        },
        {
            "\u4e2d\u6587\u540d": "\u6f6e\u5dde\u5e02",
            "adcode": 445100,
            "citycode": 768
        },
        {
            "\u4e2d\u6587\u540d": "\u6f6e\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 445101,
            "citycode": 768
        },
        {
            "\u4e2d\u6587\u540d": "\u6e58\u6865\u533a",
            "adcode": 445102,
            "citycode": 768
        },
        {
            "\u4e2d\u6587\u540d": "\u6f6e\u5b89\u533a",
            "adcode": 445103,
            "citycode": 768
        },
        {
            "\u4e2d\u6587\u540d": "\u9976\u5e73\u53bf",
            "adcode": 445122,
            "citycode": 768
        },
        {
            "\u4e2d\u6587\u540d": "\u63ed\u9633\u5e02",
            "adcode": 445200,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u63ed\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 445201,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u6995\u57ce\u533a",
            "adcode": 445202,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u63ed\u4e1c\u533a",
            "adcode": 445203,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u63ed\u897f\u53bf",
            "adcode": 445222,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u6765\u53bf",
            "adcode": 445224,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u5b81\u5e02",
            "adcode": 445281,
            "citycode": 663
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u6d6e\u5e02",
            "adcode": 445300,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u6d6e\u5e02\u5e02\u8f96\u533a",
            "adcode": 445301,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u57ce\u533a",
            "adcode": 445302,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u5b89\u533a",
            "adcode": 445303,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5174\u53bf",
            "adcode": 445321,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u90c1\u5357\u53bf",
            "adcode": 445322,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u5b9a\u5e02",
            "adcode": 445381,
            "citycode": 766
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5b81\u5e02",
            "adcode": 450100,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5b81\u5e02\u5e02\u8f96\u533a",
            "adcode": 450101,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5b81\u533a",
            "adcode": 450102,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u79c0\u533a",
            "adcode": 450103,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5357\u533a",
            "adcode": 450105,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u4e61\u5858\u533a",
            "adcode": 450107,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u826f\u5e86\u533a",
            "adcode": 450108,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u9095\u5b81\u533a",
            "adcode": 450109,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u9e23\u533a",
            "adcode": 450110,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u5b89\u53bf",
            "adcode": 450123,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u5c71\u53bf",
            "adcode": 450124,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u6797\u53bf",
            "adcode": 450125,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbe\u9633\u53bf",
            "adcode": 450126,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u6a2a\u53bf",
            "adcode": 450127,
            "citycode": 771
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u5dde\u5e02",
            "adcode": 450200,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 450201,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u4e2d\u533a",
            "adcode": 450202,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u9c7c\u5cf0\u533a",
            "adcode": 450203,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u5357\u533a",
            "adcode": 450204,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u5317\u533a",
            "adcode": 450205,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u6c5f\u533a",
            "adcode": 450206,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u67f3\u57ce\u53bf",
            "adcode": 450222,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u9e7f\u5be8\u53bf",
            "adcode": 450223,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u878d\u5b89\u53bf",
            "adcode": 450224,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u878d\u6c34\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 450225,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u6c5f\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 450226,
            "citycode": 772
        },
        {
            "\u4e2d\u6587\u540d": "\u6842\u6797\u5e02",
            "adcode": 450300,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u6842\u6797\u5e02\u5e02\u8f96\u533a",
            "adcode": 450301,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u79c0\u5cf0\u533a",
            "adcode": 450302,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u53e0\u5f69\u533a",
            "adcode": 450303,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u8c61\u5c71\u533a",
            "adcode": 450304,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u4e03\u661f\u533a",
            "adcode": 450305,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u96c1\u5c71\u533a",
            "adcode": 450311,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6842\u533a",
            "adcode": 450312,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u9633\u6714\u53bf",
            "adcode": 450321,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u5ddd\u53bf",
            "adcode": 450323,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u5168\u5dde\u53bf",
            "adcode": 450324,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5b89\u53bf",
            "adcode": 450325,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u798f\u53bf",
            "adcode": 450326,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u704c\u9633\u53bf",
            "adcode": 450327,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u80dc\u5404\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 450328,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u6e90\u53bf",
            "adcode": 450329,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u4e50\u53bf",
            "adcode": 450330,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u8354\u6d66\u5e02",
            "adcode": 450381,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u606d\u57ce\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 450332,
            "citycode": 773
        },
        {
            "\u4e2d\u6587\u540d": "\u68a7\u5dde\u5e02",
            "adcode": 450400,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u68a7\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 450401,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u79c0\u533a",
            "adcode": 450403,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6d32\u533a",
            "adcode": 450405,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5729\u533a",
            "adcode": 450406,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u82cd\u68a7\u53bf",
            "adcode": 450421,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u85e4\u53bf",
            "adcode": 450422,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u8499\u5c71\u53bf",
            "adcode": 450423,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u5c91\u6eaa\u5e02",
            "adcode": 450481,
            "citycode": 774
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6d77\u5e02",
            "adcode": 450500,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6d77\u5e02\u5e02\u8f96\u533a",
            "adcode": 450501,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u57ce\u533a",
            "adcode": 450502,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u94f6\u6d77\u533a",
            "adcode": 450503,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u5c71\u6e2f\u533a",
            "adcode": 450512,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u6d66\u53bf",
            "adcode": 450521,
            "citycode": 779
        },
        {
            "\u4e2d\u6587\u540d": "\u9632\u57ce\u6e2f\u5e02",
            "adcode": 450600,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u9632\u57ce\u6e2f\u5e02\u5e02\u8f96\u533a",
            "adcode": 450601,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2f\u53e3\u533a",
            "adcode": 450602,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u9632\u57ce\u533a",
            "adcode": 450603,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u4e0a\u601d\u53bf",
            "adcode": 450621,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5174\u5e02",
            "adcode": 450681,
            "citycode": 770
        },
        {
            "\u4e2d\u6587\u540d": "\u94a6\u5dde\u5e02",
            "adcode": 450700,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u94a6\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 450701,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u94a6\u5357\u533a",
            "adcode": 450702,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u94a6\u5317\u533a",
            "adcode": 450703,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u5c71\u53bf",
            "adcode": 450721,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u6d66\u5317\u53bf",
            "adcode": 450722,
            "citycode": 777
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u6e2f\u5e02",
            "adcode": 450800,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u6e2f\u5e02\u5e02\u8f96\u533a",
            "adcode": 450801,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2f\u5317\u533a",
            "adcode": 450802,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2f\u5357\u533a",
            "adcode": 450803,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u8983\u5858\u533a",
            "adcode": 450804,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5357\u53bf",
            "adcode": 450821,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u6842\u5e73\u5e02",
            "adcode": 450881,
            "citycode": 1755
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6797\u5e02",
            "adcode": 450900,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6797\u5e02\u5e02\u8f96\u533a",
            "adcode": 450901,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u5dde\u533a",
            "adcode": 450902,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u7ef5\u533a",
            "adcode": 450903,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u5bb9\u53bf",
            "adcode": 450921,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u9646\u5ddd\u53bf",
            "adcode": 450922,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u767d\u53bf",
            "adcode": 450923,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u4e1a\u53bf",
            "adcode": 450924,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u6d41\u5e02",
            "adcode": 450981,
            "citycode": 775
        },
        {
            "\u4e2d\u6587\u540d": "\u767e\u8272\u5e02",
            "adcode": 451000,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u767e\u8272\u5e02\u5e02\u8f96\u533a",
            "adcode": 451001,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u53f3\u6c5f\u533a",
            "adcode": 451002,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u7530\u9633\u533a",
            "adcode": 451003,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u7530\u4e1c\u53bf",
            "adcode": 451022,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u679c\u5e02",
            "adcode": 451082,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u4fdd\u53bf",
            "adcode": 451024,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u90a3\u5761\u53bf",
            "adcode": 451026,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u51cc\u4e91\u53bf",
            "adcode": 451027,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u4e1a\u53bf",
            "adcode": 451028,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u7530\u6797\u53bf",
            "adcode": 451029,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u6797\u53bf",
            "adcode": 451030,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u6797\u5404\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451031,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u897f\u5e02",
            "adcode": 451081,
            "citycode": 776
        },
        {
            "\u4e2d\u6587\u540d": "\u8d3a\u5dde\u5e02",
            "adcode": 451100,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u8d3a\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 451101,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u516b\u6b65\u533a",
            "adcode": 451102,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6842\u533a",
            "adcode": 451103,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u5e73\u53bf",
            "adcode": 451121,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u949f\u5c71\u53bf",
            "adcode": 451122,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u5ddd\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451123,
            "citycode": 1774
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u6c60\u5e02",
            "adcode": 451200,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u6c60\u5e02\u5e02\u8f96\u533a",
            "adcode": 451201,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u57ce\u6c5f\u533a",
            "adcode": 451202,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u5dde\u533a",
            "adcode": 451203,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u4e39\u53bf",
            "adcode": 451221,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5ce8\u53bf",
            "adcode": 451222,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u5c71\u53bf",
            "adcode": 451223,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5170\u53bf",
            "adcode": 451224,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u57ce\u4eeb\u4f6c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451225,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u73af\u6c5f\u6bdb\u5357\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451226,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u9a6c\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451227,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u90fd\u5b89\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451228,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5316\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451229,
            "citycode": 778
        },
        {
            "\u4e2d\u6587\u540d": "\u6765\u5bbe\u5e02",
            "adcode": 451300,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u6765\u5bbe\u5e02\u5e02\u8f96\u533a",
            "adcode": 451301,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5bbe\u533a",
            "adcode": 451302,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u5ffb\u57ce\u53bf",
            "adcode": 451321,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u8c61\u5dde\u53bf",
            "adcode": 451322,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5ba3\u53bf",
            "adcode": 451323,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u79c0\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 451324,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u5c71\u5e02",
            "adcode": 451381,
            "citycode": 1772
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u5de6\u5e02",
            "adcode": 451400,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u5de6\u5e02\u5e02\u8f96\u533a",
            "adcode": 451401,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5dde\u533a",
            "adcode": 451402,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u6276\u7ee5\u53bf",
            "adcode": 451421,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u660e\u53bf",
            "adcode": 451422,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u5dde\u53bf",
            "adcode": 451423,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u65b0\u53bf",
            "adcode": 451424,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u7b49\u53bf",
            "adcode": 451425,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u51ed\u7965\u5e02",
            "adcode": 451481,
            "citycode": 1771
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u53e3\u5e02",
            "adcode": 460100,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u53e3\u5e02\u5e02\u8f96\u533a",
            "adcode": 460101,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u79c0\u82f1\u533a",
            "adcode": 460105,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u534e\u533a",
            "adcode": 460106,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u743c\u5c71\u533a",
            "adcode": 460107,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u7f8e\u5170\u533a",
            "adcode": 460108,
            "citycode": 898
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u4e9a\u5e02",
            "adcode": 460200,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u4e9a\u5e02\u5e02\u8f96\u533a",
            "adcode": 460201,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u68e0\u533a",
            "adcode": 460202,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u9633\u533a",
            "adcode": 460203,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6daf\u533a",
            "adcode": 460204,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u5d16\u5dde\u533a",
            "adcode": 460205,
            "citycode": 899
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u6c99\u5e02",
            "adcode": 460300,
            "citycode": 2898
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u6c99\u5e02\u5e02\u8f96\u533a",
            "adcode": 460301,
            "citycode": 2898
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u6c99\u7fa4\u5c9b",
            "adcode": 460321,
            "citycode": 1895
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6c99\u7fa4\u5c9b",
            "adcode": 460322,
            "citycode": 1891
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u6c99\u7fa4\u5c9b\u7684\u5c9b\u7901\u53ca\u5176\u6d77\u57df",
            "adcode": 460323,
            "citycode": 2801
        },
        {
            "\u4e2d\u6587\u540d": "\u510b\u5dde\u5e02",
            "adcode": 460400,
            "citycode": 805
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u6307\u5c71\u5e02",
            "adcode": 469001,
            "citycode": 1897
        },
        {
            "\u4e2d\u6587\u540d": "\u743c\u6d77\u5e02",
            "adcode": 469002,
            "citycode": 1894
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u660c\u5e02",
            "adcode": 469005,
            "citycode": 1893
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5b81\u5e02",
            "adcode": 469006,
            "citycode": 1898
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u65b9\u5e02",
            "adcode": 469007,
            "citycode": 807
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u5b89\u53bf",
            "adcode": 469021,
            "citycode": 806
        },
        {
            "\u4e2d\u6587\u540d": "\u5c6f\u660c\u53bf",
            "adcode": 469022,
            "citycode": 1892
        },
        {
            "\u4e2d\u6587\u540d": "\u6f84\u8fc8\u53bf",
            "adcode": 469023,
            "citycode": 804
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u9ad8\u53bf",
            "adcode": 469024,
            "citycode": 1896
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u6c99\u9ece\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469025,
            "citycode": 802
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u6c5f\u9ece\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469026,
            "citycode": 803
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u4e1c\u9ece\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469027,
            "citycode": 2802
        },
        {
            "\u4e2d\u6587\u540d": "\u9675\u6c34\u9ece\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469028,
            "citycode": 809
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u4ead\u9ece\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469029,
            "citycode": 801
        },
        {
            "\u4e2d\u6587\u540d": "\u743c\u4e2d\u9ece\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 469030,
            "citycode": 1899
        },
        {
            "\u4e2d\u6587\u540d": "\u91cd\u5e86\u5e02",
            "adcode": 500000,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u91cd\u5e86\u5e02\u5e02\u8f96\u533a",
            "adcode": 500100,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5dde\u533a",
            "adcode": 500101,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6daa\u9675\u533a",
            "adcode": 500102,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6e1d\u4e2d\u533a",
            "adcode": 500103,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u6e21\u53e3\u533a",
            "adcode": 500104,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5317\u533a",
            "adcode": 500105,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u576a\u575d\u533a",
            "adcode": 500106,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u9f99\u5761\u533a",
            "adcode": 500107,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5cb8\u533a",
            "adcode": 500108,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u789a\u533a",
            "adcode": 500109,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u7da6\u6c5f\u533a",
            "adcode": 500110,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u8db3\u533a",
            "adcode": 500111,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6e1d\u5317\u533a",
            "adcode": 500112,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5357\u533a",
            "adcode": 500113,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed4\u6c5f\u533a",
            "adcode": 500114,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5bff\u533a",
            "adcode": 500115,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6d25\u533a",
            "adcode": 500116,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u5ddd\u533a",
            "adcode": 500117,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5ddd\u533a",
            "adcode": 500118,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5ddd\u533a",
            "adcode": 500119,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u74a7\u5c71\u533a",
            "adcode": 500120,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u6881\u533a",
            "adcode": 500151,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6f7c\u5357\u533a",
            "adcode": 500152,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u8363\u660c\u533a",
            "adcode": 500153,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u5dde\u533a",
            "adcode": 500154,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u5e73\u533a",
            "adcode": 500155,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u9686\u533a",
            "adcode": 500156,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u91cd\u5e86\u5e02\u90ca\u53bf",
            "adcode": 500200,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u53e3\u53bf",
            "adcode": 500229,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u4e30\u90fd\u53bf",
            "adcode": 500230,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u57ab\u6c5f\u53bf",
            "adcode": 500231,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5fe0\u53bf",
            "adcode": 500233,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u9633\u53bf",
            "adcode": 500235,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5949\u8282\u53bf",
            "adcode": 500236,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5deb\u5c71\u53bf",
            "adcode": 500237,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5deb\u6eaa\u53bf",
            "adcode": 500238,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u67f1\u571f\u5bb6\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 500240,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u79c0\u5c71\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 500241,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u9149\u9633\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 500242,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6d\u6c34\u82d7\u65cf\u571f\u5bb6\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 500243,
            "citycode": 23
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u90fd\u5e02",
            "adcode": 510100,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u90fd\u5e02\u5e02\u8f96\u533a",
            "adcode": 510101,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u9526\u6c5f\u533a",
            "adcode": 510104,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u7f8a\u533a",
            "adcode": 510105,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u725b\u533a",
            "adcode": 510106,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u4faf\u533a",
            "adcode": 510107,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u534e\u533a",
            "adcode": 510108,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u6cc9\u9a7f\u533a",
            "adcode": 510112,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u767d\u6c5f\u533a",
            "adcode": 510113,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u90fd\u533a",
            "adcode": 510114,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u6c5f\u533a",
            "adcode": 510115,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6d41\u533a",
            "adcode": 510116,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u90eb\u90fd\u533a",
            "adcode": 510117,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5802\u53bf",
            "adcode": 510121,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u9091\u53bf",
            "adcode": 510129,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u84b2\u6c5f\u53bf",
            "adcode": 510131,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6d25\u53bf",
            "adcode": 510132,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u90fd\u6c5f\u5830\u5e02",
            "adcode": 510181,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6d\u5dde\u5e02",
            "adcode": 510182,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u909b\u5d03\u5e02",
            "adcode": 510183,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u5dde\u5e02",
            "adcode": 510184,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u7b80\u9633\u5e02",
            "adcode": 510185,
            "citycode": 28
        },
        {
            "\u4e2d\u6587\u540d": "\u81ea\u8d21\u5e02",
            "adcode": 510300,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u81ea\u8d21\u5e02\u5e02\u8f96\u533a",
            "adcode": 510301,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u81ea\u6d41\u4e95\u533a",
            "adcode": 510302,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u8d21\u4e95\u533a",
            "adcode": 510303,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5b89\u533a",
            "adcode": 510304,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbf\u6ee9\u533a",
            "adcode": 510311,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u8363\u53bf",
            "adcode": 510321,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u987a\u53bf",
            "adcode": 510322,
            "citycode": 813
        },
        {
            "\u4e2d\u6587\u540d": "\u6500\u679d\u82b1\u5e02",
            "adcode": 510400,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u6500\u679d\u82b1\u5e02\u5e02\u8f96\u533a",
            "adcode": 510401,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u533a",
            "adcode": 510402,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u533a",
            "adcode": 510403,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec1\u548c\u533a",
            "adcode": 510411,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u7c73\u6613\u53bf",
            "adcode": 510421,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u8fb9\u53bf",
            "adcode": 510422,
            "citycode": 812
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u5dde\u5e02",
            "adcode": 510500,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 510501,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u9633\u533a",
            "adcode": 510502,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u7eb3\u6eaa\u533a",
            "adcode": 510503,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u9a6c\u6f6d\u533a",
            "adcode": 510504,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u53bf",
            "adcode": 510521,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u6c5f\u53bf",
            "adcode": 510522,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u53d9\u6c38\u53bf",
            "adcode": 510524,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u853a\u53bf",
            "adcode": 510525,
            "citycode": 830
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u9633\u5e02",
            "adcode": 510600,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 510601,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u65cc\u9633\u533a",
            "adcode": 510603,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u6c5f\u53bf",
            "adcode": 510623,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u6c5f\u533a",
            "adcode": 510604,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u6c49\u5e02",
            "adcode": 510681,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec0\u90a1\u5e02",
            "adcode": 510682,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u7ef5\u7af9\u5e02",
            "adcode": 510683,
            "citycode": 838
        },
        {
            "\u4e2d\u6587\u540d": "\u7ef5\u9633\u5e02",
            "adcode": 510700,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u7ef5\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 510701,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u6daa\u57ce\u533a",
            "adcode": 510703,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u6e38\u4ed9\u533a",
            "adcode": 510704,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5dde\u533a",
            "adcode": 510705,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u53f0\u53bf",
            "adcode": 510722,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u4ead\u53bf",
            "adcode": 510723,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u6893\u6f7c\u53bf",
            "adcode": 510725,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u5ddd\u7f8c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 510726,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u6b66\u53bf",
            "adcode": 510727,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u6cb9\u5e02",
            "adcode": 510781,
            "citycode": 816
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5143\u5e02",
            "adcode": 510800,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5143\u5e02\u5e02\u8f96\u533a",
            "adcode": 510801,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u5229\u5dde\u533a",
            "adcode": 510802,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u5316\u533a",
            "adcode": 510811,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u671d\u5929\u533a",
            "adcode": 510812,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u65fa\u82cd\u53bf",
            "adcode": 510821,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u5ddd\u53bf",
            "adcode": 510822,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u5251\u9601\u53bf",
            "adcode": 510823,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u82cd\u6eaa\u53bf",
            "adcode": 510824,
            "citycode": 839
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u5b81\u5e02",
            "adcode": 510900,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u9042\u5b81\u5e02\u5e02\u8f96\u533a",
            "adcode": 510901,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u8239\u5c71\u533a",
            "adcode": 510903,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5c45\u533a",
            "adcode": 510904,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u84ec\u6eaa\u53bf",
            "adcode": 510921,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u5c04\u6d2a\u5e02",
            "adcode": 510981,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u82f1\u53bf",
            "adcode": 510923,
            "citycode": 825
        },
        {
            "\u4e2d\u6587\u540d": "\u5185\u6c5f\u5e02",
            "adcode": 511000,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u5185\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 511001,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u4e2d\u533a",
            "adcode": 511002,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5174\u533a",
            "adcode": 511011,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u8fdc\u53bf",
            "adcode": 511024,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u4e2d\u53bf",
            "adcode": 511025,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u660c\u5e02",
            "adcode": 511083,
            "citycode": 1832
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u5c71\u5e02",
            "adcode": 511100,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 511101,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u5e02\u4e2d\u533a",
            "adcode": 511102,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u6e7e\u533a",
            "adcode": 511111,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u901a\u6865\u533a",
            "adcode": 511112,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u53e3\u6cb3\u533a",
            "adcode": 511113,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u728d\u4e3a\u53bf",
            "adcode": 511123,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u4e95\u7814\u53bf",
            "adcode": 511124,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u5939\u6c5f\u53bf",
            "adcode": 511126,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u6c90\u5ddd\u53bf",
            "adcode": 511129,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u5ce8\u8fb9\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 511132,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u8fb9\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 511133,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u5ce8\u7709\u5c71\u5e02",
            "adcode": 511181,
            "citycode": 833
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5145\u5e02",
            "adcode": 511300,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u5145\u5e02\u5e02\u8f96\u533a",
            "adcode": 511301,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u987a\u5e86\u533a",
            "adcode": 511302,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u576a\u533a",
            "adcode": 511303,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u9675\u533a",
            "adcode": 511304,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u90e8\u53bf",
            "adcode": 511321,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u8425\u5c71\u53bf",
            "adcode": 511322,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u84ec\u5b89\u53bf",
            "adcode": 511323,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u4eea\u9647\u53bf",
            "adcode": 511324,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5145\u53bf",
            "adcode": 511325,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u9606\u4e2d\u5e02",
            "adcode": 511381,
            "citycode": 817
        },
        {
            "\u4e2d\u6587\u540d": "\u7709\u5c71\u5e02",
            "adcode": 511400,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u7709\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 511401,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5761\u533a",
            "adcode": 511402,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6d\u5c71\u533a",
            "adcode": 511403,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec1\u5bff\u53bf",
            "adcode": 511421,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u6d2a\u96c5\u53bf",
            "adcode": 511423,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u68f1\u53bf",
            "adcode": 511424,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u795e\u53bf",
            "adcode": 511425,
            "citycode": 1833
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u5bbe\u5e02",
            "adcode": 511500,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u5bbe\u5e02\u5e02\u8f96\u533a",
            "adcode": 511501,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u7fe0\u5c4f\u533a",
            "adcode": 511502,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6eaa\u533a",
            "adcode": 511503,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u53d9\u5dde\u533a",
            "adcode": 511504,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5b89\u53bf",
            "adcode": 511523,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5b81\u53bf",
            "adcode": 511524,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u53bf",
            "adcode": 511525,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u73d9\u53bf",
            "adcode": 511526,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u7b60\u8fde\u53bf",
            "adcode": 511527,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u6587\u53bf",
            "adcode": 511528,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u5c4f\u5c71\u53bf",
            "adcode": 511529,
            "citycode": 831
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5b89\u5e02",
            "adcode": 511600,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 511601,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5b89\u533a",
            "adcode": 511602,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u524d\u950b\u533a",
            "adcode": 511603,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u6c60\u53bf",
            "adcode": 511621,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u80dc\u53bf",
            "adcode": 511622,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u90bb\u6c34\u53bf",
            "adcode": 511623,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u84e5\u5e02",
            "adcode": 511681,
            "citycode": 826
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5dde\u5e02",
            "adcode": 511700,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 511701,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u5ddd\u533a",
            "adcode": 511702,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5ddd\u533a",
            "adcode": 511703,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u6c49\u53bf",
            "adcode": 511722,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u6c5f\u53bf",
            "adcode": 511723,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7af9\u53bf",
            "adcode": 511724,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u6e20\u53bf",
            "adcode": 511725,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u6e90\u5e02",
            "adcode": 511781,
            "citycode": 818
        },
        {
            "\u4e2d\u6587\u540d": "\u96c5\u5b89\u5e02",
            "adcode": 511800,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u96c5\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 511801,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u96e8\u57ce\u533a",
            "adcode": 511802,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u540d\u5c71\u533a",
            "adcode": 511803,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u8365\u7ecf\u53bf",
            "adcode": 511822,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u6e90\u53bf",
            "adcode": 511823,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u68c9\u53bf",
            "adcode": 511824,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5168\u53bf",
            "adcode": 511825,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u82a6\u5c71\u53bf",
            "adcode": 511826,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5174\u53bf",
            "adcode": 511827,
            "citycode": 835
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u4e2d\u5e02",
            "adcode": 511900,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u4e2d\u5e02\u5e02\u8f96\u533a",
            "adcode": 511901,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5dde\u533a",
            "adcode": 511902,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u6069\u9633\u533a",
            "adcode": 511903,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u6c5f\u53bf",
            "adcode": 511921,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6c5f\u53bf",
            "adcode": 511922,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u660c\u53bf",
            "adcode": 511923,
            "citycode": 827
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u9633\u5e02",
            "adcode": 512000,
            "citycode": 832
        },
        {
            "\u4e2d\u6587\u540d": "\u8d44\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 512001,
            "citycode": 832
        },
        {
            "\u4e2d\u6587\u540d": "\u96c1\u6c5f\u533a",
            "adcode": 512002,
            "citycode": 832
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5cb3\u53bf",
            "adcode": 512021,
            "citycode": 832
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u81f3\u53bf",
            "adcode": 512022,
            "citycode": 832
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u575d\u85cf\u65cf\u7f8c\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 513200,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u5c14\u5eb7\u5e02",
            "adcode": 513201,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u6c76\u5ddd\u53bf",
            "adcode": 513221,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u7406\u53bf",
            "adcode": 513222,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u8302\u53bf",
            "adcode": 513223,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u6f58\u53bf",
            "adcode": 513224,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u5be8\u6c9f\u53bf",
            "adcode": 513225,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5ddd\u53bf",
            "adcode": 513226,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u5c0f\u91d1\u53bf",
            "adcode": 513227,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed1\u6c34\u53bf",
            "adcode": 513228,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u58e4\u5858\u53bf",
            "adcode": 513230,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u575d\u53bf",
            "adcode": 513231,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u82e5\u5c14\u76d6\u53bf",
            "adcode": 513232,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u539f\u53bf",
            "adcode": 513233,
            "citycode": 837
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5b5c\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 513300,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u5b9a\u5e02",
            "adcode": 513301,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u5b9a\u53bf",
            "adcode": 513322,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u5df4\u53bf",
            "adcode": 513323,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u9f99\u53bf",
            "adcode": 513324,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u96c5\u6c5f\u53bf",
            "adcode": 513325,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u9053\u5b5a\u53bf",
            "adcode": 513326,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u7089\u970d\u53bf",
            "adcode": 513327,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5b5c\u53bf",
            "adcode": 513328,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u9f99\u53bf",
            "adcode": 513329,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u683c\u53bf",
            "adcode": 513330,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u7389\u53bf",
            "adcode": 513331,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u6e20\u53bf",
            "adcode": 513332,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u8272\u8fbe\u53bf",
            "adcode": 513333,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u7406\u5858\u53bf",
            "adcode": 513334,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5858\u53bf",
            "adcode": 513335,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u4e61\u57ce\u53bf",
            "adcode": 513336,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u7a3b\u57ce\u53bf",
            "adcode": 513337,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u5f97\u8363\u53bf",
            "adcode": 513338,
            "citycode": 836
        },
        {
            "\u4e2d\u6587\u540d": "\u51c9\u5c71\u5f5d\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 513400,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u660c\u5e02",
            "adcode": 513401,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u6728\u91cc\u85cf\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 513422,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u6e90\u53bf",
            "adcode": 513423,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u660c\u53bf",
            "adcode": 513424,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u7406\u53bf",
            "adcode": 513425,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u4e1c\u53bf",
            "adcode": 513426,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5357\u53bf",
            "adcode": 513427,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u683c\u53bf",
            "adcode": 513428,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u5e03\u62d6\u53bf",
            "adcode": 513429,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u9633\u53bf",
            "adcode": 513430,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u89c9\u53bf",
            "adcode": 513431,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u559c\u5fb7\u53bf",
            "adcode": 513432,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u5195\u5b81\u53bf",
            "adcode": 513433,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u8d8a\u897f\u53bf",
            "adcode": 513434,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u6d1b\u53bf",
            "adcode": 513435,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u7f8e\u59d1\u53bf",
            "adcode": 513436,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u96f7\u6ce2\u53bf",
            "adcode": 513437,
            "citycode": 834
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u9633\u5e02",
            "adcode": 520100,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 520101,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u660e\u533a",
            "adcode": 520102,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u5ca9\u533a",
            "adcode": 520103,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u6eaa\u533a",
            "adcode": 520111,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5f53\u533a",
            "adcode": 520112,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u4e91\u533a",
            "adcode": 520113,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u89c2\u5c71\u6e56\u533a",
            "adcode": 520115,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u9633\u53bf",
            "adcode": 520121,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u606f\u70fd\u53bf",
            "adcode": 520122,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u4fee\u6587\u53bf",
            "adcode": 520123,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u9547\u5e02",
            "adcode": 520181,
            "citycode": 851
        },
        {
            "\u4e2d\u6587\u540d": "\u516d\u76d8\u6c34\u5e02",
            "adcode": 520200,
            "citycode": 858
        },
        {
            "\u4e2d\u6587\u540d": "\u949f\u5c71\u533a",
            "adcode": 520201,
            "citycode": 858
        },
        {
            "\u4e2d\u6587\u540d": "\u516d\u679d\u7279\u533a",
            "adcode": 520203,
            "citycode": 858
        },
        {
            "\u4e2d\u6587\u540d": "\u6c34\u57ce\u53bf",
            "adcode": 520221,
            "citycode": 858
        },
        {
            "\u4e2d\u6587\u540d": "\u76d8\u5dde\u5e02",
            "adcode": 520281,
            "citycode": 858
        },
        {
            "\u4e2d\u6587\u540d": "\u9075\u4e49\u5e02",
            "adcode": 520300,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u9075\u4e49\u5e02\u5e02\u8f96\u533a",
            "adcode": 520301,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u82b1\u5c97\u533a",
            "adcode": 520302,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u6c47\u5ddd\u533a",
            "adcode": 520303,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u64ad\u5dde\u533a",
            "adcode": 520304,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u6850\u6893\u53bf",
            "adcode": 520322,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u9633\u53bf",
            "adcode": 520323,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u5b89\u53bf",
            "adcode": 520324,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u9053\u771f\u4ee1\u4f6c\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520325,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u52a1\u5ddd\u4ee1\u4f6c\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520326,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u5188\u53bf",
            "adcode": 520327,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u6e44\u6f6d\u53bf",
            "adcode": 520328,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u4f59\u5e86\u53bf",
            "adcode": 520329,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u4e60\u6c34\u53bf",
            "adcode": 520330,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u8d64\u6c34\u5e02",
            "adcode": 520381,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec1\u6000\u5e02",
            "adcode": 520382,
            "citycode": 852
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u987a\u5e02",
            "adcode": 520400,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u987a\u5e02\u5e02\u8f96\u533a",
            "adcode": 520401,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u79c0\u533a",
            "adcode": 520402,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u575d\u533a",
            "adcode": 520403,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u5b9a\u53bf",
            "adcode": 520422,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u5b81\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520423,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u5173\u5cad\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520424,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u7d2b\u4e91\u82d7\u65cf\u5e03\u4f9d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520425,
            "citycode": 853
        },
        {
            "\u4e2d\u6587\u540d": "\u6bd5\u8282\u5e02",
            "adcode": 520500,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u4e03\u661f\u5173\u533a",
            "adcode": 520502,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u65b9\u53bf",
            "adcode": 520521,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed4\u897f\u53bf",
            "adcode": 520522,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u6c99\u53bf",
            "adcode": 520523,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u7ec7\u91d1\u53bf",
            "adcode": 520524,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u7eb3\u96cd\u53bf",
            "adcode": 520525,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u5b81\u5f5d\u65cf\u56de\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520526,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u8d6b\u7ae0\u53bf",
            "adcode": 520527,
            "citycode": 857
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u4ec1\u5e02",
            "adcode": 520600,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u78a7\u6c5f\u533a",
            "adcode": 520602,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u4e07\u5c71\u533a",
            "adcode": 520603,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u53e3\u53bf",
            "adcode": 520621,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u5c4f\u4f97\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520622,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u9621\u53bf",
            "adcode": 520623,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u601d\u5357\u53bf",
            "adcode": 520624,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u5370\u6c5f\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520625,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u6c5f\u53bf",
            "adcode": 520626,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbf\u6cb3\u571f\u5bb6\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520627,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u677e\u6843\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 520628,
            "citycode": 856
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed4\u897f\u5357\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 522300,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u4e49\u5e02",
            "adcode": 522301,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u4ec1\u5e02",
            "adcode": 522302,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u5b89\u53bf",
            "adcode": 522323,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u6674\u9686\u53bf",
            "adcode": 522324,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u8d1e\u4e30\u53bf",
            "adcode": 522325,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u8c1f\u53bf",
            "adcode": 522326,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u518c\u4ea8\u53bf",
            "adcode": 522327,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u9f99\u53bf",
            "adcode": 522328,
            "citycode": 859
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed4\u4e1c\u5357\u82d7\u65cf\u4f97\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 522600,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u51ef\u91cc\u5e02",
            "adcode": 522601,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5e73\u53bf",
            "adcode": 522622,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u65bd\u79c9\u53bf",
            "adcode": 522623,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u7a57\u53bf",
            "adcode": 522624,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u8fdc\u53bf",
            "adcode": 522625,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u5c91\u5de9\u53bf",
            "adcode": 522626,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u67f1\u53bf",
            "adcode": 522627,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9526\u5c4f\u53bf",
            "adcode": 522628,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u5251\u6cb3\u53bf",
            "adcode": 522629,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u6c5f\u53bf",
            "adcode": 522630,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9ece\u5e73\u53bf",
            "adcode": 522631,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u6995\u6c5f\u53bf",
            "adcode": 522632,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u4ece\u6c5f\u53bf",
            "adcode": 522633,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u96f7\u5c71\u53bf",
            "adcode": 522634,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u6c5f\u53bf",
            "adcode": 522635,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u5be8\u53bf",
            "adcode": 522636,
            "citycode": 855
        },
        {
            "\u4e2d\u6587\u540d": "\u9ed4\u5357\u5e03\u4f9d\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 522700,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u90fd\u5300\u5e02",
            "adcode": 522701,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u6cc9\u5e02",
            "adcode": 522702,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u8354\u6ce2\u53bf",
            "adcode": 522722,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u5b9a\u53bf",
            "adcode": 522723,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u74ee\u5b89\u53bf",
            "adcode": 522725,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u72ec\u5c71\u53bf",
            "adcode": 522726,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5858\u53bf",
            "adcode": 522727,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u7538\u53bf",
            "adcode": 522728,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u987a\u53bf",
            "adcode": 522729,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u91cc\u53bf",
            "adcode": 522730,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u6c34\u53bf",
            "adcode": 522731,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u90fd\u6c34\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 522732,
            "citycode": 854
        },
        {
            "\u4e2d\u6587\u540d": "\u6606\u660e\u5e02",
            "adcode": 530100,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u6606\u660e\u5e02\u5e02\u8f96\u533a",
            "adcode": 530101,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u534e\u533a",
            "adcode": 530102,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u76d8\u9f99\u533a",
            "adcode": 530103,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5b98\u6e21\u533a",
            "adcode": 530111,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5c71\u533a",
            "adcode": 530112,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u5ddd\u533a",
            "adcode": 530113,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5448\u8d21\u533a",
            "adcode": 530114,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u664b\u5b81\u533a",
            "adcode": 530115,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u6c11\u53bf",
            "adcode": 530124,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u826f\u53bf",
            "adcode": 530125,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u6797\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530126,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5d69\u660e\u53bf",
            "adcode": 530127,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u7984\u529d\u5f5d\u65cf\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530128,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5bfb\u7538\u56de\u65cf\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530129,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5b81\u5e02",
            "adcode": 530181,
            "citycode": 871
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u9756\u5e02",
            "adcode": 530300,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u9756\u5e02\u5e02\u8f96\u533a",
            "adcode": 530301,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u9e92\u9e9f\u533a",
            "adcode": 530302,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbe\u76ca\u533a",
            "adcode": 530303,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u9f99\u533a",
            "adcode": 530304,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u9646\u826f\u53bf",
            "adcode": 530322,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u5e08\u5b97\u53bf",
            "adcode": 530323,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u7f57\u5e73\u53bf",
            "adcode": 530324,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u6e90\u53bf",
            "adcode": 530325,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u6cfd\u53bf",
            "adcode": 530326,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u5ba3\u5a01\u5e02",
            "adcode": 530381,
            "citycode": 874
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6eaa\u5e02",
            "adcode": 530400,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6eaa\u5e02\u5e02\u8f96\u533a",
            "adcode": 530401,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u5854\u533a",
            "adcode": 530402,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5ddd\u533a",
            "adcode": 530403,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u6f84\u6c5f\u5e02",
            "adcode": 530481,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u6d77\u53bf",
            "adcode": 530423,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u5b81\u53bf",
            "adcode": 530424,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u6613\u95e8\u53bf",
            "adcode": 530425,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u5ce8\u5c71\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530426,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5e73\u5f5d\u65cf\u50a3\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530427,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u6c5f\u54c8\u5c3c\u65cf\u5f5d\u65cf\u50a3\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530428,
            "citycode": 877
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5c71\u5e02",
            "adcode": 530500,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u4fdd\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 530501,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u9633\u533a",
            "adcode": 530502,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u65bd\u7538\u53bf",
            "adcode": 530521,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u9f99\u9675\u53bf",
            "adcode": 530523,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u5b81\u53bf",
            "adcode": 530524,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u817e\u51b2\u5e02",
            "adcode": 530581,
            "citycode": 875
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u901a\u5e02",
            "adcode": 530600,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u901a\u5e02\u5e02\u8f96\u533a",
            "adcode": 530601,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u9633\u533a",
            "adcode": 530602,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u9c81\u7538\u53bf",
            "adcode": 530621,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u5de7\u5bb6\u53bf",
            "adcode": 530622,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u6d25\u53bf",
            "adcode": 530623,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5173\u53bf",
            "adcode": 530624,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5584\u53bf",
            "adcode": 530625,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u6c5f\u53bf",
            "adcode": 530626,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u96c4\u53bf",
            "adcode": 530627,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u5f5d\u826f\u53bf",
            "adcode": 530628,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u5a01\u4fe1\u53bf",
            "adcode": 530629,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u6c34\u5bcc\u5e02",
            "adcode": 530681,
            "citycode": 870
        },
        {
            "\u4e2d\u6587\u540d": "\u4e3d\u6c5f\u5e02",
            "adcode": 530700,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u4e3d\u6c5f\u5e02\u5e02\u8f96\u533a",
            "adcode": 530701,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u57ce\u533a",
            "adcode": 530702,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u9f99\u7eb3\u897f\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530721,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u80dc\u53bf",
            "adcode": 530722,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u576a\u53bf",
            "adcode": 530723,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u8497\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530724,
            "citycode": 888
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u6d31\u5e02",
            "adcode": 530800,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u6d31\u5e02\u5e02\u8f96\u533a",
            "adcode": 530801,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u601d\u8305\u533a",
            "adcode": 530802,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u6d31\u54c8\u5c3c\u65cf\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530821,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u58a8\u6c5f\u54c8\u5c3c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530822,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u4e1c\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530823,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u8c37\u50a3\u65cf\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530824,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u6c85\u5f5d\u65cf\u54c8\u5c3c\u65cf\u62c9\u795c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530825,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u57ce\u54c8\u5c3c\u65cf\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530826,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u5b5f\u8fde\u50a3\u65cf\u62c9\u795c\u65cf\u4f64\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530827,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u6f9c\u6ca7\u62c9\u795c\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530828,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u76df\u4f64\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530829,
            "citycode": 879
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6ca7\u5e02",
            "adcode": 530900,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6ca7\u5e02\u5e02\u8f96\u533a",
            "adcode": 530901,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u7fd4\u533a",
            "adcode": 530902,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u5e86\u53bf",
            "adcode": 530921,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u53bf",
            "adcode": 530922,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5fb7\u53bf",
            "adcode": 530923,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u5eb7\u53bf",
            "adcode": 530924,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6c5f\u62c9\u795c\u65cf\u4f64\u65cf\u5e03\u6717\u65cf\u50a3\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530925,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u803f\u9a6c\u50a3\u65cf\u4f64\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530926,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u6ca7\u6e90\u4f64\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 530927,
            "citycode": 883
        },
        {
            "\u4e2d\u6587\u540d": "\u695a\u96c4\u5f5d\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 532300,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u695a\u96c4\u5e02",
            "adcode": 532301,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u67cf\u53bf",
            "adcode": 532322,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u725f\u5b9a\u53bf",
            "adcode": 532323,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u534e\u53bf",
            "adcode": 532324,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u59da\u5b89\u53bf",
            "adcode": 532325,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u59da\u53bf",
            "adcode": 532326,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u4ec1\u53bf",
            "adcode": 532327,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u8c0b\u53bf",
            "adcode": 532328,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5b9a\u53bf",
            "adcode": 532329,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u7984\u4e30\u53bf",
            "adcode": 532331,
            "citycode": 878
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u6cb3\u54c8\u5c3c\u65cf\u5f5d\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 532500,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2a\u65e7\u5e02",
            "adcode": 532501,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u5f00\u8fdc\u5e02",
            "adcode": 532502,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u8499\u81ea\u5e02",
            "adcode": 532503,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u5f25\u52d2\u5e02",
            "adcode": 532504,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u5c4f\u8fb9\u82d7\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532523,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u5efa\u6c34\u53bf",
            "adcode": 532524,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5c4f\u53bf",
            "adcode": 532525,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u897f\u53bf",
            "adcode": 532527,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u9633\u53bf",
            "adcode": 532528,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u6cb3\u53bf",
            "adcode": 532529,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5e73\u82d7\u65cf\u7476\u65cf\u50a3\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532530,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u7eff\u6625\u53bf",
            "adcode": 532531,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u53e3\u7476\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532532,
            "citycode": 873
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u5c71\u58ee\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 532600,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u5c71\u5e02",
            "adcode": 532601,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u781a\u5c71\u53bf",
            "adcode": 532622,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u7574\u53bf",
            "adcode": 532623,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u9ebb\u6817\u5761\u53bf",
            "adcode": 532624,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u9a6c\u5173\u53bf",
            "adcode": 532625,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u4e18\u5317\u53bf",
            "adcode": 532626,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u5357\u53bf",
            "adcode": 532627,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u5b81\u53bf",
            "adcode": 532628,
            "citycode": 876
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u53cc\u7248\u7eb3\u50a3\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 532800,
            "citycode": 691
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u6d2a\u5e02",
            "adcode": 532801,
            "citycode": 691
        },
        {
            "\u4e2d\u6587\u540d": "\u52d0\u6d77\u53bf",
            "adcode": 532822,
            "citycode": 691
        },
        {
            "\u4e2d\u6587\u540d": "\u52d0\u814a\u53bf",
            "adcode": 532823,
            "citycode": 691
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7406\u767d\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 532900,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u7406\u5e02",
            "adcode": 532901,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u6f3e\u6fde\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532922,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u7965\u4e91\u53bf",
            "adcode": 532923,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5bbe\u5ddd\u53bf",
            "adcode": 532924,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5f25\u6e21\u53bf",
            "adcode": 532925,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6da7\u5f5d\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532926,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5dcd\u5c71\u5f5d\u65cf\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 532927,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5e73\u53bf",
            "adcode": 532928,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u4e91\u9f99\u53bf",
            "adcode": 532929,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u6d31\u6e90\u53bf",
            "adcode": 532930,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5251\u5ddd\u53bf",
            "adcode": 532931,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u9e64\u5e86\u53bf",
            "adcode": 532932,
            "citycode": 872
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u5b8f\u50a3\u65cf\u666f\u9887\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 533100,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u745e\u4e3d\u5e02",
            "adcode": 533102,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u8292\u5e02",
            "adcode": 533103,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u6881\u6cb3\u53bf",
            "adcode": 533122,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u76c8\u6c5f\u53bf",
            "adcode": 533123,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u9647\u5ddd\u53bf",
            "adcode": 533124,
            "citycode": 692
        },
        {
            "\u4e2d\u6587\u540d": "\u6012\u6c5f\u5088\u50f3\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 533300,
            "citycode": 886
        },
        {
            "\u4e2d\u6587\u540d": "\u6cf8\u6c34\u5e02",
            "adcode": 533301,
            "citycode": 886
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u8d21\u53bf",
            "adcode": 533323,
            "citycode": 886
        },
        {
            "\u4e2d\u6587\u540d": "\u8d21\u5c71\u72ec\u9f99\u65cf\u6012\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 533324,
            "citycode": 886
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u576a\u767d\u65cf\u666e\u7c73\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 533325,
            "citycode": 886
        },
        {
            "\u4e2d\u6587\u540d": "\u8fea\u5e86\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 533400,
            "citycode": 887
        },
        {
            "\u4e2d\u6587\u540d": "\u9999\u683c\u91cc\u62c9\u5e02",
            "adcode": 533401,
            "citycode": 887
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u94a6\u53bf",
            "adcode": 533422,
            "citycode": 887
        },
        {
            "\u4e2d\u6587\u540d": "\u7ef4\u897f\u5088\u50f3\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 533423,
            "citycode": 887
        },
        {
            "\u4e2d\u6587\u540d": "\u62c9\u8428\u5e02",
            "adcode": 540100,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u62c9\u8428\u5e02\u5e02\u8f96\u533a",
            "adcode": 540101,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u5173\u533a",
            "adcode": 540102,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u5806\u9f99\u5fb7\u5e86\u533a",
            "adcode": 540103,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5b5c\u533a",
            "adcode": 540104,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u5468\u53bf",
            "adcode": 540121,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u5f53\u96c4\u53bf",
            "adcode": 540122,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u5c3c\u6728\u53bf",
            "adcode": 540123,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u6c34\u53bf",
            "adcode": 540124,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u58a8\u7af9\u5de5\u5361\u53bf",
            "adcode": 540127,
            "citycode": 891
        },
        {
            "\u4e2d\u6587\u540d": "\u65e5\u5580\u5219\u5e02",
            "adcode": 540200,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u6851\u73e0\u5b5c\u533a",
            "adcode": 540202,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u6728\u6797\u53bf",
            "adcode": 540221,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u5b5c\u53bf",
            "adcode": 540222,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u65e5\u53bf",
            "adcode": 540223,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u8428\u8fe6\u53bf",
            "adcode": 540224,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u62c9\u5b5c\u53bf",
            "adcode": 540225,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u6602\u4ec1\u53bf",
            "adcode": 540226,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u8c22\u901a\u95e8\u53bf",
            "adcode": 540227,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u6717\u53bf",
            "adcode": 540228,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u4ec1\u5e03\u53bf",
            "adcode": 540229,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u9a6c\u53bf",
            "adcode": 540230,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u7ed3\u53bf",
            "adcode": 540231,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u4ef2\u5df4\u53bf",
            "adcode": 540232,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u4e9a\u4e1c\u53bf",
            "adcode": 540233,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u9686\u53bf",
            "adcode": 540234,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u8042\u62c9\u6728\u53bf",
            "adcode": 540235,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u8428\u560e\u53bf",
            "adcode": 540236,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u5c97\u5df4\u53bf",
            "adcode": 540237,
            "citycode": 892
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u90fd\u5e02",
            "adcode": 540300,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u5361\u82e5\u533a",
            "adcode": 540302,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u6c5f\u8fbe\u53bf",
            "adcode": 540321,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u8d21\u89c9\u53bf",
            "adcode": 540322,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u7c7b\u4e4c\u9f50\u53bf",
            "adcode": 540323,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u4e01\u9752\u53bf",
            "adcode": 540324,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u96c5\u53bf",
            "adcode": 540325,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u516b\u5bbf\u53bf",
            "adcode": 540326,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u5de6\u8d21\u53bf",
            "adcode": 540327,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u8292\u5eb7\u53bf",
            "adcode": 540328,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u9686\u53bf",
            "adcode": 540329,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u8fb9\u575d\u53bf",
            "adcode": 540330,
            "citycode": 895
        },
        {
            "\u4e2d\u6587\u540d": "\u6797\u829d\u5e02",
            "adcode": 540400,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u5b9c\u533a",
            "adcode": 540402,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u5de5\u5e03\u6c5f\u8fbe\u53bf",
            "adcode": 540421,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u7c73\u6797\u53bf",
            "adcode": 540422,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u58a8\u8131\u53bf",
            "adcode": 540423,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u6ce2\u5bc6\u53bf",
            "adcode": 540424,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u9685\u53bf",
            "adcode": 540425,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u6717\u53bf",
            "adcode": 540426,
            "citycode": 894
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u5357\u5e02",
            "adcode": 540500,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u4e43\u4e1c\u533a",
            "adcode": 540502,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u624e\u56ca\u53bf",
            "adcode": 540521,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u8d21\u560e\u53bf",
            "adcode": 540522,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u6851\u65e5\u53bf",
            "adcode": 540523,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u743c\u7ed3\u53bf",
            "adcode": 540524,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u677e\u53bf",
            "adcode": 540525,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u63aa\u7f8e\u53bf",
            "adcode": 540526,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u624e\u53bf",
            "adcode": 540527,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u52a0\u67e5\u53bf",
            "adcode": 540528,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u5b50\u53bf",
            "adcode": 540529,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u9519\u90a3\u53bf",
            "adcode": 540530,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u6d6a\u5361\u5b50\u53bf",
            "adcode": 540531,
            "citycode": 893
        },
        {
            "\u4e2d\u6587\u540d": "\u90a3\u66f2\u5e02",
            "adcode": 540600,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u8272\u5c3c\u533a",
            "adcode": 540602,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u9ece\u53bf",
            "adcode": 540621,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u6bd4\u5982\u53bf",
            "adcode": 540622,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u8042\u8363\u53bf",
            "adcode": 540623,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u591a\u53bf",
            "adcode": 540624,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u7533\u624e\u53bf",
            "adcode": 540625,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u7d22\u53bf",
            "adcode": 540626,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u73ed\u6208\u53bf",
            "adcode": 540627,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u9752\u53bf",
            "adcode": 540628,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u5c3c\u739b\u53bf",
            "adcode": 540629,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6e56\u53bf",
            "adcode": 540630,
            "citycode": 896
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u91cc\u5730\u533a",
            "adcode": 542500,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u666e\u5170\u53bf",
            "adcode": 542521,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u672d\u8fbe\u53bf",
            "adcode": 542522,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u5676\u5c14\u53bf",
            "adcode": 542523,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u65e5\u571f\u53bf",
            "adcode": 542524,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u9769\u5409\u53bf",
            "adcode": 542525,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u6539\u5219\u53bf",
            "adcode": 542526,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u63aa\u52e4\u53bf",
            "adcode": 542527,
            "citycode": 897
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b89\u5e02",
            "adcode": 610100,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 610101,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u57ce\u533a",
            "adcode": 610102,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u7891\u6797\u533a",
            "adcode": 610103,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u83b2\u6e56\u533a",
            "adcode": 610104,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u705e\u6865\u533a",
            "adcode": 610111,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u672a\u592e\u533a",
            "adcode": 610112,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u96c1\u5854\u533a",
            "adcode": 610113,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u960e\u826f\u533a",
            "adcode": 610114,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6f7c\u533a",
            "adcode": 610115,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u5b89\u533a",
            "adcode": 610116,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u9675\u533a",
            "adcode": 610117,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u9120\u9091\u533a",
            "adcode": 610118,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u84dd\u7530\u53bf",
            "adcode": 610122,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u5468\u81f3\u53bf",
            "adcode": 610124,
            "citycode": 29
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u5ddd\u5e02",
            "adcode": 610200,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u94dc\u5ddd\u5e02\u5e02\u8f96\u533a",
            "adcode": 610201,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u738b\u76ca\u533a",
            "adcode": 610202,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u5370\u53f0\u533a",
            "adcode": 610203,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u8000\u5dde\u533a",
            "adcode": 610204,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u541b\u53bf",
            "adcode": 610222,
            "citycode": 919
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u9e21\u5e02",
            "adcode": 610300,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u9e21\u5e02\u5e02\u8f96\u533a",
            "adcode": 610301,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2d\u6ee8\u533a",
            "adcode": 610302,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u53f0\u533a",
            "adcode": 610303,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u9648\u4ed3\u533a",
            "adcode": 610304,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u7fd4\u53bf",
            "adcode": 610322,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u5c90\u5c71\u53bf",
            "adcode": 610323,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u6276\u98ce\u53bf",
            "adcode": 610324,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u7709\u53bf",
            "adcode": 610326,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u9647\u53bf",
            "adcode": 610327,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u5343\u9633\u53bf",
            "adcode": 610328,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u9e9f\u6e38\u53bf",
            "adcode": 610329,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u51e4\u53bf",
            "adcode": 610330,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u592a\u767d\u53bf",
            "adcode": 610331,
            "citycode": 917
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u9633\u5e02",
            "adcode": 610400,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u54b8\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 610401,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u90fd\u533a",
            "adcode": 610402,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6768\u9675\u533a",
            "adcode": 610403,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2d\u57ce\u533a",
            "adcode": 610404,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u4e09\u539f\u53bf",
            "adcode": 610422,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfe\u9633\u53bf",
            "adcode": 610423,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u4e7e\u53bf",
            "adcode": 610424,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u793c\u6cc9\u53bf",
            "adcode": 610425,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5bff\u53bf",
            "adcode": 610426,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6c\u5dde\u5e02",
            "adcode": 610482,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u957f\u6b66\u53bf",
            "adcode": 610428,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u65ec\u9091\u53bf",
            "adcode": 610429,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6df3\u5316\u53bf",
            "adcode": 610430,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u529f\u53bf",
            "adcode": 610431,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5e73\u5e02",
            "adcode": 610481,
            "citycode": 910
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2d\u5357\u5e02",
            "adcode": 610500,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2d\u5357\u5e02\u5e02\u8f96\u533a",
            "adcode": 610501,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6e2d\u533a",
            "adcode": 610502,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u5dde\u533a",
            "adcode": 610503,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u6f7c\u5173\u53bf",
            "adcode": 610522,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u8354\u53bf",
            "adcode": 610523,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u9633\u53bf",
            "adcode": 610524,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u6f84\u57ce\u53bf",
            "adcode": 610525,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u84b2\u57ce\u53bf",
            "adcode": 610526,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u6c34\u53bf",
            "adcode": 610527,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u5e73\u53bf",
            "adcode": 610528,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u97e9\u57ce\u5e02",
            "adcode": 610581,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u9634\u5e02",
            "adcode": 610582,
            "citycode": 913
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5b89\u5e02",
            "adcode": 610600,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5b89\u5e02\u5e02\u8f96\u533a",
            "adcode": 610601,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9d\u5854\u533a",
            "adcode": 610602,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u585e\u533a",
            "adcode": 610603,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u957f\u53bf",
            "adcode": 610621,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5ef6\u5ddd\u53bf",
            "adcode": 610622,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5b50\u957f\u5e02",
            "adcode": 610681,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5fd7\u4e39\u53bf",
            "adcode": 610625,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u8d77\u53bf",
            "adcode": 610626,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u6cc9\u53bf",
            "adcode": 610627,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u53bf",
            "adcode": 610628,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u5ddd\u53bf",
            "adcode": 610629,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9c\u5ddd\u53bf",
            "adcode": 610630,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u9f99\u53bf",
            "adcode": 610631,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u9675\u53bf",
            "adcode": 610632,
            "citycode": 911
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u4e2d\u5e02",
            "adcode": 610700,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u4e2d\u5e02\u5e02\u8f96\u533a",
            "adcode": 610701,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u53f0\u533a",
            "adcode": 610702,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u90d1\u533a",
            "adcode": 610703,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u56fa\u53bf",
            "adcode": 610722,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u6d0b\u53bf",
            "adcode": 610723,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u4e61\u53bf",
            "adcode": 610724,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u52c9\u53bf",
            "adcode": 610725,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u5f3a\u53bf",
            "adcode": 610726,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u7565\u9633\u53bf",
            "adcode": 610727,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u5df4\u53bf",
            "adcode": 610728,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u7559\u575d\u53bf",
            "adcode": 610729,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u4f5b\u576a\u53bf",
            "adcode": 610730,
            "citycode": 916
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u6797\u5e02",
            "adcode": 610800,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u6797\u5e02\u5e02\u8f96\u533a",
            "adcode": 610801,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u9633\u533a",
            "adcode": 610802,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u6a2a\u5c71\u533a",
            "adcode": 610803,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u5e9c\u8c37\u53bf",
            "adcode": 610822,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u8fb9\u53bf",
            "adcode": 610824,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u8fb9\u53bf",
            "adcode": 610825,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u7ee5\u5fb7\u53bf",
            "adcode": 610826,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u7c73\u8102\u53bf",
            "adcode": 610827,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u4f73\u53bf",
            "adcode": 610828,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u5821\u53bf",
            "adcode": 610829,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6da7\u53bf",
            "adcode": 610830,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u5b50\u6d32\u53bf",
            "adcode": 610831,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u795e\u6728\u5e02",
            "adcode": 610881,
            "citycode": 912
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5eb7\u5e02",
            "adcode": 610900,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5eb7\u5e02\u5e02\u8f96\u533a",
            "adcode": 610901,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u6ee8\u533a",
            "adcode": 610902,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u6c49\u9634\u53bf",
            "adcode": 610921,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u6cc9\u53bf",
            "adcode": 610922,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u9655\u53bf",
            "adcode": 610923,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u7d2b\u9633\u53bf",
            "adcode": 610924,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u5c9a\u768b\u53bf",
            "adcode": 610925,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5229\u53bf",
            "adcode": 610926,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u576a\u53bf",
            "adcode": 610927,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u65ec\u9633\u53bf",
            "adcode": 610928,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u6cb3\u53bf",
            "adcode": 610929,
            "citycode": 915
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u6d1b\u5e02",
            "adcode": 611000,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u6d1b\u5e02\u5e02\u8f96\u533a",
            "adcode": 611001,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u5dde\u533a",
            "adcode": 611002,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u5357\u53bf",
            "adcode": 611021,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u4e39\u51e4\u53bf",
            "adcode": 611022,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u5546\u5357\u53bf",
            "adcode": 611023,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u9633\u53bf",
            "adcode": 611024,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u5b89\u53bf",
            "adcode": 611025,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u67de\u6c34\u53bf",
            "adcode": 611026,
            "citycode": 914
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u5dde\u5e02",
            "adcode": 620100,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u5170\u5dde\u5e02\u5e02\u8f96\u533a",
            "adcode": 620101,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u5173\u533a",
            "adcode": 620102,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u4e03\u91cc\u6cb3\u533a",
            "adcode": 620103,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u56fa\u533a",
            "adcode": 620104,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5b81\u533a",
            "adcode": 620105,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u53e4\u533a",
            "adcode": 620111,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u767b\u53bf",
            "adcode": 620121,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u768b\u5170\u53bf",
            "adcode": 620122,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u6986\u4e2d\u53bf",
            "adcode": 620123,
            "citycode": 931
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5cea\u5173\u5e02",
            "adcode": 620200,
            "citycode": 1937
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u5cea\u5173\u5e02\u5e02\u8f96\u533a",
            "adcode": 620201,
            "citycode": 1937
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u660c\u5e02",
            "adcode": 620300,
            "citycode": 935
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u660c\u5e02\u5e02\u8f96\u533a",
            "adcode": 620301,
            "citycode": 935
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5ddd\u533a",
            "adcode": 620302,
            "citycode": 935
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u660c\u53bf",
            "adcode": 620321,
            "citycode": 935
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u94f6\u5e02",
            "adcode": 620400,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u94f6\u5e02\u5e02\u8f96\u533a",
            "adcode": 620401,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u94f6\u533a",
            "adcode": 620402,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5ddd\u533a",
            "adcode": 620403,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u9756\u8fdc\u53bf",
            "adcode": 620421,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u4f1a\u5b81\u53bf",
            "adcode": 620422,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u666f\u6cf0\u53bf",
            "adcode": 620423,
            "citycode": 943
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6c34\u5e02",
            "adcode": 620500,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u6c34\u5e02\u5e02\u8f96\u533a",
            "adcode": 620501,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u5dde\u533a",
            "adcode": 620502,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u9ea6\u79ef\u533a",
            "adcode": 620503,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u6e05\u6c34\u53bf",
            "adcode": 620521,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u79e6\u5b89\u53bf",
            "adcode": 620522,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u8c37\u53bf",
            "adcode": 620523,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5c71\u53bf",
            "adcode": 620524,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u5bb6\u5ddd\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 620525,
            "citycode": 938
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5a01\u5e02",
            "adcode": 620600,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u5a01\u5e02\u5e02\u8f96\u533a",
            "adcode": 620601,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u51c9\u5dde\u533a",
            "adcode": 620602,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u6c11\u52e4\u53bf",
            "adcode": 620621,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u53e4\u6d6a\u53bf",
            "adcode": 620622,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u795d\u85cf\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 620623,
            "citycode": 1935
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u6396\u5e02",
            "adcode": 620700,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u5f20\u6396\u5e02\u5e02\u8f96\u533a",
            "adcode": 620701,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5dde\u533a",
            "adcode": 620702,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u8083\u5357\u88d5\u56fa\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 620721,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u6c11\u4e50\u53bf",
            "adcode": 620722,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6cfd\u53bf",
            "adcode": 620723,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u53f0\u53bf",
            "adcode": 620724,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u5c71\u4e39\u53bf",
            "adcode": 620725,
            "citycode": 936
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u51c9\u5e02",
            "adcode": 620800,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u51c9\u5e02\u5e02\u8f96\u533a",
            "adcode": 620801,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u5d06\u5cd2\u533a",
            "adcode": 620802,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfe\u5ddd\u53bf",
            "adcode": 620821,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u53f0\u53bf",
            "adcode": 620822,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u5d07\u4fe1\u53bf",
            "adcode": 620823,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u4ead\u5e02",
            "adcode": 620881,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u5e84\u6d6a\u53bf",
            "adcode": 620825,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u9759\u5b81\u53bf",
            "adcode": 620826,
            "citycode": 933
        },
        {
            "\u4e2d\u6587\u540d": "\u9152\u6cc9\u5e02",
            "adcode": 620900,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u9152\u6cc9\u5e02\u5e02\u8f96\u533a",
            "adcode": 620901,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u8083\u5dde\u533a",
            "adcode": 620902,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u5854\u53bf",
            "adcode": 620921,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u74dc\u5dde\u53bf",
            "adcode": 620922,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u8083\u5317\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 620923,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u514b\u585e\u54c8\u8428\u514b\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 620924,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u95e8\u5e02",
            "adcode": 620981,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u6566\u714c\u5e02",
            "adcode": 620982,
            "citycode": 937
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u9633\u5e02",
            "adcode": 621000,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u9633\u5e02\u5e02\u8f96\u533a",
            "adcode": 621001,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5cf0\u533a",
            "adcode": 621002,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u5e86\u57ce\u53bf",
            "adcode": 621021,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u73af\u53bf",
            "adcode": 621022,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u534e\u6c60\u53bf",
            "adcode": 621023,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u6c34\u53bf",
            "adcode": 621024,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u6b63\u5b81\u53bf",
            "adcode": 621025,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u5b81\u53bf",
            "adcode": 621026,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u9547\u539f\u53bf",
            "adcode": 621027,
            "citycode": 934
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u897f\u5e02",
            "adcode": 621100,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u5b9a\u897f\u5e02\u5e02\u8f96\u533a",
            "adcode": 621101,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u5b89\u5b9a\u533a",
            "adcode": 621102,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u901a\u6e2d\u53bf",
            "adcode": 621121,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u9647\u897f\u53bf",
            "adcode": 621122,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u6e2d\u6e90\u53bf",
            "adcode": 621123,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6d2e\u53bf",
            "adcode": 621124,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u6f33\u53bf",
            "adcode": 621125,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb7\u53bf",
            "adcode": 621126,
            "citycode": 932
        },
        {
            "\u4e2d\u6587\u540d": "\u9647\u5357\u5e02",
            "adcode": 621200,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u9647\u5357\u5e02\u5e02\u8f96\u533a",
            "adcode": 621201,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u6b66\u90fd\u533a",
            "adcode": 621202,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u6210\u53bf",
            "adcode": 621221,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u6587\u53bf",
            "adcode": 621222,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u5b95\u660c\u53bf",
            "adcode": 621223,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u53bf",
            "adcode": 621224,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u548c\u53bf",
            "adcode": 621225,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u793c\u53bf",
            "adcode": 621226,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u5fbd\u53bf",
            "adcode": 621227,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u4e24\u5f53\u53bf",
            "adcode": 621228,
            "citycode": 2935
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u590f\u56de\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 622900,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u590f\u5e02",
            "adcode": 622901,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u590f\u53bf",
            "adcode": 622921,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u5eb7\u4e50\u53bf",
            "adcode": 622922,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u9756\u53bf",
            "adcode": 622923,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u5e7f\u6cb3\u53bf",
            "adcode": 622924,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u653f\u53bf",
            "adcode": 622925,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u4e61\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 622926,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u79ef\u77f3\u5c71\u4fdd\u5b89\u65cf\u4e1c\u4e61\u65cf\u6492\u62c9\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 622927,
            "citycode": 930
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5357\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 623000,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u5408\u4f5c\u5e02",
            "adcode": 623001,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u4e34\u6f6d\u53bf",
            "adcode": 623021,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u5353\u5c3c\u53bf",
            "adcode": 623022,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u821f\u66f2\u53bf",
            "adcode": 623023,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u8fed\u90e8\u53bf",
            "adcode": 623024,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u739b\u66f2\u53bf",
            "adcode": 623025,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u788c\u66f2\u53bf",
            "adcode": 623026,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u590f\u6cb3\u53bf",
            "adcode": 623027,
            "citycode": 941
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b81\u5e02",
            "adcode": 630100,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5b81\u5e02\u5e02\u8f96\u533a",
            "adcode": 630101,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u4e1c\u533a",
            "adcode": 630102,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u4e2d\u533a",
            "adcode": 630103,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u897f\u533a",
            "adcode": 630104,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u57ce\u5317\u533a",
            "adcode": 630105,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u901a\u56de\u65cf\u571f\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 630121,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u6e5f\u4e2d\u533a",
            "adcode": 630106,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u6e5f\u6e90\u53bf",
            "adcode": 630123,
            "citycode": 971
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u4e1c\u5e02",
            "adcode": 630200,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u4e50\u90fd\u533a",
            "adcode": 630202,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u5b89\u533a",
            "adcode": 630203,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u6c11\u548c\u56de\u65cf\u571f\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 630222,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u4e92\u52a9\u571f\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 630223,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u5316\u9686\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 630224,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u5faa\u5316\u6492\u62c9\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 630225,
            "citycode": 972
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5317\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632200,
            "citycode": 970
        },
        {
            "\u4e2d\u6587\u540d": "\u95e8\u6e90\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 632221,
            "citycode": 970
        },
        {
            "\u4e2d\u6587\u540d": "\u7941\u8fde\u53bf",
            "adcode": 632222,
            "citycode": 970
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u664f\u53bf",
            "adcode": 632223,
            "citycode": 970
        },
        {
            "\u4e2d\u6587\u540d": "\u521a\u5bdf\u53bf",
            "adcode": 632224,
            "citycode": 970
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5357\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632300,
            "citycode": 973
        },
        {
            "\u4e2d\u6587\u540d": "\u540c\u4ec1\u53bf",
            "adcode": 632321,
            "citycode": 973
        },
        {
            "\u4e2d\u6587\u540d": "\u5c16\u624e\u53bf",
            "adcode": 632322,
            "citycode": 973
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfd\u5e93\u53bf",
            "adcode": 632323,
            "citycode": 973
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb3\u5357\u8499\u53e4\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 632324,
            "citycode": 973
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u5357\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632500,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u5171\u548c\u53bf",
            "adcode": 632521,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u540c\u5fb7\u53bf",
            "adcode": 632522,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u5fb7\u53bf",
            "adcode": 632523,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u6d77\u53bf",
            "adcode": 632524,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u8d35\u5357\u53bf",
            "adcode": 632525,
            "citycode": 974
        },
        {
            "\u4e2d\u6587\u540d": "\u679c\u6d1b\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632600,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u739b\u6c81\u53bf",
            "adcode": 632621,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u73ed\u739b\u53bf",
            "adcode": 632622,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u7518\u5fb7\u53bf",
            "adcode": 632623,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u65e5\u53bf",
            "adcode": 632624,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u4e45\u6cbb\u53bf",
            "adcode": 632625,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u739b\u591a\u53bf",
            "adcode": 632626,
            "citycode": 975
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6811\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632700,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u7389\u6811\u5e02",
            "adcode": 632701,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u6742\u591a\u53bf",
            "adcode": 632722,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u79f0\u591a\u53bf",
            "adcode": 632723,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u6cbb\u591a\u53bf",
            "adcode": 632724,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u56ca\u8c26\u53bf",
            "adcode": 632725,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u66f2\u9ebb\u83b1\u53bf",
            "adcode": 632726,
            "citycode": 976
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u897f\u8499\u53e4\u65cf\u85cf\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 632800,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u683c\u5c14\u6728\u5e02",
            "adcode": 632801,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u5fb7\u4ee4\u54c8\u5e02",
            "adcode": 632802,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u832b\u5d16\u5e02",
            "adcode": 632803,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5170\u53bf",
            "adcode": 632821,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u90fd\u5170\u53bf",
            "adcode": 632822,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5cfb\u53bf",
            "adcode": 632823,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u897f\u8499\u53e4\u65cf\u85cf\u65cf\u81ea\u6cbb\u5dde\u76f4\u8f96",
            "adcode": 632825,
            "citycode": 977
        },
        {
            "\u4e2d\u6587\u540d": "\u94f6\u5ddd\u5e02",
            "adcode": 640100,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u94f6\u5ddd\u5e02\u5e02\u8f96\u533a",
            "adcode": 640101,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u5174\u5e86\u533a",
            "adcode": 640104,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u590f\u533a",
            "adcode": 640105,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u91d1\u51e4\u533a",
            "adcode": 640106,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u6c38\u5b81\u53bf",
            "adcode": 640121,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u8d3a\u5170\u53bf",
            "adcode": 640122,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u7075\u6b66\u5e02",
            "adcode": 640181,
            "citycode": 951
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5634\u5c71\u5e02",
            "adcode": 640200,
            "citycode": 952
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u5634\u5c71\u5e02\u5e02\u8f96\u533a",
            "adcode": 640201,
            "citycode": 952
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u6b66\u53e3\u533a",
            "adcode": 640202,
            "citycode": 952
        },
        {
            "\u4e2d\u6587\u540d": "\u60e0\u519c\u533a",
            "adcode": 640205,
            "citycode": 952
        },
        {
            "\u4e2d\u6587\u540d": "\u5e73\u7f57\u53bf",
            "adcode": 640221,
            "citycode": 952
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u5fe0\u5e02",
            "adcode": 640300,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u5434\u5fe0\u5e02\u5e02\u8f96\u533a",
            "adcode": 640301,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u5229\u901a\u533a",
            "adcode": 640302,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u7ea2\u5bfa\u5821\u533a",
            "adcode": 640303,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u76d0\u6c60\u53bf",
            "adcode": 640323,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u540c\u5fc3\u53bf",
            "adcode": 640324,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u94dc\u5ce1\u5e02",
            "adcode": 640381,
            "citycode": 953
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u539f\u5e02",
            "adcode": 640400,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u56fa\u539f\u5e02\u5e02\u8f96\u533a",
            "adcode": 640401,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u539f\u5dde\u533a",
            "adcode": 640402,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u5409\u53bf",
            "adcode": 640422,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u9686\u5fb7\u53bf",
            "adcode": 640423,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfe\u6e90\u53bf",
            "adcode": 640424,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u5f6d\u9633\u53bf",
            "adcode": 640425,
            "citycode": 954
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u536b\u5e02",
            "adcode": 640500,
            "citycode": 1953
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u536b\u5e02\u5e02\u8f96\u533a",
            "adcode": 640501,
            "citycode": 1953
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u5761\u5934\u533a",
            "adcode": 640502,
            "citycode": 1953
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u5b81\u53bf",
            "adcode": 640521,
            "citycode": 1953
        },
        {
            "\u4e2d\u6587\u540d": "\u6d77\u539f\u53bf",
            "adcode": 640522,
            "citycode": 1953
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u9c81\u6728\u9f50\u5e02",
            "adcode": 650100,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u9c81\u6728\u9f50\u5e02\u5e02\u8f96\u533a",
            "adcode": 650101,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u5929\u5c71\u533a",
            "adcode": 650102,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u4f9d\u5df4\u514b\u533a",
            "adcode": 650103,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u5e02\u533a",
            "adcode": 650104,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u6c34\u78e8\u6c9f\u533a",
            "adcode": 650105,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u5934\u5c6f\u6cb3\u533a",
            "adcode": 650106,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u8fbe\u5742\u57ce\u533a",
            "adcode": 650107,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u7c73\u4e1c\u533a",
            "adcode": 650109,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u9c81\u6728\u9f50\u53bf",
            "adcode": 650121,
            "citycode": 991
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u62c9\u739b\u4f9d\u5e02",
            "adcode": 650200,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u62c9\u739b\u4f9d\u5e02\u5e02\u8f96\u533a",
            "adcode": 650201,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u72ec\u5c71\u5b50\u533a",
            "adcode": 650202,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u62c9\u739b\u4f9d\u533a",
            "adcode": 650203,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u767d\u78b1\u6ee9\u533a",
            "adcode": 650204,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u5c14\u79be\u533a",
            "adcode": 650205,
            "citycode": 990
        },
        {
            "\u4e2d\u6587\u540d": "\u5410\u9c81\u756a\u5e02",
            "adcode": 650400,
            "citycode": 995
        },
        {
            "\u4e2d\u6587\u540d": "\u9ad8\u660c\u533a",
            "adcode": 650402,
            "citycode": 995
        },
        {
            "\u4e2d\u6587\u540d": "\u912f\u5584\u53bf",
            "adcode": 650421,
            "citycode": 995
        },
        {
            "\u4e2d\u6587\u540d": "\u6258\u514b\u900a\u53bf",
            "adcode": 650422,
            "citycode": 995
        },
        {
            "\u4e2d\u6587\u540d": "\u80e1\u6768\u6cb3\u5e02",
            "adcode": 659010,
            "citycode": 992
        },
        {
            "\u4e2d\u6587\u540d": "\u54c8\u5bc6\u5e02",
            "adcode": 650500,
            "citycode": 902
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u5dde\u533a",
            "adcode": 650502,
            "citycode": 902
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u91cc\u5764\u54c8\u8428\u514b\u81ea\u6cbb\u53bf",
            "adcode": 650521,
            "citycode": 902
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u543e\u53bf",
            "adcode": 650522,
            "citycode": 902
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u5409\u56de\u65cf\u81ea\u6cbb\u5dde",
            "adcode": 652300,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u660c\u5409\u5e02",
            "adcode": 652301,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u961c\u5eb7\u5e02",
            "adcode": 652302,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u547c\u56fe\u58c1\u53bf",
            "adcode": 652323,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u739b\u7eb3\u65af\u53bf",
            "adcode": 652324,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u5947\u53f0\u53bf",
            "adcode": 652325,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u6728\u8428\u5c14\u53bf",
            "adcode": 652327,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u6728\u5792\u54c8\u8428\u514b\u81ea\u6cbb\u53bf",
            "adcode": 652328,
            "citycode": 994
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u5c14\u5854\u62c9\u8499\u53e4\u81ea\u6cbb\u5dde",
            "adcode": 652700,
            "citycode": 909
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u4e50\u5e02",
            "adcode": 652701,
            "citycode": 909
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u62c9\u5c71\u53e3\u5e02",
            "adcode": 652702,
            "citycode": 909
        },
        {
            "\u4e2d\u6587\u540d": "\u7cbe\u6cb3\u53bf",
            "adcode": 652722,
            "citycode": 909
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u6cc9\u53bf",
            "adcode": 652723,
            "citycode": 909
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u97f3\u90ed\u695e\u8499\u53e4\u81ea\u6cbb\u5dde",
            "adcode": 652800,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u5e93\u5c14\u52d2\u5e02",
            "adcode": 652801,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u8f6e\u53f0\u53bf",
            "adcode": 652822,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u5c09\u7281\u53bf",
            "adcode": 652823,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u82e5\u7f8c\u53bf",
            "adcode": 652824,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u4e14\u672b\u53bf",
            "adcode": 652825,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u7109\u8006\u56de\u65cf\u81ea\u6cbb\u53bf",
            "adcode": 652826,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u9759\u53bf",
            "adcode": 652827,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u7855\u53bf",
            "adcode": 652828,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u535a\u6e56\u53bf",
            "adcode": 652829,
            "citycode": 996
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u514b\u82cf\u5730\u533a",
            "adcode": 652900,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u514b\u82cf\u5e02",
            "adcode": 652901,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u6e29\u5bbf\u53bf",
            "adcode": 652922,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u5e93\u8f66\u5e02",
            "adcode": 652902,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u96c5\u53bf",
            "adcode": 652924,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u548c\u53bf",
            "adcode": 652925,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u62dc\u57ce\u53bf",
            "adcode": 652926,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u4ec0\u53bf",
            "adcode": 652927,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u74e6\u63d0\u53bf",
            "adcode": 652928,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u67ef\u576a\u53bf",
            "adcode": 652929,
            "citycode": 997
        },
        {
            "\u4e2d\u6587\u540d": "\u514b\u5b5c\u52d2\u82cf\u67ef\u5c14\u514b\u5b5c\u81ea\u6cbb\u5dde",
            "adcode": 653000,
            "citycode": 908
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u56fe\u4ec0\u5e02",
            "adcode": 653001,
            "citycode": 908
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u514b\u9676\u53bf",
            "adcode": 653022,
            "citycode": 908
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u5408\u5947\u53bf",
            "adcode": 653023,
            "citycode": 908
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u6070\u53bf",
            "adcode": 653024,
            "citycode": 908
        },
        {
            "\u4e2d\u6587\u540d": "\u5580\u4ec0\u5730\u533a",
            "adcode": 653100,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u5580\u4ec0\u5e02",
            "adcode": 653101,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u758f\u9644\u53bf",
            "adcode": 653121,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u758f\u52d2\u53bf",
            "adcode": 653122,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u82f1\u5409\u6c99\u53bf",
            "adcode": 653123,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u6cfd\u666e\u53bf",
            "adcode": 653124,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u838e\u8f66\u53bf",
            "adcode": 653125,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u53f6\u57ce\u53bf",
            "adcode": 653126,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u9ea6\u76d6\u63d0\u53bf",
            "adcode": 653127,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u5cb3\u666e\u6e56\u53bf",
            "adcode": 653128,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u4f3d\u5e08\u53bf",
            "adcode": 653129,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u5df4\u695a\u53bf",
            "adcode": 653130,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u5854\u4ec0\u5e93\u5c14\u5e72\u5854\u5409\u514b\u81ea\u6cbb\u53bf",
            "adcode": 653131,
            "citycode": 998
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u7530\u5730\u533a",
            "adcode": 653200,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u7530\u5e02",
            "adcode": 653201,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u7530\u53bf",
            "adcode": 653221,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u58a8\u7389\u53bf",
            "adcode": 653222,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u76ae\u5c71\u53bf",
            "adcode": 653223,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u6d1b\u6d66\u53bf",
            "adcode": 653224,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u7b56\u52d2\u53bf",
            "adcode": 653225,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u4e8e\u7530\u53bf",
            "adcode": 653226,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u6c11\u4e30\u53bf",
            "adcode": 653227,
            "citycode": 903
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u7281\u54c8\u8428\u514b\u81ea\u6cbb\u5dde",
            "adcode": 654000,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u5b81\u5e02",
            "adcode": 654002,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u594e\u5c6f\u5e02",
            "adcode": 654003,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u5c14\u679c\u65af\u5e02",
            "adcode": 654004,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u4f0a\u5b81\u53bf",
            "adcode": 654021,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u5bdf\u5e03\u67e5\u5c14\u9521\u4f2f\u81ea\u6cbb\u53bf",
            "adcode": 654022,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u970d\u57ce\u53bf",
            "adcode": 654023,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u5de9\u7559\u53bf",
            "adcode": 654024,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u65b0\u6e90\u53bf",
            "adcode": 654025,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u662d\u82cf\u53bf",
            "adcode": 654026,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u7279\u514b\u65af\u53bf",
            "adcode": 654027,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u5c3c\u52d2\u514b\u53bf",
            "adcode": 654028,
            "citycode": 999
        },
        {
            "\u4e2d\u6587\u540d": "\u5854\u57ce\u5730\u533a",
            "adcode": 654200,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u5854\u57ce\u5e02",
            "adcode": 654201,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u4e4c\u82cf\u5e02",
            "adcode": 654202,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u989d\u654f\u53bf",
            "adcode": 654221,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u6e7e\u53bf",
            "adcode": 654223,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u6258\u91cc\u53bf",
            "adcode": 654224,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u88d5\u6c11\u53bf",
            "adcode": 654225,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u548c\u5e03\u514b\u8d5b\u5c14\u8499\u53e4\u81ea\u6cbb\u53bf",
            "adcode": 654226,
            "citycode": 901
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u52d2\u6cf0\u5730\u533a",
            "adcode": 654300,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u52d2\u6cf0\u5e02",
            "adcode": 654301,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u5e03\u5c14\u6d25\u53bf",
            "adcode": 654321,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u5bcc\u8574\u53bf",
            "adcode": 654322,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u798f\u6d77\u53bf",
            "adcode": 654323,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u54c8\u5df4\u6cb3\u53bf",
            "adcode": 654324,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u9752\u6cb3\u53bf",
            "adcode": 654325,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u5409\u6728\u4e43\u53bf",
            "adcode": 654326,
            "citycode": 906
        },
        {
            "\u4e2d\u6587\u540d": "\u77f3\u6cb3\u5b50\u5e02",
            "adcode": 659001,
            "citycode": 993
        },
        {
            "\u4e2d\u6587\u540d": "\u963f\u62c9\u5c14\u5e02",
            "adcode": 659002,
            "citycode": 1997
        },
        {
            "\u4e2d\u6587\u540d": "\u56fe\u6728\u8212\u514b\u5e02",
            "adcode": 659003,
            "citycode": 1998
        },
        {
            "\u4e2d\u6587\u540d": "\u4e94\u5bb6\u6e20\u5e02",
            "adcode": 659004,
            "citycode": 1994
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u5c6f\u5e02",
            "adcode": 659005,
            "citycode": 1906
        },
        {
            "\u4e2d\u6587\u540d": "\u94c1\u95e8\u5173\u5e02",
            "adcode": 659006,
            "citycode": 1996
        },
        {
            "\u4e2d\u6587\u540d": "\u53cc\u6cb3\u5e02",
            "adcode": 659007,
            "citycode": 1909
        },
        {
            "\u4e2d\u6587\u540d": "\u53ef\u514b\u8fbe\u62c9\u5e02",
            "adcode": 659008,
            "citycode": 1999
        },
        {
            "\u4e2d\u6587\u540d": "\u6606\u7389\u5e02",
            "adcode": 659009,
            "citycode": 1903
        },
        {
            "\u4e2d\u6587\u540d": "\u53f0\u6e7e\u7701",
            "adcode": 710000,
            "citycode": 1886
        },
        {
            "\u4e2d\u6587\u540d": "\u9999\u6e2f\u7279\u522b\u884c\u653f\u533a",
            "adcode": 810000,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u4e2d\u897f\u533a",
            "adcode": 810001,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u6e7e\u4ed4\u533a",
            "adcode": 810002,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u4e1c\u533a",
            "adcode": 810003,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u5357\u533a",
            "adcode": 810004,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u6cb9\u5c16\u65fa\u533a",
            "adcode": 810005,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u6df1\u6c34\u57d7\u533a",
            "adcode": 810006,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u4e5d\u9f99\u57ce\u533a",
            "adcode": 810007,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u9ec4\u5927\u4ed9\u533a",
            "adcode": 810008,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u89c2\u5858\u533a",
            "adcode": 810009,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u8343\u6e7e\u533a",
            "adcode": 810010,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u5c6f\u95e8\u533a",
            "adcode": 810011,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u5143\u6717\u533a",
            "adcode": 810012,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u5317\u533a",
            "adcode": 810013,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u57d4\u533a",
            "adcode": 810014,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u897f\u8d21\u533a",
            "adcode": 810015,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u6c99\u7530\u533a",
            "adcode": 810016,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u8475\u9752\u533a",
            "adcode": 810017,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u79bb\u5c9b\u533a",
            "adcode": 810018,
            "citycode": 1852
        },
        {
            "\u4e2d\u6587\u540d": "\u6fb3\u95e8\u7279\u522b\u884c\u653f\u533a",
            "adcode": 820000,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u5730\u739b\u5802\u533a",
            "adcode": 820001,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u82b1\u738b\u5802\u533a",
            "adcode": 820002,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u671b\u5fb7\u5802\u533a",
            "adcode": 820003,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u5927\u5802\u533a",
            "adcode": 820004,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u98ce\u987a\u5802\u533a",
            "adcode": 820005,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u5609\u6a21\u5802\u533a",
            "adcode": 820006,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u8def\u51fc\u586b\u6d77\u533a",
            "adcode": 820007,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u5723\u65b9\u6d4e\u5404\u5802\u533a",
            "adcode": 820008,
            "citycode": 1853
        },
        {
            "\u4e2d\u6587\u540d": "\u5916\u56fd",
            "adcode": 900000,
            "citycode": 1900
        }
    ]'''


    # 将字符串转换为字典
    data_dict = json.loads(citycode_json)

    # 将字典转换为DataFrame
    df = pd.DataFrame(data_dict)

    df_city = df.drop_duplicates('citycode',keep='first')
    df_city = df_city.set_index('中文名')
    df_zone = df.set_index(['中文名','citycode'])
    return df_zone ,df_city

if __name__ == '__main__':
    codes_pip()




