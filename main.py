
import webapp2
import cgi
import re



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)
PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASSWORD_RE.match(password)
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)


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
    password = "<td><label>password</td><td><input type='password' name='pass1'/>" + pass1 + "</label></td>"
    confirm = "<td><label>confirm password</td><td><input type='password' name='pass2'/>" + pass2 + "</label></td>"
    email = "<td><label>email (not needed)</td><td><input type='type' name='email'/>" + email + "</label></td>"
    submit = "<input type='submit' />"
    content = "<form method='post'>" + header + "<table border='0'><tr>" + username + "</tr><tr>" + password + "</tr><tr>"+ confirm + "</tr><tr>" + email + "</tr></table>" + submit + "</form>"
    return content



class MainHandler(webapp2.RequestHandler):
    def get(self):
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""
        content = page_content('', '', '', '') + error_element
        clean = page_header + content + page_footer
        self.response.write(clean)

    def post(self):
        user = cgi.escape(self.request.get('user'))
        password = cgi.escape(self.request.get('pass1'))
        confirm = cgi.escape(self.request.get('pass2'))
        email = cgi.escape(self.request.get('email'))
        content = page_content(user, password, confirm, email)
        clean = page_header + content + page_footer


        if not valid_email(email) and email != "":
            error = "invalid email provided"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if not valid_password(password):
            error = "invalid password"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if password != confirm:
            error = "passwords don't match"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if len(password) < 4:
            error = "invalid password"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if password == "":
            error = "please provide a password"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if not valid_username(user):
            error = 'invalid username'
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")


        if len(user) < 3:
            tap = str(valid_username('user'))
            error = 'username too short'
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        if user == "":
            error = "please give a username"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect('/?error=' + "<h2 class='error'>" + error_escaped + "</h2>")

        self.response.write("<h2>Welcome to the web, " + user + "</h2>")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
