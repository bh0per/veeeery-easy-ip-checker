import tkinter as tk
import socket
import requests

def get_ip_info():
    ip_address = entry.get()
    try:
        # Clear the previous output
        output.delete('1.0', tk.END)

        # Get basic information about the IP address
        info = socket.getaddrinfo(ip_address, None)
        output.insert("end", f"IP version: {info[0][0]}\n")
        output.insert("end", f"Address type: {info[0][1]}\n")
        output.insert("end", f"Protocol: {info[0][2]}\n")
        output.insert("end", f"Canonical name: {info[0][3]}\n")
        output.insert("end", f"Socket address: {info[0][4]}\n\n")

        # Get more detailed information using an external API
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        data = response.json()
        output.insert("end", f"City: {data['city']}\n")
        output.insert("end", f"Region: {data['region']}\n")
        output.insert("end", f"Country: {data['country']}\n")
        output.insert("end", f"Zip code: {data['postal']}\n")
        output.insert("end", f"Timezone: {data['timezone']}\n")
        output.insert("end", f"ISP: {data['org']}\n")
    except Exception as e:
        output.insert("end", f"Error: {e}\n")

root = tk.Tk()
root.title("IP Address Info")

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Get Info", command=get_ip_info)
button.pack()

output = tk.Text(root, width=80, height=20)
output.pack()

root.mainloop()