import logging


class VisitCounterUnconfiguredError(Exception):
    """В конфиге приложения отсутствует словарь со счетчиками страниц"""
    pass


def add_visit_counter(app_config: dict, page_name: str, logger: logging.Logger) -> None:
    """
    Увеличивает счетчик просмотров на 1.

    :param app_config: Текущий объект конфига приложения.
    :param page_name: Название страницы.
    :param logger: Логгер приложения.
    :return: Итоговое количество просмотров страницы.
    """

    if 'pages' not in app_config:
        raise VisitCounterUnconfiguredError

    app_config['pages'][page_name] += 1
    logger.info('Page "%s" was viewed %s time(s)', page_name, app_config['pages'][page_name])
