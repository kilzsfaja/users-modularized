from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'fullstackmofo123'