import pysftp
import glob
import os
import pandas as pd
import socket

local_path = 'local-backup'
if not os.path.exists(local_path):
    os.mkdir(local_path)

ip_address = socket.gethostbyname(os.environ['SFTP_HOSTNAME'])
print(ip_address)

hostname = os.environ['SFTP_HOSTNAME']
username = os.environ['SFTP_USERNAME']
password = os.environ['SFTP_PASSWORD']
port = os.environ['SFTP_PORT']

cn_opts = pysftp.CnOpts()
cn_opts.hostkeys = None
with pysftp.Connection(host=hostname, username=username, password=password, port=port, cnopts=cn_opts) as sftp:
    sftp.get_d('upload', local_path, preserve_mtime=True)

all_files = glob.glob(os.path.join(local_path, "*.csv"))
df_concat_report = pd.concat((pd.read_csv(f, delimiter = ';') for f in all_files))

df_concat_report.to_csv(os.path.join(local_path, 'cancel_report.csv'), index = False, header=True, sep=";")
