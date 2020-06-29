import pysftp
import glob
import os
import pandas as pd

def createLocalDirectory():
    local_path = 'local-backup'
    if not os.path.exists(local_path):
        os.mkdir(local_path)

def downloadCSVFilesFromSFTP():
    hostname = os.environ['SFTP_HOSTNAME']
    username = os.environ['SFTP_USERNAME']
    password = os.environ['SFTP_PASSWORD']
    port = os.environ['SFTP_PORT']

    cn_opts = pysftp.CnOpts()
    cn_opts.hostkeys = None
    with pysftp.Connection(host=hostname, username=username, password=password, port=int(port), cnopts=cn_opts) as sftp:
        sftp.get_d('upload', local_path, preserve_mtime=True)

def concatCSVFilesIntoNewCSV():
    all_files = glob.glob(os.path.join(local_path, "*.csv"))
    df_concat_report = pd.concat((pd.read_csv(f, delimiter = ';') for f in all_files))
    df_concat_report.to_csv(os.path.join(local_path, 'cancel_report.csv'), index = False, header=True, sep=";")

if __name__ == "__main__":
    createLocalDirectory()
    downloadCSVFilesFromSFTP()
    concatCSVFilesIntoNewCSV()
