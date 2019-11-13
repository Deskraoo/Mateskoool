var slideIndex = 1;
showSlides(slideIndex);

// Controles adelante y atras
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Miniaturas
function currentSlide(n) {
  showSlides(slideIndex = n);
}

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 3500); // Cambia imagen cada 3,5 seg
}

/*Alertas Slider*/
function Instagram() {
  alert("Seras redirigido al Instagram de Mateskool");
}

function Facebook() {
  alert("Seras redirigido al Facebook de Mateskool");
}

function Twitter() {
  alert("Seras redirigido al Twitter de Mateskool");
}

function Enviar() {
  alert("Informacion enviada correctamente");
}

function Validar(){
  var nombre = document.getElementById('nombre').value;
  var apellidos = document.getElementById('apellidos').value;
  var direccion = document.getElementById('direccion').value;
  var email = document.getElementById('email').value;
  var telefono = document.getElementById('telefono').value;

  if(nombre==""){
      $('#Anombre').html('Debe ingresar un nombre').slideDown(500);
      $('#nombre').focus();
      return false;
  }else{
      $('#Anombre').html('').slideUp(300);
  }

  if(apellidos==""){
      $('#Aapellido').html('Debe ingresar un apellido').slideDown(500);
      $('#apellidos').focus();
      return false;
  }else{
      $('#Aapellido').html('').slideUp(300);
  }

  if(direccion==""){
      $('#Adireccion').html('Debe ingresar una direccion').slideDown(500);
      $('#direccion').focus();
      return false;
  }else{
      $('#Adireccion').html('').slideUp(300);
  }

  if(email==""){
      $('#Aemail').html('Debe ingresar un email').slideDown(500);
      $('#email').focus();
      return false;
  }else{
      $('#Aemail').html('').slideUp(300);
  }
  
  if(telefono==""){
      $('#Atelefono').html('Debe ingresar un telefono').slideDown(500);
      $('#telefono').focus();
      return false;
  }else{
      $('#Atelefono').html('').slideUp(300);
  }
}