#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 Kristian Ebdrup
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import smtplib
import tkinter as tk
from tkinter import messagebox
from time import strftime
import os
import base64

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def send_email():
    fromaddr = sender_entry.get()
    toaddr = recipient_entry.get()
    serveraddr = server_entry.get()
    usetls = tls_var.get()
    usessl = ssl_var.get()
    serverport = port_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    now = strftime("%Y-%m-%d %H:%M:%S")
    msg = "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s" % (fromaddr, toaddr, now, now)
    try:
        if usetls:
            server = smtplib.SMTP(serveraddr, serverport)
            server.starttls()
        elif usessl:
            server = smtplib.SMTP_SSL(serveraddr, serverport)
        else:
            server = smtplib.SMTP(serveraddr, serverport)
        if username and password:
            server.login(username, password)
        server.sendmail(fromaddr, toaddr, msg)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Failed to send email. Error: " + str(e))
    finally:
        server.quit()
root = tk.Tk()
root.title("SMTP Test Mail Sender")
root.geometry("550x400")
root.configure(bg='#2f2f2f')

base64_encoded = "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"
icon = tk.PhotoImage(data=base64_encoded)
root.iconphoto(True, icon)

sender_label = tk.Label(root, text="From Address:", font=("Arial", 12), bg='#2f2f2f',fg='white')
sender_label.grid(row=0, column=0, pady=10)
sender_entry = tk.Entry(root, font=("Arial", 12), width=40)
sender_entry.grid(row=0, column=1, pady=10)

recipient_label = tk.Label(root, text="To Address:", font=("Arial", 12), bg='#2f2f2f',fg='white')
recipient_label.grid(row=1, column=0, pady=10)
recipient_entry = tk.Entry(root, font=("Arial", 12), width=40)
recipient_entry.grid(row=1, column=1, pady=10)

server_label = tk.Label(root, text="SMTP Server Address:", font=("Arial", 12), bg='#2f2f2f',fg='white')
server_label.grid(row=2, column=0, pady=10)
server_entry = tk.Entry(root, font=("Arial", 12), width=40)
server_entry.grid(row=2, column=1, pady=10)

tls_var = tk.IntVar()
tls_checkbutton = tk.Checkbutton(root, text="Use TLS", variable=tls_var, font=("Arial", 12), bg='#2f2f2f',fg='white')
tls_checkbutton.grid(row=3, column=0, pady=10)

ssl_var = tk.IntVar()
ssl_checkbutton = tk.Checkbutton(root, text="Use SSL", variable=ssl_var, font=("Arial", 12), bg='#2f2f2f',fg='white')
ssl_checkbutton.grid(row=3, column=1, pady=10)

port_label = tk.Label(root, text="Server Port:", font=("Arial", 12), bg='#2f2f2f',fg='white')
port_label.grid(row=4, column=0, pady=10)
port_entry = tk.Entry(root, font=("Arial", 12), width=40)
port_entry.grid(row=4, column=1, pady=10)

username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg='#2f2f2f',fg='white')
username_label.grid(row=5, column=0, pady=10)
username_entry = tk.Entry(root, font=("Arial", 12), width=40)
username_entry.grid(row=5, column=1, pady=10)

password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg='#2f2f2f',fg='white')
password_label.grid(row=6, column=0, pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=40)
password_entry.grid(row=6, column=1, pady=10)

send_button = tk.Button(root, text="Send Email", command=send_email, font=("Arial", 12), bg='#524f4f', fg='white')
send_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
