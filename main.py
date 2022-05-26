from flask import escape
import functions_framework
import pandas as pd
import json
df = pd.read_csv('./gpi.csv')



@functions_framework.http
def grabber(request):
    """
    This function takes in a request and returns the price of the item
    """
    request_args = request.args

    if request_args and 'SKU Description' in request_args:
        id = request_args['SKU Description']
    else:
        id = "N2 Instance Ram running in Sydney"
    return json.loads(df.loc[df['SKU description'] == id, 'List price ($)'])
