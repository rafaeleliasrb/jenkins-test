import pysftp

hostname = "sftp-docker"
username = "foo"
password = "pass"
port = 22

cn_opts = pysftp.CnOpts(knownhosts='known_hosts')
#cn_opts = pysftp.CnOpts()
#cn_opts.hostkeys = None

with pysftp.Connection(host=hostname, username=username, password=password, port=port, cnopts=cn_opts) as sftp:
    print ("Connection succesfully stablished ... ")

    # Switch to a remote directory
    #sftp.cwd('/var/www/vhosts/')

    print(sftp.listdir())
    
    with sftp.cd('upload'):             # temporarily chdir to public
        print(sftp.listdir())
