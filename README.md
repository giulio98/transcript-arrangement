# transcript-arrangment

Programma che cerca fra tutte le possibili combinazioni delle materie di Eurecom
quella che massimizza la media per blocco secondo il fattore di conversione di 1.8 del
Politecnico di Torino.

In particolare
* Vengono generate tutte le possibili combinazioni di materie, dove ciascuna combinazione ha come somma totale dei crediti uguale a 25.
* A partire da tutte queste combinazioni, vengono generate delle tuple disgiunte corrispondenti ai due blocchi.
* Infine viene ritornata la tupla che massimizza la media pesata secondo il fattore di conversione di 1.8

Per calcolare la tua migliore combinazione, modifica i dizionari "subject_weight" e "subject_grade" con i pesi delle tue materie
e i voti in ventesimi.

Enjoy.
 
