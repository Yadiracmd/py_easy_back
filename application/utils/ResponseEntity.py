from flask import jsonify


class Response:


    @staticmethod
    def success(message, data=None, code=200):
        '''
        成功返回
        :param message:
        :param data:
        :param code:
        :return:
        '''
        response = {
            "message": message,
            "code": code,
        }
        if data:
            response["data"] = data
        return jsonify(response)

    @staticmethod
    def fail(message, data=None, code=401):
        '''
        失败返回
        :param message:
        :param data:
        :param code:
        :return:
        '''
        response = {
            "message": message,
            "code": code
        }

        if isinstance(message, dict):
            error_messages = []

            for field, errors in message.items():
                error_messages.append(errors[0])
            response["message"] = error_messages[0]

        if data:
            response["data"] = data
        return jsonify(response)



