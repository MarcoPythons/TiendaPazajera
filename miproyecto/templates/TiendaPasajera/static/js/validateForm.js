$(document).ready(function(){

    var btnEnviar = document.querySelector('#next');

    var Rut = {
        // Valida el rut con su cadena completa "XXXXXXXX-X"
        validaRut : function (rutCompleto) {
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
                return false;
            var tmp = rutCompleto.split('-');
            var digv= tmp[1]; 
            var rut = tmp[0];
            if ( digv == 'K' ) digv = 'k' ;
            return (Rut.dv(rut) == digv );
        },
        dv : function(T){
            var M=0,S=1;
            for(;T;T=Math.floor(T/10))
                S=(S+T%10*(9-M++%6))%11;
            return S?S-1:'k';
        }
    }

    function validarEmail(mail) { 
        return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(mail); 
    }



    function validarFormulario(){
        var rut = document.querySelector('#rut').value;
        var nombre = document.querySelector('#nombre').value;
        var apellido = document.querySelector('#apellido').value;
        var fecNac = document.querySelector('#fecNac').value;
        var correo = document.querySelector('#correo').value;
        var contra = document.querySelector('#contra').value;
        var rcontra = document.querySelector('#rcontra').value;

        if(!Rut.validaRut(rut)){
            alert("Rut Incorrecto");
        }else{
            if(!validarEmail(correo)){
                alert("Correo Incorrecto");
            }else{
                if(!validarPassword(contra, rcontra)){
                    alert("Las contraseñas no coinciden");
                }
            }
        }
    }

    // VALIDAR CONTRASEÑAS IGUALES
    // las contraseñas seran cifradas en la segunda etapa
    function validarPassword(pass1, pass2){
        if(pass1 === pass2){
            return true;
        }else{
            return false;
        }
    }





    btnEnviar.addEventListener('click', function(e){
        e.preventDefault();
        validarFormulario();
    });

});