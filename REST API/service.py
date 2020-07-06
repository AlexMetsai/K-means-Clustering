# Alexandros Metsai
# alexmetsai@gmail.com

import bottle
import json
from inference import inference

@bottle.route('/process', method='POST')
def process():
    # Get input features.
    try:
        body = str(bottle.request.body.read())[2:-1]
        body_dict = json.loads(body)
    except:
        return bottle.HTTPResponse(body='Wrong body format.', status=400)
    
    # Classify the input.
    try:
        output = inference(body_dict)
        print(output)
        return bottle.HTTPResponse(body=output+'\n', status=200)
    except:
        return bottle.HTTPResponse(body='Error during classification.\n', status=400)

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port='8080')
