# lninstaller
A awesome alternative to ln command,aimed to backup your files more easily.

# Why
Very often you don't want to backup whole directory as it has big size.So,
lninstaller was created to solve this problem.

# Getting Started
## Installation

    git clone https://github.com/zgqq/lninstaller && cd lninstaller
    pip install .

## Usage
Create a file named install.py in new directory(usually located at ~/Dropbox/),
then import module 

    from lninstaller import link

use absolute path
    
    " store file, target file"
    link.link ('/home/zgq/Dropbox/system/fstab', '/etc/fstab')

use home path

    link.home_link('Dropbox/Projects/mah','Projects/mah')
    " equals "
    link.link('~/Dropbox/Projects/mah', '~/Projects/mah')

## Example

    from lninstaller import link
    def linkblog(source):
        path = 'Dropbox/Blog/zgqq.github.io/' + source
        target = 'Blog/zgqq.github.io/' + source
        link.home_link(path, target)

    linkblog('source')
    linkblog('_config.yml')
    linkblog('themes/next/_config.yml')

# How to work
lninstaller will check whether store file exists and target file exists.If both store
file and target file exist,lninstaller will move target file to /tmp and create a 
symbolic link to target file;If store file exists and target file doesn't exist,
lninstaller will create a symbolic link to target file;If both store file and target
file don't exist,lninstaller will raise error!
