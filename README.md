# Phoenix Quality Platform

Progetto pratico di test automation, Docker e CI/CD.

## Obiettivi

- Automatizzare test API e interfaccia web.
- Creare un ambiente riproducibile con Docker.
- Eseguire i test tramite GitHub Actions.
- Collegare requisiti, test e risultati.

## Ambiente Python

Creare l'ambiente virtuale:
python3 -m venv .venv

Attivare l'ambiente virtuale:
source .venv/bin/activate

## Installare le dipendenze di sviluppo

Con l'ambiente virtuale attivo:
python -m pip install -r requirements-dev.txt

## Eseguire i test

python -m pytest -v

## Quality gate

Il rilascio è consentito se è stato eseguito almeno un test
e nessun test è fallito.
