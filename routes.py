from flask import Blueprint, current_app

from utils import add_visit_counter

routes_bp: Blueprint = Blueprint('routes', __name__, url_prefix='/')


def views_counter(func):
    """
    Декоратор-счетчик посещений каждой страницы.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        add_visit_counter(
            app_config=current_app.config,
            page_name=func.__name__,
            logger=current_app.logger,
        )
        return result

    return wrapper


@routes_bp.route('/')
@views_counter
def index():
    """
    Главная страница.
    """

    return '<h3>Hello world</h3>'
