import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        if 'name' in req_body:
            cake_name = req_body['name']
            # put to queue
            msg.set(json.dumps(req_body))
            return func.HttpResponse(f"I put your cake, {cake_name} into processing.", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"I can not bake your cake yet", status_code=400)
