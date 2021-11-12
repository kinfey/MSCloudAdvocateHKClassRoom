
from flask import Flask

from user import bp as user_module
from shop import bp as shop_module

app = Flask(__name__)

app.register_blueprint(shop_module,  url_prefix='/')
app.register_blueprint(user_module,  url_prefix='/user')

# if __name__ == '__main__':
#     app.run(debug=True,port=8000)
