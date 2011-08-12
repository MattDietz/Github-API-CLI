import json
import sys

import httplib2

BASE_URL = 'http://github.com/api/v2/json'

class GithubAPI(object):

    def authenticate(self, username, password):
        r = httplib2.Http()
        r.add_credentials(username, password)
        return r

    def issues(self, username, password, project):
        r = self.authenticate(username, password)
        url = "%s/issues/list/%s/%s/open" %\
                (BASE_URL, username, project)
        print url
        s, c = r.request(url, method='GET')
        body = json.loads(c)
        for issue in body['issues']:
            print "Title %s" % issue['title']
            print "Filed by %s" % issue['user']
            print "Description: \n%s" % issue['body']
            print "\n"
        
if __name__ == "__main__":
    api = GithubAPI()
    getattr(api, sys.argv[1])(*sys.argv[2:])

