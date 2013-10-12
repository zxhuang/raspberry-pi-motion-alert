#!/usr/bin/env python
"""
Copyright (c) 2013, Zeke Huang
All rights reserved.
https://github.com/zxhuang/raspberry-pi-motion-alert
"""

import os.path
import gdata.data
import gdata.docs.client

def gd_avi_upload(username, password, to_folder, avideo):
    gd = gdata.docs.client.DocsClient(source='motion')
    gd.http_client.debug = False
    gd.client_login(username, password, service=gd.auth_service, source=gd.source)

    d = None
    for folder in gd.GetAllResources(uri='/feeds/default/private/full/-/folder'):
        if folder.title.text == to_folder:
            d = gdata.docs.data.Resource(type='video', title=os.path.basename(avideo))
            media = gdata.data.MediaSource()
            media.SetFileHandle(avideo, 'video/avi')
            d = gd.CreateResource(d, media=media, collection=folder) 
            break

    link = None
    for l in d.link:
        if 'video.google.com' in l.href:
            link = l.href

    return link




##########################
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Upload avi video to Google Drive.')
    parser.add_argument('--username', required=True, help='Google Drive username')
    parser.add_argument('--password', required=True, help='Google Drive password')
    parser.add_argument('--to_folder', required=True, help='Upload to folder')
    parser.add_argument('--avideo', required=True, help='AVI video file path')
    args = parser.parse_args()

    gd_avi_upload(**vars(args))


