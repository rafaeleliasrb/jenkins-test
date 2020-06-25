import pysftp

myHostname = "0.0.0.0"
myUsername = "foo"
myPassword = "pass"

cn_opts = pysftp.CnOpts()
cn_opts.hostkeys = None

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, port=2222, cnopts=cn_opts) as sftp:
    print ("Connection succesfully stablished ... ")

    # Switch to a remote directory
    #sftp.cwd('/var/www/vhosts/')

    print(sftp.listdir())
    
    with sftp.cd('upload'):             # temporarily chdir to public
        print(sftp.listdir())
