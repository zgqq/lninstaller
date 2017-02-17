# lninstaller
A awesome alternative to ln command,aimed to backup your file more easily.

# Why
Very often you don't want to backup whole directory as it has big size.So,
lninstaller was created to solve this problem.

# Getting Started
## Installtion
git clone https://github.com/zgqq/lninstaller && cd lninstaller
pip install .

## Usage
Create a file named install.py in directory you want to backup.
then import module 

    from lninstaller import link

use absolute path
    
    link.link ('/etc/fstab','/home/zgq/Dropbox/system/fstab')

use home path

    link.home_link('Projects/mah','Dropbox/Projects/mah')
    " equal "
    link.link('~/Projects/mah','~/Dropbox/Projects/mah')

## Example

    from lninstaller import link
    def linkblog(source):
        path = 'Dropbox/Blog/zgqq.github.io/' + source
        target = 'Blog/zgqq.github.io/' + source
        link.home_link(path, target)

    linkblog('source')
    linkblog('_config.yml')
    linkblog('themes/next/_config.yml')
