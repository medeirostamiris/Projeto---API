const API_URL = "http://localhost:5000/items";


async function carregarLivros() {
    try {
        const response = await fetch(API_URL);
        const livros = await response.json();

        const tbody = document.getElementById("listaLivros");
        tbody.innerHTML = "";

        if (livros.length === 0) {
            tbody.innerHTML = "<tr><td colspan='4'>Nenhum livro cadastrado</td></tr>";
            return;
        }

        livros.forEach(livro => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
            <td>${livro.titulo}</td>
            <td>${livro.tipo}</td>
            <td>${livro.status}</td>
            <td>${livro.descricao || "-"}</td>
            <td>${livro.data || "-"}</td>
        `;

            tbody.appendChild(tr);
        });

    } catch (error) {
        console.error("Erro ao carregar livros:", error);
    }
}


document.getElementById("formLivro").addEventListener("submit", async (e) => {
    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const status = document.getElementById("status").value;
    const descricao = document.getElementById("descricao").value;
    const data = document.getElementById("data").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            titulo: titulo,
            tipo: "livro",
            status: status,
            descricao: descricao,
            data: data
        })
    });

    if (response.ok) {
        document.getElementById("mensagem").innerText = "Livro cadastrado com sucesso!";
        carregarLivros();
        e.target.reset();
    } else {
        const erro = await response.json();
        document.getElementById("mensagem").innerText = erro.error;
    }
});

carregarLivros();
