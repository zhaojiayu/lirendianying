# -*-coding:utf-8-*-

import web
import mysql

render = web.template.render('templates/')   

class Index:
    def GET(self):
        temp = mysql.Select()
	movie = temp.GetDataOld()
        name = ('test1','test2')
        return render.daily(movie)
