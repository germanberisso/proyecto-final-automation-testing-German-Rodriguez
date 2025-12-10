import pytest

pytest.main(["tests/", "--html=reporte.html", "--self-contained-html", "--capture=sys"])