# HTML Injection Scanner

Description: 

Simple Html Injection Scanner for Web Applications with the intent of automatic testing.

Git Clone:
  
     git clone https://github.com/Gaurav-Jadhav/htmlinjection.git
     cd htmlinjection


Arguments:

    -url   = Plase enter valid URL example: http://testphp.vulnweb.com/listproducts.php?cat=2
    -ul    = Plase provide URL List File, filename.txt
    -d     = Domain Name example: testphp.vulnweb.com



Specific scanning:

If you want to scan only for specific URL(for example, http://testphp.vulnweb.com/listproducts.php?cat=2), you can simply try the following:

     python3.6 html_inj.py -d "google-gruyere.appspot.com"  -url 'https://google-gruyere.appspot.com/618330416163754376309156278800266650779/snippets.gtl?uid=brie'


If you want to scan list of urls file ,you can simply try the following:

     python3.6 html_inj.py -d "google-gruyere.appspot.com" -ul googl-gru.txt
