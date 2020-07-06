To initiate the service, execute the following commands in your terminal:

'''
docker build -t kmeans .
docker run -it --expose 8008 -p 8080:8080  kmeans
python service.py
'''

Example queries:

'''
# Request #1:
curl -X POST --data "{\"t\": \"112.22\", \"CPU\": \"27.22\",\"RxKBTot\": \"1.78\",\"TxKBTot\": \"1.22\",\"WriteKBTot\": \"0\", \"Watts\": \"84.3\", \"Amps\": \"0.540177392\", \"RMS\": \"0.795854727\", \"diff_encoder_l\": \"12.96667\"}" http://0.0.0.0:8080/process

#Request #2:
curl -X POST --data "{\"t\": \"11112.22\", \"CPU\": \"27.22\",\"RxKBTot\": \"1.78\",\"TxKBTot\": \"1.22\",\"WriteKBTot\": \"0\", \"Watts\": \"841.3\", \"Amps\": \"0.540177392\", \"RMS\": \"1.795854727\", \"diff_encoder_l\": \"12233.96667\"}"  http://0.0.0.0:8080/process
'''
