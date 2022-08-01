# Tutorial Django REST Framework

## Scopul tutorialului
Scopul tutorialului este intelegerea conceptelor de API si RestAPI si a notiunilor de baza din Django/django_rest_framework cum ar fi:
ORM, modele, serializeri, view-uri, endpoint-uri, etc. Tutorialul este facut atat pentru Linux, cat si pentru Windows, astfel incat cat mai multa lume sa-l poata urma.

## Cerinte preliminare

Experienta cu python3, baze de date si cu lucrul in terminal (Windows/Linux)

## Cuvant inainte

Acest tutorial este un tutorial "prietenos" adresat tuturor developerilor de python care sunt interesati sa invete django-rest-framework.
Daca nu ati reusit sa terminati quickstart-ul de pe site-ul oficial, poate acest tutorial, ce intra mai in detaliu va poate ajuta sa intelegeti cum functioneaza acest minunat framework.
Navigarea intre filele din tutorial se poate face cu butoanele(link-urile) din josul paginii Previous/Next/Cuprins.
Codul final pentru proiect este disponibil in sectiunea src si poate fi consultat in cazul unui bugg, dar va recomand din proprie experienta sa rezolvati bugg-urile singuri, pentru a aprofunda mai multe cunostinte.

Pentru orice intrebare, va rog sa mi scrieti la adresa de email: #TODO, sau sa adaugati un issue pe github.

## Ce este un API?

API(Application Programming Interface) reprezinta un set de reguli si definitii de comunicare pentru construirea si integrarea aplicatiilor. In termeni mai simpli, un API reprezinta o interfata care ne permite sa comunicam cu un serviciu.
Cel mai simplu exemplu de API poate fi aplicatia de vreme de pe telefonul dumneavoastra, ce face **request**-uri catre server pentru a actualiza starea vremii. Deseori, in API-urilor se afla servicii foarte complexe, ce apeleaza ele insasi alte API-uri. Un alt exemplu de API poate fi reprezentat de masina. Folosind volanul si pedalele putem comunica cu masina.
In spatele acestor "manevre" insa, sunt executate calcule complexe de computer-ul masinii si diferite sisteme din el, cum ar fi sistemul ce controleaza nivelul de carburant si oxigen din motor, sistemul ce previne rotile sa se blocheze la franare (ABS), etc.
Cu aceste sisteme nu putem comunica direct, noi comunicam cu masina doar prin volan si pedale, iar restul operatiilor se intampla in spate.
Comunicarea cu aceste sisteme se desfasoara sub niste reguli prestabilite (nu putem apasa acceleratia mai adanc de podea, si nu putem intoarce volanul decat de un numar prestabilit de ori). 
API-ul reprezinta astfel o comunicare reglementata de un set prestabilit de reguli intre doua sisteme.
Mai multe detalii despre un API pot fi gasite [aici](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces)
## Ce este un REST API?

REST API(Representational State Transfer) este un stil arhitectural pentru comunicarea cu API-uri, ce foloseste request-uri de tip
HTTP pentru accesul si schimbul de date intre client si server. Arhitectura contine un set clar de reguli, ce asigura fiabilitate, performanta ridicata,
siguranta si scalabiliate sistemelor ce respecta aceste reguli. Django-rest-framework ne ofera abstractizari peste aceste reguli,
astfel ca nu vom intra in prea multe detalii, dar mai multe informatii pot fi gasite [aici](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces#soap-vs-rest) si [aici](https://aws.amazon.com/what-is/restful-api/).

## Ce este Django Rest Framework(DRF)?

DRF este un framework ce permite transferul de informatii intre o interfata si o baza de date intr-un mod simplu. Este croit pentru crearea
de servicii de tip rest si este in momentul de fata(2022) unul dintre cele mai populare framework-uri pentru backend.

![Django rest framework and the web](/images/django_rest.png)

## Termeni folositi in lucrul cu DRF

1. ### request
Un request este un mesaj transmis intre client(sau browser) si server. Request-urile sunt esentiale in transmiterea informatiei cerute,
cum ar fi primirea unei pagini web.

2. ### endpoint
Un endpoint este, in cel mai simpli termeni, un url prin care se poate face o transmitere de date. Reprezinta unul dintre capetele canalului de comunicatie dintre client si server.
3. ### client
Un client este o aplicatie (de multe ori un browser, sau un serviciu definit de noi) ce apeleaza (trimite request-uri) catre un server. 
4. ### server
Un server este un program ce asigura un serviciu pentru clienti. Acesta asteapta request-uri si le indeplineste pentru clienti.
## Cuprins

[1. Setup][1.0]

[1.1 Instalare python][1.1]

[1.2 Instalare virtualenv][1.2]

[1.3 Crearea unui virtualenv][1.3]

[1.4 Activarea virtualenv-ului si instalarea dependintelor][1.4]

[2. Init project][2.0]

[2.1 Structura unui proiect de Django][2.1]

[2.2 ]


[Next][101] | [Cuprins][102]


[1.0]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.0_setup.md
[1.1]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.1_instalare_python.md
[1.2]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.2_instalare_virtualenv.md
[1.3]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.3_creare_virtualenv.md
[1.4]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.4_instalare_dependinte.md

[101]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/beginner/setup/1.0_setup.md
[102]: https://github.com/CookiezLIT/Django-Rest-Framework-Tutorial/blob/main/README.md