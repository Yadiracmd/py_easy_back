from flask import Blueprint

from application.utils.ResponseEntity import Response
from application.utils.decorators import charge_user

bp = Blueprint("yidun", __name__, url_prefix='/yi')

@bp.route("/y2",methods=["GET"])
@charge_user(payCost=30)
def get_json_data(data):
    if data:
        return Response.success("调用成功")
    return Response.fail("余额不足,请联系微信：jzx2968496291")
