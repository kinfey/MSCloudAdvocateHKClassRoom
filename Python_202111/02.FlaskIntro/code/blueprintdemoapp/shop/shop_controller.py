from flask import Flask, render_template

from shop import bp

@bp.route('/')
def index():
    return render_template('./shop/index.html')