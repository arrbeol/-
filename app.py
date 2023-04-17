from flask import Flask, g, request
from settings import DefaultConfig, DevelopmentConfig
from address.stu import stu_bp
from common.model.stu_model import db
from flask_cors import CORS
from flask_restful import Api, Resource


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/')
def hello_world():
    return 'Hello World!'



def create_flask_app(config):
    # 1.创建对象
    app = Flask(__name__)
    # 2.加载配置
    app.config.from_object(config)

    # 3.返回app
    return app


# 调用工厂方法
app = create_flask_app(DevelopmentConfig)
# 注册蓝图


db.init_app(app)
app.register_blueprint(stu_bp)
cors = CORS(app)


if __name__ == '__main__':
    app.run(port=3001)
