# Com funciona?

El funcionament del xatbot integrat al WordPress funciona connectan-lo a l'API del Google Gemini. Així respon les preguntes basades en el contingut d'un lloc web. 

El backend s'executa a Google Colab, es el que connecta amb l'API i gestiona les peticions. 

Per no tenir una sobrecarrega al servidor, té un llimit de peticions i el web scraping només funciona quan l'usuari ho demana. 
