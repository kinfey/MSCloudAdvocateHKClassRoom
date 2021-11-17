from flask import Flask, render_template

from user import bp

@bp.route('/')
@bp.route('/info')
def info():
    return render_template('./user/info.html')