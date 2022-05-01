import os

import mysql.connector
import pytest
from main.utilities import base
from main.utilities.common_ops import Common_Ops




@pytest.fixture(scope='class')
def init_api(request):
    base.server_url = Common_Ops.get_data('serverUrl')
    base.header = {'Content-type': Common_Ops.get_data('contentType')}


def init_DB():
    mydb = mysql.connector.connect(
        host=Common_Ops.get_data("host"),
        database=Common_Ops.get_data("databaseDB"),
        user=Common_Ops.get_data("usernameDB"),
        password=Common_Ops.get_data("passwordDB")
    )
    return mydb

