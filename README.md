# Applicazione di Login con Flask e Verifica OTP

Questa è una semplice applicazione Flask che implementa un sistema di login di base e verifica OTP (One-Time Password). L'applicazione è costruita utilizzando il framework Flask e utilizza l'estensione Flask-Mail per l'invio di email.

## Funzionalità

- **Login:** Gli utenti possono inserire il loro nome utente e password per accedere all'applicazione.
- **Generazione OTP:** Dopo un login riuscito, viene generato un codice OTP casuale e inviato all'indirizzo email dell'utente.
- **Verifica OTP:** Gli utenti sono invitati ad inserire il codice OTP ricevuto via email per verificare la propria identità.
- **Pagina di Successo:** Se il codice OTP inserito corrisponde al codice generato, viene visualizzata una pagina di successo, indicando una verifica riuscita.
- **Gestione degli Errori:** L'applicazione fornisce messaggi di errore appropriati per credenziali non valide e codici OTP incorretti.

## Istruzioni di Configurazione

Per eseguire questa applicazione in locale o distribuirla su un server, segui questi passaggi:

1. Clona il repository nella tua macchina locale:

   ```
   git clone https://github.com/tuo-nomeutente/tua-repository.git
   ```

2. Installa le dipendenze richieste eseguendo il seguente comando nella directory del progetto:

   ```
   pip install -r requirements.txt
   ```

3. Configura l'applicazione modificando le seguenti variabili nel file `app.py`:

   - `SECRET_KEY`: Imposta una chiave segreta sicura per l'applicazione Flask.
   - `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`: Specifica i dettagli del server SMTP e le credenziali dell'email.
   - `MAIL_USE_TLS`, `MAIL_USE_SSL`: Scegli se utilizzare TLS o SSL per la comunicazione email.

4. Avvia l'applicazione eseguendo il seguente comando:

   ```
   python app.py
   ```

5. Apri un browser web e accedi all'applicazione all'indirizzo [http://localhost:5000](http://localhost:5000).

## Utilizzo

1. Nella pagina di accesso, inserisci le seguenti credenziali:

   - **Nome utente:** latuamail.com
   - **Password:** 1234

2. Dopo un accesso riuscito, verrà generato un codice OTP e inviato all'indirizzo email fornito.

3. Passa al tuo client di posta elettronica e controlla se è presente un'email dall'applicazione.

4. Torna all'applicazione e inserisci il codice OTP ricevuto nella pagina di verifica.

5. Se il codice OTP inserito corrisponde al codice generato, verrà visualizzata una pagina di successo.

## Nota

- Questa applicazione è solo a scopo dimostrativo e non dovrebbe essere utilizzata in un ambiente di produzione senza ulteriori miglioramenti della sicurezza.

Sentiti libero di esplorare e modificare l'applicazione in base alle tue esigenze.
