# pwauth

Forked version of pwauth with ClearOS changes applied

## Update usage
  Add __#kojibuild__ to commit message to automatically build

* git clone git+ssh://git@github.com/clearos/pwauth.git
* cd pwauth
* git checkout master
* git remote add upstream git://pkgs.fedoraproject.org/pwauth.git
* git pull upstream master
* git checkout clear7
* git merge --no-commit master
* git commit
