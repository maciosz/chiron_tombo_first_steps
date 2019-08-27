W log są wszystkie komendy, które są potrzebne żeby:
- zrobić basecalling chironem
- przygotować dane do trenowania (tombo preprocess, tombo resquiggle)
- wytrenować model chirona
- zrobić basecalling chironem z własnym modelem
*Uwaga: żeby niektóre zadziałały trzeba wprowadzić zmiany w kodach źródłowych chirona i tombo.*

Model trenowałam i testowałam na odczytach faga lambda,
 tych samych, których używał chiron.
 (Basecalling testowałam też na naszych, działa).
 Są [tutaj](gigadb.org/dataset/100425) (train.tar.gz). 
 W katalogu `lambda_test` jest plik fast5 z jednym readem zrobiony z tych danych,
 wygenerowany skryptem `create_test_read.py`.
 Wrzucam też skrypty `create_test_reads.py` i `create_test_fastqs.sh`
 którymi wygenerowałam 9 readów do trenowania
 podejrzewając że może chiron nie działa bo próbuję go trenować na jednym readzie.
 (Co okazało się nieprawdą.)
 `lambda_ref.fa` to sekwencja referencyjna faga lambda, [z bazy NCBI](https://www.ncbi.nlm.nih.gov/nuccore/NC_001416.1/);
 ta sama, której używał chiron.

W `chiron` i `tombo` są skrypty z tychże pakietów, które musiałam zmodyfikować żeby działały.
 Przy samych zmianach są moje lakoniczne komentarze
 (podpisane maciosz żeby móc je znaleźć).

W `minimap_testing` jest prosty zapis testów na minimapie
 oraz odczyt, na którym je prowadziłam;
 chciałam sprawdzić, na ile jest wrażliwy na błędy / mutacje
 i jak to można zmienić parametrami.
 Próbowałam zmapować read na jego samego (czyli jedną sekwencję na sekwencję o 100%wej identyczności)
 i się nie udawało, co mnie nieco niepokoiło
 i być może wyjaśniało czemu minimap nie chce mapować naszych readów na referencję.
 Na razie nie mam wniosków z tych testów, ale ślad jest i jeszcze do tego wrócę.
