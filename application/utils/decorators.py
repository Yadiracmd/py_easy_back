from functools import wraps
from flask import request, g
from sqlalchemy.exc import SQLAlchemyError

from application.models import ConsumptionModel, UserModel
from application.schema import UserSchema
from application.utils.ResponseEntity import Response
from exts import db


def ResponseBody(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.is_json:
            data = request.get_json()
            return func(data, *args, **kwargs)  # 将解析后的 JSON 数据传递给原函数
    return wrapper


def charge_user(payCost):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                user = getattr(g, "user", None)

                user_object = UserSchema(many=False).dump(user)
                balance = user_object.get('balance')

                if balance < payCost:
                    return func(False, *args, **kwargs)

                balance = balance - payCost

                if balance < 0:
                    return func(False, *args, **kwargs)

                consumption = ConsumptionModel(funcName=request.base_url, score=payCost, userId=user)
                db.session.add(consumption)
                db.session.query(UserModel).filter_by(id=user.id).update({"balance": balance})
                db.session.commit()
                return func(True, *args, **kwargs)
            except SQLAlchemyError as e:
                db.session.rollback()
                raise RuntimeError("调用失败")


        return wrapper
    return decorator