function initMap() {
  const centro = { lat: -14.223, lng: -42.782 };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: centro,
  });

  if (Array.isArray(locais)) {
    locais.forEach(local => {
      if (local && typeof local.lat === "number" && typeof local.lng === "number") {
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
    console.error("Variável 'locais' não encontrada ou não é um array.");
  }
}

// Exporta para global pra Google Maps encontrar
window.initMap = initMap;
