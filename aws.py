import boto3
import os, glob
access_key="AK3YBI"
access_secret="wwt2Y0zt"
dir = 'Audio'
s3_client = boto3.client('s3',
aws_access_key_id=access_key,
aws_secret_access_key = access_secret)
def s3audio():
    resp= s3_client.upload_file("Audio\\botaudio.wav",'pace20-dev-all-companies',"8/safety/observations/Bot_recordings/botaudio.wav")
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
s3audio()