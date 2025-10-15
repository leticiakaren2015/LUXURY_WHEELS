document.addEventListener('DOMContentLoaded', function() {
  const inicio = document.getElementById('id_data_inicio');
  const fim = document.getElementById('id_data_fim');
  const clienteSelect = document.getElementById('id_cliente');
  const valorDisplay = document.getElementById('valor_total_display');

  // Valores por categoria (mesmos do models.py)
  const valores = {
    'Gold': 600,
    'Silver': 250,
    'Econômico': 50,
    'Economico': 50  // fallback sem acento
  };

  function extrairCategoriaDoTexto(texto) {
    // Texto típico do select: "Letícia (Gold - 600€)" ou "Nome (Gold)"
    if (!texto) return null;
    const m = texto.match(/\((.*?)\)/);
    const dentro = m ? m[1] : texto;
    // procurar palavras-chave
    if (dentro.indexOf('Gold') !== -1) return 'Gold';
    if (dentro.indexOf('Silver') !== -1) return 'Silver';
    if (dentro.indexOf('Econ') !== -1 || dentro.indexOf('Econômico') !== -1 || dentro.indexOf('Economico') !== -1) return 'Econômico';
    // fallback: verificar todo o texto
    if (texto.indexOf('Gold') !== -1) return 'Gold';
    if (texto.indexOf('Silver') !== -1) return 'Silver';
    if (texto.indexOf('Econ') !== -1 || texto.indexOf('Economico') !== -1) return 'Econômico';
    return null;
  }

  function calcular() {
    if (!inicio || !fim || !valorDisplay) return;

    const vInicio = inicio.value;
    const vFim = fim.value;
    if (!vInicio || !vFim) {
      valorDisplay.textContent = '—';
      return;
    }

    const d1 = new Date(vInicio);
    const d2 = new Date(vFim);
    const diffMs = d2 - d1;
    const dias = Math.floor(diffMs / (1000*60*60*24)) + 1;

    if (isNaN(dias) || dias <= 0) {
      valorDisplay.textContent = '0';
      return;
    }

    // pegar categoria do cliente selecionado
    let categoria = null;
    if (clienteSelect && clienteSelect.selectedIndex >= 0) {
      const txt = clienteSelect.options[clienteSelect.selectedIndex].text;
      categoria = extrairCategoriaDoTexto(txt);
    }

    const valorDiario = valores[categoria] || 0;
    const total = dias * valorDiario;
    valorDisplay.textContent = total.toFixed(2);
  }

  if (inicio) inicio.addEventListener('change', calcular);
  if (fim) fim.addEventListener('change', calcular);
  if (clienteSelect) clienteSelect.addEventListener('change', calcular);
});
