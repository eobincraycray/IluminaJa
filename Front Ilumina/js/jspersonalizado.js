function atualizarContador() {
    const textarea = document.getElementById("descricao");
    const contador = document.getElementById("contador");
    contador.textContent = `${textarea.value.length}/500`;
  }