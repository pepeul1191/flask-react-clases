function getCookie(name) {
  console.log(document)
  let cookieArray = document.cookie.split(';'); // Dividir el string de cookies en un array
  for (let i = 0; i < cookieArray.length; i++) {
      let cookiePair = cookieArray[i].split('='); // Dividir cada par nombre=valor
      if (name === cookiePair[0].trim()) { // Eliminar espacio blanco y comparar el nombre
          return decodeURIComponent(cookiePair[1]); // Decodificar el valor de la cookie y retornarlo
      }
  }
  return null; // Si no se encuentra la cookie, retornar null
}

