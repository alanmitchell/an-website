# an-website
Analysis North Website

Edit files in the `content` directory. To build the website, make sure the Python 
packages `pelican` and `Markdown` are installed, and run the command:

    pelican

from the root directory, which will place needed HTML/CSS/JS files in the 
output/ directory.

To upload files to the website, make sure the following environment variable
is set:

    export WEBSITE_RSYNC_DEST="<user>@<website host>:<destination directory ending w/ slash>"

In my case, the destination directory is `web@analysisnorth.com:/home/web/html/`.  Then run:

    ./upload_site.sh

while in the root directory.
