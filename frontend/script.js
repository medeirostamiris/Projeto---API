document.addEventListener("DOMContentLoaded", function () {

const API_URL = "http://localhost:5000/items";

let livrosCache = [];

//  CARREGAR LIVROS

async function carregarLivros() {

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            console.error("Erro ao buscar livros");
            return;
        }

        const data = await response.json();

        if (!Array.isArray(data)) {
            console.error("Resposta inválida:", data);
            return;
        }

        livrosCache = data;

        const tbody = document.getElementById("listaLivros");
        tbody.innerHTML = "";

        if (livrosCache.length === 0) {
            tbody.innerHTML = "<tr><td colspan='6'>Nenhum livro cadastrado</td></tr>";
            return;
        }

        livrosCache.forEach(livro => {

            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${livro.titulo}</td>
                <td>${livro.tipo}</td>
                <td>${livro.status}</td>
                <td>${livro.descricao || "-"}</td>
                <td>${livro.data || "-"}</td>
                <td>
                    <button onclick="abrirModalEditar(${livro.id})">✏️</button>
                    <button onclick="deletarLivro(${livro.id})">🗑️</button>
                </td>
            `;

            tbody.appendChild(tr);

        });

    } catch (error) {
        console.error("Erro ao carregar livros:", error);
    }
}



// CADASTRAR

document.getElementById("formLivro").addEventListener("submit", async function (e) {

    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const status = document.getElementById("status").value;
    const descricao = document.getElementById("descricao").value;
    const data = document.getElementById("data").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            titulo,
            tipo: "livro",
            status,
            descricao,
            data
        })
    });

    const result = await response.json();

    if (!response.ok) {
        alert(result.error);
        return;
    }

    alert(result.message);

    e.target.reset();

    await carregarLivros();
});

// DELETAR

async function deletarLivro(id) {

    if (!confirm("Deseja realmente excluir este livro?")) return;

    const response = await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });

    const result = await response.json();

    if (!response.ok) {
        alert(result.error);
        return;
    }

    alert(result.message);

    await carregarLivros();
}

// ABRIR MODAL

function abrirModalEditar(id) {

    const livro = livrosCache.find(l => l.id === id);

    if (!livro) {
        alert("Livro não encontrado");
        return;
    }

    document.getElementById("editId").value = livro.id;
    document.getElementById("editTitulo").value = livro.titulo;
    document.getElementById("editStatus").value = livro.status;
    document.getElementById("editDescricao").value = livro.descricao || "";
    document.getElementById("editData").value = livro.data || "";

    document.getElementById("modalEditar").style.display = "block";
}

// FECHAR MODAL

function fecharModal() {
    document.getElementById("modalEditar").style.display = "none";
}

// SALVAR EDIÇÃO

document.getElementById("formEditar").addEventListener("submit", async function (e) {

    e.preventDefault();

    const id = document.getElementById("editId").value;

    const titulo = document.getElementById("editTitulo").value;
    const status = document.getElementById("editStatus").value;
    const descricao = document.getElementById("editDescricao").value;
    const data = document.getElementById("editData").value;

    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            titulo,
            tipo: "livro",
            status,
            descricao,
            data
        })
    });

    const result = await response.json();

    if (!response.ok) {
        alert(result.error);
        return;
    }

    alert(result.message);

    fecharModal();

    await carregarLivros();
});

// INICIAR

carregarLivros();

// Deixa as funções visíveis para o HTML
window.abrirModalEditar = abrirModalEditar;
window.deletarLivro = deletarLivro;
window.fecharModal = fecharModal;

});