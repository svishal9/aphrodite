import shutil
from pathlib import Path

import pytest

from app.com.saraswati.www.src.utilities import log_message

GDP_ENVIRONMENT = 'test'


@pytest.fixture(scope='session')
def initialize_app_int_tests(request):
    """Create a single node application."""
    log_message("starting unit test initialisation")
    base_dir = str(Path(__file__).parent)
    output_dir = str(Path(__file__).parent.parent / "output")
    yield base_dir, output_dir
    log_message('tearing down')
    shutil.rmtree(base_dir)
    shutil.rmtree(output_dir)
