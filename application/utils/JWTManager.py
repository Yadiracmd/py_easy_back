import jwt
import datetime


class JWTManager:
    SECRET_KEY = "abcd123456"  # 全局密钥，可作为类属性共享
    DEFAULT_ALGORITHM = "HS256"
    DEFAULT_EXPIRATION_DAYS = 1

    @staticmethod
    def generate_token(user_id, email, secret_key=None, algorithm=None, expiration_days=None):
        """
        生成 JWT token
        :param user_id: 用户 ID
        :param email: 用户邮箱
        :param secret_key: 用于签名的密钥
        :param algorithm: 加密算法
        :param expiration_days: token 的有效期（单位：天）
        :return: 生成的 JWT token
        """
        secret_key = secret_key or JWTManager.SECRET_KEY
        algorithm = algorithm or JWTManager.DEFAULT_ALGORITHM
        expiration_days = expiration_days or JWTManager.DEFAULT_EXPIRATION_DAYS

        payload = {
            'user_id': user_id,
            'email': email,
            'exp': datetime.datetime.now() + datetime.timedelta(days=expiration_days)  # 过期时间
        }
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        return token

    @staticmethod
    def decode_token(token, secret_key=None, algorithm=None):
        """
        解码并验证 JWT token
        :param token: JWT token
        :param secret_key: 用于验证的密钥
        :param algorithm: 加密算法
        :return: 解码后的 payload，如果验证失败会抛出异常
        """
        secret_key = secret_key or JWTManager.SECRET_KEY
        algorithm = algorithm or JWTManager.DEFAULT_ALGORITHM

        try:
            # 解码并验证 token
            payload = jwt.decode(token, secret_key, algorithms=[algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            # JWT 已过期
            return None
        except jwt.InvalidTokenError:
            # 无效的 JWT
            return None

    @staticmethod
    def is_token_expired(token, secret_key=None, algorithm=None):
        """
        检查 JWT 是否已过期
        :param token: JWT token
        :param secret_key: 用于验证的密钥
        :param algorithm: 加密算法
        :return: True 如果 token 已过期，False 如果 token 仍然有效
        """
        payload = JWTManager.decode_token(token, secret_key, algorithm)
        if payload:
            # 如果 payload 存在，说明 token 没有过期
            return False
        return True
