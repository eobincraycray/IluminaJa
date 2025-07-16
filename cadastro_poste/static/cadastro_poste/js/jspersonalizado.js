// Atualiza contador de caracteres
function atualizarContador() {
  const texto = document.getElementById('descricao');
  const contador = document.getElementById('contador');
  if (texto && contador) {
    contador.innerText = `${texto.value.length}/500`;
  }
}

// Geolocalização ao carregar página
window.addEventListener('load', function () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      const latInput = document.getElementById("latitude");
      const lngInput = document.getElementById("longitude");

      if (latInput && lngInput) {
        latInput.value = position.coords.latitude;
        lngInput.value = position.coords.longitude;
      }
    }, function (error) {
      alert("Erro ao capturar localização: " + error.message);
    });
  } else {
    alert("Geolocalização não é suportada pelo seu navegador.");
  }
});

// Inicializa o mapa com marcadores
function initMap() {
  const centro = { lat: -14.223, lng: -42.782 };

  const mapEl = document.getElementById("map");
  if (!mapEl) return;

  const map = new google.maps.Map(mapEl, {
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

// Modal de informações do poste
function openInfoModal(problema, descricao, rua, numero, bairro, cidade) {
  const problemaEl = document.getElementById('modalProblema');
  const descricaoEl = document.getElementById('modalDescricao');
  const enderecoEl = document.getElementById('modalEndereco');

  if (problemaEl && descricaoEl && enderecoEl) {
    problemaEl.textContent = problema;
    descricaoEl.textContent = descricao;
    enderecoEl.textContent = `${rua}, Nº ${numero}, ${bairro} - ${cidade}`;
  }

  const modalEl = document.getElementById('infoModal');
  if (modalEl) {
    const modal = new bootstrap.Modal(modalEl);
    modal.show();
  }
}

// Modal para confirmação de correção
function abrirModalConfirmarCorrecao(posteId) {
  console.log("Abrindo modal para poste:", posteId); // <== ADICIONE ISSO
  const inputPosteId = document.getElementById("inputPosteId");
  const lampadaSelect = document.getElementById("lampadaSelect");

  if (!inputPosteId || !lampadaSelect) return;

  inputPosteId.value = posteId;

  fetch(`/lampada-por-poste/${posteId}/`)
    .then(response => response.json())
    .then(data => {
      lampadaSelect.innerHTML = ''; // limpa opções

      if (data.id) {
        const option = document.createElement("option");
        option.value = data.id;
        option.textContent = `${data.tipo} - ${data.potencia}W`;
        lampadaSelect.appendChild(option);
      } else {
        const option = document.createElement("option");
        option.textContent = "Nenhuma lâmpada associada";
        option.disabled = true;
        lampadaSelect.appendChild(option);
      }

      const modalEl = document.getElementById('modalConfirmarCorrecao');
      if (modalEl) {
        console.log("Mostrando modal..."); // <== ADICIONE ISSO
        new bootstrap.Modal(modalEl).show();
      }
    })
    .catch(error => {
      console.error("Erro ao buscar lâmpada:", error);
    });
}

window.addEventListener("load", () => {
  initMap(); // chama somente quando tudo estiver carregado
});
