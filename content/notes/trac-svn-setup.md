Title: Trac setup on SVN server
Date: 2014-05-27
Category: Notes
Tags: trac, svn, self-hosted
Author: Wray Mills
Summary: Trac/SVN server setup documentation

This entry documents the setup for a new project/group setup when using self-hosted SVN in lieu of github.

We are using a server that hosts both SVN as well as several trac instances. This server resides within our internal restricted network. We'll refer to the trac/svn server as trac-1.

SVN -
~~~~~~
sudo svnadmin create in /Users/svn
sudo chgrp -R _www # for Apache svn service access
sudo chmod -R g+w
~~~~~~

Add permissions for developers in ${app_root}/.svn_authz

Can access via https://${trac-1.domain}/scc/${new_project} # via apache proxy connecting to specific trac instance port.

Then, you can do an svn import -m "initial import"

Trac - (now up to version 1.0.1)

~~~~~~
trac-admin ${app_root}/${new_project}-trac initenv
trac-admin ${app_root}/${new_project}-trac permission add ${admin_user} TRAC_ADMIN
~~~~~~

Adjust trac.conf for:

* attachment size
* email settings (including default notification settings)
* svn settings! (Trac 1.0.1 does not favor or default to svn, so the svn modules need to be turned on in the conf file before you can set the repository in the interface). There is a link I should add here.

Immediately go in and adjust permissions to give unauthenticated none

Re-arrange permissions to give authenticated a rather large set of permissions (use another project as a template).

Configure the default repository.

Launch on specific port (add to crontab @reboot) -
~~~~~~
tracd -s -- port ${project_port} --auth=${new_project} trac,${app_root}/.htdigest,'${new_project}' --base-path=${app_root}/${new_project}-trac
~~~~~~

Finally, add users to the htdigest, update their name and email and notify them of their new credentials.


