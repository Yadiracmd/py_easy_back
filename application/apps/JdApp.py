from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from application.models import ConsumptionModel, UserModel
from application.schema import UserSchema
from application.utils.ResponseEntity import Response

from flask import g

from application.utils.decorators import charge_user
from exts import db

bp = Blueprint("jd", __name__, url_prefix='/jd')





@bp.route("/h5st",methods=["POST"])
@charge_user(payCost=100)
def get_json_data(data):
    if data:
        return Response.success("调用成功")
    return Response.fail("余额不足")



