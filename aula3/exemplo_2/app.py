from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Verificando as variáveis
    i = 1 # Define a variável como interira
    b_integer = isinstance(i, int) #Verificando se é do tipo int

    s = "Minha String" # Define a variável como String
    b_string = isinstance(s, str) # Verifica se é do tipo string

    f = 1.9 # Define a variável como float
    b_float = isinstance(f, float) # Verifica se a variável é float

    t = True # Define a variável como booleana
    b_bool = isinstance(t, bool) # Verifica se a variavel é booleana

    a = [] # Define se a variável é como array ou lista
    b_array = isinstance(a, list) # Verifica se a variável é do tipo array

    v = 1
    b_isset = v is not None # Verifica se não é None
    
    return render_template(
        "index.html",
        b_integer=b_integer,
        b_string=b_string,
        b_float=b_float,
        b_bool=b_bool,
        b_array=b_array,
        b_isset=b_isset
    )
if __name__ == "__main__":
    app.run(debug=True)