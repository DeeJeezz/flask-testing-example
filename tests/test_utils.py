from unittest.mock import Mock

import pytest

import utils


@pytest.mark.parametrize(
    ('app_config', 'expected_value'),
    (
        (
            {
                'pages': {
                    'index': 1,
                },
            },
            2,
        ),
        (
            {
                'pages': {
                    'index': 2,
                },
            },
            3,
        )
    )
)
def test_add_visit_counter(app_config, expected_value):

    utils.add_visit_counter(app_config, 'index', logger=Mock())

    assert expected_value == app_config['pages']['index']


def test_add_visit_counter_with_error():
    with pytest.raises(utils.VisitCounterUnconfiguredError):
        utils.add_visit_counter({}, 'test_page_name', logger=Mock())
