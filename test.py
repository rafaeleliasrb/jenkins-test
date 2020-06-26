import pysftp
import glob
import os
import pandas as pd

local_path = 'local-backup'
if not os.path.exists(local_path):
    os.mkdir(local_path)

hostname = "172.20.0.4"
username = "foo"
password = "pass"
port = 22

cn_opts = pysftp.CnOpts()
cn_opts.hostkeys = None
with pysftp.Connection(host=hostname, username=username, password=password, port=port, cnopts=cn_opts) as sftp:
    sftp.get_d('upload', local_path, preserve_mtime=True)

all_files = glob.glob(os.path.join(local_path, "*.csv"))
df_concat_report = pd.concat((pd.read_csv(f, delimiter = ';') for f in all_files))

df_concat_report.to_csv(os.path.join(local_path, 'cancel_report.csv'), index = False, header=True, sep=";")
