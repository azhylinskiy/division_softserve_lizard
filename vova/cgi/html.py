#!/usr/bin/env python

def p(text):
    return '<p>%s</a>' % text


def a(ref, text):
    return '<a href=%s>%s</a>' % (ref, text)

def doc(body):
    return """<!DOCTYPE html>
        <html>
        <body>
        %s
        </body>
        </html>""" % body

def table(data):
    return """<table border="1">
        %s
        </table>""" % data

def tr(row):
    return "<tr>%s</tr>" % row


