import logging

import azure.functions as func


def main(msg1: func.QueueMessage, msgout:  func.Out[str]) -> None:
    body = msg1.get_body().decode('utf-8')
    logging.info('Python queue trigger function processed a queue item: %s',
                 body)
    msgout.set('cake is ready')