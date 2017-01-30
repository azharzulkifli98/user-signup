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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = """
        <h2>SignUp</h2>
        """
        username = """<label>username<input type="type" /></label>"""
        password = """<label>password<input type="type" /></label>"""
        confirm = """<label>confirm password<input type="type" /></label>"""
        email = """<label>email (not needed)<input type="type" /></label>"""
        submit = """<input type="submit" />"""
        content = "<form method='post'>" + header + username + "<br>" + password + "<br>" + confirm + "<br>" + email + "<br>" + submit + "</form>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
