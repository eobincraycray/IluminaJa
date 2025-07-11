 function atualizarContador() {
    const texto = document.getElementById('descricao').value;
    document.getElementById('contador').innerText = `${texto.length}/500`;
  }

  window.onload = function () {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        document.getElementById("latitude").value = position.coords.latitude;
        document.getElementById("longitude").value = position.coords.longitude;
      }, function (error) {
        alert("Erro ao capturar localização: " + error.message);
      });
    } else {
      alert("Geolocalização não é suportada pelo seu navegador.");
    }
  };