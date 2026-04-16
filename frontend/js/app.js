const API = "http://127.0.0.1:8000/api/";

// REGISTRO
async function register() {
    let username = document.getElementById("regUser").value;
    let password = document.getElementById("regPass").value;

    let res = await fetch(API + "usuarios/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    alert("Usuario creado");
}

// LOGIN
async function login() {
    let username = document.getElementById("logUser").value;
    let password = document.getElementById("logPass").value;

    let res = await fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    let data = await res.json();

    if (data.access) {
        localStorage.setItem("token", data.access);
        alert("Login correcto");
    } else {
        alert("Error en login");
    }
}

// TOKEN
function getToken() {
    return localStorage.getItem("token");
}

// ESTADO
async function getEstado() {
    let res = await fetch(API + "estado/", {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    });

    let data = await res.json();
    document.getElementById("estado").innerText =
        JSON.stringify(data, null, 2);
}

// ACCIÓN
async function accion(id) {
    let res = await fetch(API + "accion/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify({accion_id: id})
    });

    let data = await res.json();
    alert("Acción ejecutada");
}

// RANKING
async function getRanking() {
    let res = await fetch(API + "ranking/");
    let data = await res.json();

    document.getElementById("ranking").innerText =
        JSON.stringify(data, null, 2);
}