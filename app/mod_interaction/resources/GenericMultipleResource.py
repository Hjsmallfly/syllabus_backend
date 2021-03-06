# coding=utf-8
__author__ = 'smallfly'

from flask_restful import Resource, marshal
from app.mod_interaction.database_operations import common

class GenericMultipleResource(Resource):
    """
    主要用于get多份数据
    """

    # 数据的展示结构
    MARSHAL_STRUCTURE = "MARSHAL_STRUCTURE"

    # 数据模型
    MODEL = "MODEL"

    # 参数解析器
    PARSER_FOR_METHODS_DICT = "PARSER_FOR_METHODS_DICT"

    # 用于封装最后的结果, 即 {"ENVELOPE": result}
    ENVELOPE = "ENVELOPE"

    # 用于处理返回的数据
    RESULT_CALLBACK = "RESULT_CALLBACK"


    def __init__(self, **kwargs):
        self.marshal_structure = kwargs.pop(GenericMultipleResource.MARSHAL_STRUCTURE, None)
        self.model = kwargs.pop(GenericMultipleResource.MODEL, None)
        self.parsers = kwargs.pop(GenericMultipleResource.PARSER_FOR_METHODS_DICT, None)
        self.envelope = kwargs.pop(GenericMultipleResource.ENVELOPE, "data_list")
        self.result_callback = kwargs.pop(GenericMultipleResource.RESULT_CALLBACK, None)


    def get(self):
        args = {}
        if "get" in self.parsers:
            args.update(self.parsers["get"].parse_args())
        # print(args)
        result = common.query_multiple(self.model, **args)
        if result == False:
            return {"error": "wrong field name"}, 400
        if len(result) == 0:
            return {"error": "no resources yet"}, 404
        else:
            if self.result_callback is not None:
                return marshal(self.result_callback(result), self.marshal_structure, envelope=self.envelope)
            return marshal(result, self.marshal_structure, envelope=self.envelope)

