from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def render_toolbox():
    return render_template('toolbox.html')
@app.route('/rstudio')
def launch_rstudio():
    return redirect("http://localhost:8787", code=302)
@app.route('/ibmsas')
def launch_sas():
    return redirect("https://welcome.oda.sas.com/login", code=302)
@app.route('/git')
def launch_git():
    return redirect("http://localhost:3000", code=302)
@app.route('/jupyter')
def launch_jupyter():
    return redirect("http://localhost:8888?token=test", code=302)
@app.route('/orange')
def launch_orange():
    return redirect("http://localhost:6901", code=302)
@app.route('/vscode')
def launch_vscode():
    return redirect("http://localhost:8080", code=302)
@app.route('/hadoop')
def launch_hadoop():
    return redirect("http://localhost:50070", code=302)
@app.route('/spark')
def launch_spark():
    return redirect("http://localhost:8887?token=test", code=302)
@app.route('/tableau')
def launch_tableau():
    return redirect("https://sso.online.tableau.com/public/idp/SSO", code=302)
@app.route('/sonar')
def launch_sonar():
    return redirect("http://localhost:9000", code=302)    
@app.route('/tensor')
def launch_tensor():
    return redirect("http://localhost:8889?token=test", code=302)
@app.route('/markdown')
def launch_markdown():
    return redirect("http://localhost:12345", code=302)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')