
# asnx
A useful script to gather ASNs and prefixes of your target, while you are doing a wide recon process.
This tool gathers *IPs* or *subdomains* as input and will provide prefixes and ASNs of them as output.

![asnx](https://github.com/AliSh3ikhi/asnx/assets/77098341/878bbf17-a5a6-472e-ab7b-9e1b3b3c0d52)

**Table of Usage**
| Options   | Descriptions              |
|----------|----------------------------|
| -h       | Show this lovely help menu |
| -u       | Single url or IP           |
| -l       | List of urls or IPs        |
| -asn     | Only show ASNs             |
| -prefix  | Only show prefixes         |

**Example**
```
 asnx -u alish3ikhi.com
 ```
 > Result:
```
[+] 104.111.216.130:
{
  "prefix": "104.111.216.0/22",
  "ASN": 16625
}
{
  "prefix": "104.64.0.0/10",
  "ASN": 20940
}
```
**Other Example**
```
asnx -u 8.8.4.4
```
```
asnx -l list.txt
```

**Example of `--asn`**
```
asnx -l list.txt --asn
```
![asnx2](https://github.com/AliSh3ikhi/asnx/assets/77098341/9015df87-ed20-4321-8153-3e25e434f476)

**Example of `--prefix`**
```
asnx -l list.txt --prefix
```
![asnx3](https://github.com/AliSh3ikhi/asnx/assets/77098341/39bb047e-6c85-47c8-8f9a-55d63d32dcc7)

Happy hunting :)
