// Suponiendo que tienes un botón con id 'fetch-balance' y un elemento para mostrar el saldo con id 'balance'
document.getElementById('fetch-balance').addEventListener('click', () => {
    const token = localStorage.getItem('authToken');  // O de donde sea que consigas el token
  
    fetch('/api/get_balance', {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + token,
      },
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('balance').textContent = `Saldo: ${data.balance}`;
    })
    .catch(error => console.error('Error al obtener el saldo:', error));
  });
  