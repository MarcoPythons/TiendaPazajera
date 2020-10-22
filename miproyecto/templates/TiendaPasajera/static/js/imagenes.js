$(document).ready(function() {
    var lista = $('li').hide();
    $('#mostrar').click(function() {
            var i = 0;
            (function mostrarimg() {
                lista.eq(i++).fadeIn(122, mostrarimg);
            })();
    });
    $('#ocultar').click(function() {
            var i = $('li').size();
            (function ocultarimg() {
                lista.eq(--i).fadeOut(200, ocultarimg);
            })();
    });
});