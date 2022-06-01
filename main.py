import json

import functions_framework
import pandas as pd
from flask import escape

df = pd.read_csv("./gpi.csv")
rab = 

"""{'SKU description': 
    ['E2 Instance Core running in Americas',
    'E2 Instance Core running in Japan',
    'E2 Instance Core running in Los Angeles',
    'E2 Instance Core running in Montreal',
    'E2 Instance Core running in Netherlands',
    'E2 Instance Core running in Sydney',
    'E2 Instance Core running in Virginia',
    'E2 Instance Ram running in Americas',
    'E2 Instance Ram running in Japan',
    'E2 Instance Ram running in Los Angeles',
    'E2 Instance Ram running in Montreal',
    'E2 Instance Ram running in Netherlands',
    'E2 Instance Ram running in Sydney',
    'E2 Instance Ram running in Virginia',
    'N1 Predefined Instance Core running in Americas',
    'N1 Predefined Instance Core running in Montreal',
    'N1 Predefined Instance Core running in Netherlands',
    'N1 Predefined Instance Core running in Sydney',
    'N1 Predefined Instance Core running in Virginia',
    'N1 Predefined Instance Ram running in Americas',
    'N1 Predefined Instance Ram running in Montreal',
    'N1 Predefined Instance Ram running in Netherlands',
    'N1 Predefined Instance Ram running in Sydney',
    'N1 Predefined Instance Ram running in Virginia',
    'N2 Custom Instance Core running in Americas',
    'N2 Custom Instance Ram running in Americas',
    'N2 Instance Core running in Americas',
    'N2 Instance Core running in Japan',
    'N2 Instance Core running in Netherlands',
    'N2 Instance Core running in Sydney',
    'N2 Instance Ram running in Americas',
    'N2 Instance Ram running in Japan',
    'N2 Instance Ram running in Netherlands',
    'N2 Instance Ram running in Sydney']}"""


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
    request_args=request.args
    df2 = pd.DataFrame(request_args)

    df2=df2.merge(df, on='SKU description', how='left')
    df2.drop(df2.columns.difference(['SKU description', 'List price ($)']),1,inplace=True)
    print(df2)
    
"""
for index,row in df2.iterrows():
        df.loc[index] = row
           # request_args = request.args
    if request_args and "desc" in request_args:
        id = request_args["desc"]
    else:
        id = "Cloud SQL for MySQL: Regional - 8 vCPU + 52GB RAM in Sydney"

    x = df.loc[df["SKU description"] == id, "List price ($)"]
    y = x.to_json(orient="values")
    z = json.loads(y)
    return z[0]
"""
    
    
if __name__ == "__main__":
    grabber(request)
    
