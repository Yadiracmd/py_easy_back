from flask import Blueprint, request
from application.utils.ResponseEntity import Response
from application.utils.decorators import charge_user


bp = Blueprint("jd", __name__, url_prefix='/yd')


@bp.route("/h5st",methods=["GET"])
@charge_user(payCost=30)
def get_json_data(data):
    if data:
        return Response.success("调用成功")
    return Response.fail("余额不足,请联系微信：jzx2968496291")



