import json

import functions_framework
import pandas as pd
from flask import escape

df = pd.read_csv("./gpi.csv")


@functions_framework.http
def grabber(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_args = request.args
    print(request_args["desc"])
    if request_args and "desc" in request_args:
        id = request_args["desc"]
    else:
        id = "Cloud SQL for MySQL: Regional - 8 vCPU + 52GB RAM in Sydney"

    x = df.loc[df["SKU description"] == id, "List price ($)"]
    y = x.to_json(orient="values")
    z = json.loads(y)
    return z[0]
