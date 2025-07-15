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


// Lista de postes vindos do Django
let locais = []; // Essa variável será preenchida dinamicamente no template

function initMap() {
  const centro = { lat: -14.223, lng: -42.782 }; // Centro padrão

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: centro,
  });

  if (Array.isArray(locais) && locais.length > 0) {
    locais.forEach((local) => {
      if (
        local &&
        typeof local.lat === "number" &&
        typeof local.lng === "number"
      ) {
        new google.maps.Marker({
          position: { lat: local.lat, lng: local.lng },
          map,
          title: local.titulo || "Poste",
        });
      } else {
        console.warn("Local inválido:", local);
      }
    });
  } else {
    console.info("Nenhum local para mostrar no mapa.");
  }
}
