import pysftp
import glob
import os
import pandas as pd

DIRECTORY = os.environ['DIRECTORY']

def createLocalDirectory():
    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

def downloadCSVFilesFromSFTP():
    cn_opts = pysftp.CnOpts()
    cn_opts.hostkeys = None
    with pysftp.Connection(host=os.environ['SFTP_HOSTNAME'], username=os.environ['SFTP_USERNAME'], password=os.environ['SFTP_PASSWORD'], 
                           port=int(os.environ['SFTP_PORT']), cnopts=cn_opts) as sftp:
        sftp.get_d('upload', DIRECTORY, preserve_mtime=True)

def concatCSVFilesIntoNewCSV():
    all_files = glob.glob(os.path.join(DIRECTORY, "*.csv"))
    df_concat_report = pd.concat((pd.read_csv(f, delimiter = ';') for f in all_files))
    df_concat_report.to_csv(os.environ['FTP_FILE'], index = False, header=True, sep=";")

if __name__ == "__main__":
    createLocalDirectory()
    downloadCSVFilesFromSFTP()
    concatCSVFilesIntoNewCSV()
