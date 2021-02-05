# HTML Injection Scanner

Description: 

Simple Html Injection Scanner for Web Applications with the intent of automatic testing.

Git Clone:
  
     wget https://github.com/Gaurav-Jadhav/htmlinjection.git
     cd htmlinjection


Specific scanning:

If you want to scan only for specific URL(for example, http://testphp.vulnweb.com/listproducts.php?cat=2), you can simply try the following:

     $ python3.6 html_inj.py -d "testphp.vulnweb.com" -url 'http://testphp.vulnweb.com/listproducts.php?cat=2'

If you want to scan list of urls file ,you can simply try the following:

     $ python3.6 html_inj.py -d "testphp.vulnweb.com" -ul urls.txt

