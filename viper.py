#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Erdog

import requests
import json
import sys
import argparse
import hashlib
import argparse

from configparser import ConfigParser


class Viper():
    """
    Viper
    """
    def __init__(self, url='', token=''):
        """
        init

        Args:
            url (str, optional): viper-web url. Defaults to ''.
            token (str, optional): token of viper user. Defaults to ''.
        """
        super().__init__()
        self.url = url
        self.token = token
        self.header = {"Authorization": "Token {}".format(token)}
        self.debug = False
        self.proxies = None

    def init_from_file(self, file='config.ini'):
        """
        Init Viper Class args from a Config file

        Args:
            file (str, optional): config file path. Defaults to 'config.ini'.
        """
        cfp = ConfigParser()
        cfp.read(file)
        host = cfp.get('viper-web', 'host')
        port = cfp.get('viper-web', 'port')
        token = cfp.get('viper-web', 'token')
        self.token = token
        self.url = "http://{}:{}".format(host, port)
        self.header = {"Authorization": "Token {}".format(token)}

    def upload(self, samplepath, filename=None, tags='', project='default'):
        """
        Upload Sample by multipart/form-data post requests
        
        Args:
            samplepath (str): Sample path
            filename (str): Name for Sample. Defaults by filepath
            tags (str): Tags for Sample (comma separated). Defaults to ''.
            project (str, optional): Project name. Defaults to 'default'.
        """

        path = "/api/v3/project/{}/malware/upload/".format(project)
        url = self.url + path

        data = {'tag_list': tags} if tags else None
        filename = filename if filename else samplepath.split('/')[-1]

        with open(samplepath, 'rb') as f:
            params = {"file": (filename, f, 'text/plain')}
            res = requests.post(url,
                                data=data,
                                files=params,
                                headers=self.header,
                                timeout=120,
                                proxies=self.proxies)
        if self.debug:
            print(res.request.headers)
            # print(res.request.body)
            print(res.text)

        return res.json

    def add_tag(self, sha256, tag):
        """
        Add a tag to Sample

        Args:
            sha256 (str): sha256 of sample to add tag
            tag (str): tag
        """

        path = "/api/v3/project/default/malware/{}/tag/".format(sha256)
        url = self.url + path
        payload = {"tag": tag}

        res = requests.post(url,
                            headers=self.header,
                            data=payload,
                            proxies=self.proxies)

        if self.debug:
            print(res.request.headers)
            print(res.text)

        return res.json

    @staticmethod
    def get_sha256(file):
        """
        Get SHA256 of file

        Args:
            file (str): file path

        Returns:
            sha256: sha256
        """
        with open(file, "rb") as f:
            bytes = f.read()
            sha256 = hashlib.sha256(bytes).hexdigest()
            return sha256


def main():
    viper = Viper()
    viper.init_from_file(args.config)
    viper.debug = args.debug
    viper.upload(args.file, tags=args.tags, project=args.project)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-f',
                        '--file',
                        type=str,
                        required=True,
                        help='Select upload file')
    parser.add_argument('-t',
                        '--tags',
                        type=str,
                        default='',
                        help='Tags for Sample (comma separated)')
    parser.add_argument('-p',
                        '--project',
                        type=str,
                        default="default",
                        help='Project for Sample')
    parser.add_argument('-c',
                        '--config',
                        type=str,
                        default="config.ini",
                        help='Config file for Viper')
    parser.add_argument("-d",
                        "--debug",
                        action="store_true",
                        help="Debug model")
    args = parser.parse_args()

    main()