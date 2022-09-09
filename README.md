# transcript-arrangment

Programma che cerca fra tutte le possibili combinazioni delle materie di Eurecom
quella che massimizza la media per blocco secondo il fattore di conversione di 1.8 del
Politecnico di Torino.

In particolare
* Vengono generate tutte le possibili combinazioni di materie, dove ciascuna combinazione ha come somma totale dei crediti uguale a 25.
* A partire da tutte queste combinazioni, vengono generate delle tuple disgiunte corrispondenti ai due blocchi.
* Infine vengono ritornate due possibili combinazioni: la prima massimizza la media pesata di eurecom, la seconda invece ritorna una alternativa soluzione che massimizza la media pesata dei voti del poli ma con risultati piu' calibrati tra i due blocchi.

Per calcolare la tua migliore combinazione, modifica i dizionari "subject_weight" e "subject_grade" con i pesi delle tue materie
e i voti in ventesimi.

Enjoy.
 
