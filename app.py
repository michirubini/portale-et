# TINDET 

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Dizionario di utenti con le loro password (da sostituire con un sistema di autenticazione più sicuro)

users = {
    'admin': 'password1',  # Aggiungi qui il nome utente e la password
    'utente2': 'password2',
    # Aggiungi gli altri utenti qui
}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            if username in users and users[username] == password:
                user = User(username)
                login_user(user)
                flash('Login effettuato con successo!', 'success')  # Aggiungi un messaggio di successo
                return redirect(url_for('index'))
            else:
                flash('Credenziali non valide. Riprova.', 'error')  # Aggiungi un messaggio di errore
        else:
            flash('Campi mancanti nel modulo.', 'error')  # Aggiungi un messaggio di errore per campi mancanti
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout effettuato con successo!', 'success')  # Aggiungi un messaggio di successo
    return redirect(url_for('index'))

venditori = {
    "Mirko": {
        "nuova_km0": 7, "semestrale_aziendale": 7, "usata": 10, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },
    
    "Francesco": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Diego": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Rossano": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Mario": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Samuele": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Simone": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    },

    "Valentina": {
        "nuova_km0": 0, "semestrale_aziendale": 0, "usata": 0, 
        "finanziamento_si": 0, "finanziamento_no": 0, 
        "permuta_si": 0, "permuta_no": 0, 
        "pieve_di_cento": 0, "25_km": 0, "bologna_modena_ferrara": 0, 
        "18_28": 0, "29_39": 0, "40_50": 0, "51_61": 0, "62+": 0, 
        "idee_chiare": 0, "multimarca": 0, 
        "uomo": 0, "donna": 0, 
        "utilitaria": 0, "suv": 0, "berlina": 0, 
        "0_10": 0, "11_21": 0, "22_32": 0, "33_43": 0, "44+": 0,
    }

}

# Funzione per calcolare il punteggio del venditore in base alle preferenze del cliente
def calcola_punteggio_venditore(venditore, cliente):
    punteggio = 0
    if cliente["tipo"] == "nuova_km0":
        punteggio += venditore["nuova_km0"]

    elif cliente["tipo"] == "semestrale_aziendale":
        punteggio += venditore["semestrale_aziendale"]

    elif cliente["tipo"] == "usata":
        punteggio += venditore["usata"]
    
    if cliente["finanziamento"] == "finanziamento_si":
        punteggio += venditore["finanziamento_si"]

    elif cliente["finanziamento"] == "finanziamento_no":
        punteggio += venditore["finanziamento_no"]
    
    if cliente["permuta"] == "permuta_si":
        punteggio += venditore["permuta_si"]

    elif cliente["permuta"] == "permuta_no":
        punteggio += venditore["permuta_no"]

    if cliente["zona"] == "pieve_di_cento":
        punteggio += venditore["pieve_di_cento"]

    elif cliente["zona"] == "25_km":
        punteggio += venditore["25_km"]
        
    elif cliente["zona"] == "bologna_modena_ferrara":
        punteggio += venditore["bologna_modena_ferrara"]

    if cliente["età"] == "18_28":
        punteggio += venditore["18_28"]

    elif cliente["età"] == "29_39":
        punteggio += venditore["29_39"]

    elif cliente["età"] == "40_50":
        punteggio += venditore["40_50"]

    elif cliente["età"] == "51_61":
        punteggio += venditore["51_61"]

    elif cliente["età"] == "62+":
        punteggio += venditore["62+"]

    if cliente["consulenza"] == "idee_chiare":
        punteggio += venditore["idee_chiare"]

    elif cliente["consulenza"] == "multimarca":
        punteggio += venditore["multimarca"]

    if cliente["sesso"] == "uomo":
        punteggio += venditore["uomo"]

    elif cliente["sesso"] == "donna":
        punteggio += venditore["donna"]

    if cliente["segmento"] == "utilitaria":
        punteggio += venditore["utilitaria"]

    elif cliente["segmento"] == "suv":
        punteggio += venditore["suv"]

    elif cliente["segmento"] == "berlina":
        punteggio += venditore["berlina"]

    if cliente["budget"] == "0_10":
        punteggio += venditore["0_10"]

    elif cliente["budget"] == "11_21":
        punteggio += venditore["11_21"]

    elif cliente["budget"] == "22_32":
        punteggio += venditore["22_32"]
    
    elif cliente["budget"] == "33_43":
        punteggio += venditore["33_43"]

    elif cliente["budget"] == "44+":
        punteggio += venditore["44+"]

    return punteggio

# Cliente con le sue preferenze. INSERIRE QUI SOTTO LA RICHIESTA DEL CLIENTE
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        cliente = {
            "tipo": request.form["tipo"],
            "finanziamento": request.form["finanziamento"],
            "permuta": request.form["permuta"],
            "zona": request.form["zona"],
            "età": request.form["età"],
            "consulenza": request.form["consulenza"],
            "sesso": request.form["sesso"],
            "segmento": request.form["segmento"],
            "budget": request.form["budget"],
        }

        venditori_ordinati = []

        for venditore, punteggi in venditori.items():
            punteggio_venditore = calcola_punteggio_venditore(punteggi, cliente)
            venditori_ordinati.append((venditore, punteggio_venditore))

        venditori_ordinati.sort(key=lambda x: x[1], reverse=True)

        return render_template("risultato.html", venditori=venditori_ordinati)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)











