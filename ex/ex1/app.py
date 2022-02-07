from flask import Flask, render_template, request, g, Response, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        # データベースをオープンしてFlaskのグローバル変数に保存
        g.db = sqlite3.connect('chinook.db')
    return g.db

@app.route('/ex1/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        selectedTable = request.form.get('table')
        return redirect(url_for('select', selectedTable=selectedTable))
    else:
        con = get_db()
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'")
        tablename = [i[0] for i in c.fetchall() ]

        return render_template('index.html', tablename=tablename)

        
        
@app.route('/ex1/<string:selectedTable>')
def select(selectedTable):
    con = get_db()
    cur = con.execute("select * from %s" % selectedTable)
    data = cur.fetchall()
    c = con.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE TYPE='table'")
    tablename = [i[0] for i in c.fetchall() ]



    for data_cnt in range( len( data ) ) :
        cl = [ column[ 0 ] for column in cur.description ]
    columns = cl

    con.close()
    return render_template('index.html',data=data, columns=columns, selectedTable=selectedTable, tablename=tablename)


if __name__ == "__main__":
    app.run(port=8080, debug=True)




