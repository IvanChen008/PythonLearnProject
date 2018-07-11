from os.path import basename
from urlparse import urlsplit
import urllib.parse

def url3name(args):
    return basename(urlsplit(url)[2])
def download(url,localFileName = None):
    localName = url3name(url)
    req = urllib3.Request(url)
    r = urllib3.urlopen()

    