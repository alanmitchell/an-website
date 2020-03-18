#!/bin/bash
find output -type d -exec chmod 755 {} \;
find output -type f -exec chmod 644 {} \;
rsync -rlptgoDvs output/. $WEBSITE_RSYNC_DEST
