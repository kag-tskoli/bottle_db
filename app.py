pwd = 'yourpasswordhere'

from bottle import *
import pymysql

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
c = conn.cursor()

#c.execute('INSERT INTO bilar Values("CD-345", "Suzuki Swift (Dökkgrár)", "MBHGYUSKD343", "2016-06-10", 50, 1200, "2020-06-10", "Í umferð")')
#conn.commit()

#c.execute('DELETE from bilar where skraningarnumer = "CD-345"')
#conn.commit()

#c.execute('UPDATE bilar SET stada="Í umferð" WHERE skraningarnumer = "AB-123"')
#conn.commit()

c.execute('SELECT * FROM bilar')
records = c.fetchall()

conn.close()
c.close()

print(records)

@route('/')
def index():
    return template('index')

@route('/car')
def car():
    nr = request.query.get('leita')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar where skraningarnumer = %s', (nr))
    bill = c.fetchone()

    conn.close()
    c.close()

    if bill:
        return template('car', bill=bill)
    else:
        return 'Skráningarnúmer ekki í grunni. <br> <a href="/">Til baka</a>'

@route('/db/add')
def add_record():
    return template('newcar')

@route('/db/add', method='post')
def submit_record():
    skr_nr = request.forms.get('skr_nr')
    tegund = request.forms.tegund
    vrk_nr = request.forms.get('vrk_nr')
    skr_dags = request.forms.get('skr_dags')
    co2 = request.forms.get('co2')
    tyngd = request.forms.get('tyngd')
    sko_dags = request.forms.get('sko_dags')
    stada = request.forms.stada

    co2 = int(co2)
    tyngd = int(tyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar')
    records = c.fetchall()

    if any(skr_nr in r for r in records):
        conn.close()
        c.close()
        return 'Skráningarnúmer þegar í grunni. <br> <a href="/">Til baka</a>'
    else:
        #c.execute('INSERT INTO bilar Values(%s, %s, %s, %s, %s, %s, %s, %s)',(skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada))
        c.execute(
            "Insert into bilar values('{}','{}','{}','{}','{:d}','{:d}','{}','{}')".format(skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada))

        conn.commit()
        conn.close()
        c.close()
        return redirect('/')

@route('/db/del/<nr>')
def del_record(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
    c = conn.cursor()

    c.execute('DELETE from bilar where skraningarnumer = %s', (nr))
    conn.commit()

    conn.close()
    c.close()

    return redirect('/')

@route('/db/update/<nr>')
def update_record(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar where skraningarnumer = %s', (nr))
    bill = c.fetchone()

    conn.close()
    c.close()

    return template('updatecar', bill=bill)

@route('/db/update', method="post")
def submit_update():
    skr_nr = request.forms.get('skr_nr')
    tegund = request.forms.tegund
    vrk_nr = request.forms.get('vrk_nr')
    skr_dags = request.forms.get('skr_dags')
    co2 = request.forms.get('co2')
    tyngd = request.forms.get('tyngd')
    sko_dags = request.forms.get('sko_dags')
    stada = request.forms.stada

    co2 = int(co2)
    tyngd = int(tyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kag', passwd=pwd, db='kag_test')
    c = conn.cursor()

    #c.execute('UPDATE bilar SET skraningarnumer=%s, tegund=%s, verksmidjunumer=%s, skraningardagur=%s, co2=%s, þyngd=s%, skodun=%s, stada=%s WHERE skraningarnumer=%s', (skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada, skr_nr))
    c.execute(
        "Update bilar set skraningarnumer='{}', tegund='{}', verksmidjunumer='{}',skraningardagur='{}',co2='{:d}',þyngd='{:d}',skodun='{}',stada='{}' where skraningarnumer='{}'".format(
            skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada, skr_nr))

    conn.commit()

    conn.close()
    c.close()

    return redirect('/')

run()