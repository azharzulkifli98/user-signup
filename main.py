#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

def page_content(user, pass1, pass2, email):
    header = "<h2>SignUp</h2>"
    username = "<td><label>username</td><td><input type='type' name='user' />" + user + "</label></td>"
    password = "<td><label>password</td><td><input type='type' name='pass1'/>" + pass1 + "</label></td>"
    confirm = "<td><label>confirm password</td><td><input type='type' name='pass2'/>" + pass2 + "</label></td>"
    email = "<td><label>email (not needed)</td><td><input type='type' name='email'/>" + email + "</label></td>"
    submit = "<input type='submit' />"
    content = "<form method='post'>" + header + "<table border='0'><tr>" + username + "</tr><tr>" + password + "</tr><tr>"+ confirm + "</tr><tr>" + email + "</tr></table>" + submit + "</form>"
    return content



class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = page_content('', '', '', '')
        clean = page_header + content + page_footer
        self.response.write(clean)

    def post(self):
        user = self.request.get('user')
        password = self.request.get('pass1')
        confirm = self.request.get('pass2')
        email = self.request.get('email')
        page = page_content(user, pass1, pass2, email)
        self.response.write("<h2>Welcome to the web, " + user + "</h2>")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
