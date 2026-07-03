
logs = [
    "192.168.0.1 - 2023-10-01 - /index.html - 200",
    "192.168.0.2 - 2023-10-01 - /about.html - 404",
    "192.168.0.1 - 2023-10-01 - /contact.html - 200",
    "192.168.0.3 - 2023-10-01 - /index.html - 200",
    "192.168.0.1 - 2023-10-01 - /index.html - 200"
]
list = []

for i in logs:
    ip, date, url, code_ans = i.split(' - ')
    code_ans = int(code_ans)

    if code_ans == 200:
        list.append((ip, url))
    else:
        continue

ip_count = {}
url_count = {}

for ip, url in list:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

    if url in url_count:
        url_count[url] += 1
    else:
        url_count[url] = 1


most_active_ip = max(ip_count, key = ip_count.get)
most_requested_url = max(url_count, key = url_count.get)

print(f'most_active_ip: {most_active_ip}')
print(f'most_requested_url: {most_requested_url}')





succesful_ips = []
succesful_urls = []

for log in logs:
    parts = log.split(' - ')

    ip = parts[0]
    url = parts[2]
    status_code = parts[3]

    if status_code == '200':
        succesful_ips.append(ip)
        succesful_urls.append(url)

most_active_ip = None
max_ip_count = 0

for ip in succesful_ips:
    ip_count = succesful_ips.count(ip)

    if ip_count > max_ip_count:
        max_ip_count = ip_count
        most_active_ip = ip

most_requared_url = None
max_url_count = 0

for url in succesful_urls:
    url_count = succesful_urls.count(url)

    if url_count > max_url_count:
        max_url_count = url_count
        most_requared_url = url


print(most_active_ip)
print(most_requared_url)