#!/usr/bin/env bash

password="cogrobucsd23!"
username="cogrob_admin"
dir_origin="docs/*"
dir_destination="/home/cogrob_admin/cogrob.org/"
Ip="ps136143.dreamhostps.com"

echo "Uploading files to remote server...."
sshpass -p "$password" rsync --progress -avz -e "ssh -o StrictHostKeyChecking=no" $dir_origin $username@$Ip:$dir_destination
echo "File upload to remote server completed! ;)"
echo $(ls docs)