import pytest
import glob

from lib.common import get_mhealth_subjects


@pytest.mark.parametrize(
    "source, data", [
        (
            "./tests/etc/",
            [
                -9.8184, 0.009971,
                0.29563, 0.0041863,
                0.0041863, 2.1849,
                -9.6967, 0.63077,
                0.1039, -0.84053,
                -0.68762, -0.37,
                -0.36327, 0.29963,
                -8.6499, -4.5781,
                0.18776, -0.44902,
                -1.0103, 0.034483,
                -2.35, -1.6102,
                -0.030899,
                0
            ]
        )
    ]
)
def test_get_mhealth_subjects(source, data):

    test = get_mhealth_subjects(data_source=source)
    
    assert len(test) == 1
    assert isinstance(test[0], dict)
    assert test[0]["data"][0] == data
