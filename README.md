# Tabnabbing_POC
This repository contains POC of tabnabbing vulnerability occurs in web applications.

# Tabnabbing

Tabnabbing is an attack where a page linked from the target page is able to rewrite that page, for example to replace it with a phishing site. As the user was originally on the correct page they are less likely to notice that it has been changed to a phishing site, especially if the site looks the same as the target. If the user authenticates to this new page then their credentials (or other sensitive data) are sent to the phishing site rather than the legitimate one.

As well as the target site being able to overwrite the target page, any http link can be spoofed to overwrite the target page if the user is on an unsecured network, for example a public wifi hotspot. The attack is possible even if the target site is only available via https as the attacker only needs to spoof the http site that is being linked to.

Reference: [Tabnabbing](https://owasp.org/www-community/attacks/Reverse_Tabnabbing)

# How POC Works

- First execute `startIjectionApp.bat` file 
- Second execute `startSourceApp.bat` file 
- Once `startSourceApp.bat` file executed copy the url `127.0.0.1:8000` and paste it in browser window.
- Then login page dispalys, enter 
``` 
username : user@poc.com
password : Pass@123
```
- Once login successfull it dispalys home page, then click on tabnabbing link on top left corner.
- Once that page loaded click on any button then it redirect to new page and old link is changed to login page.
- When user try to login in agin then the credintials are goto `startInjectionApp.bat` window.

# LICENSE

Copyright (c) 2021 Devaraju Garigapati

This repository is licensed under the [MIT](https://opensource.org/licenses/MIT) license.
See [LICENSE](https://opensource.org/licenses/MIT) for details.