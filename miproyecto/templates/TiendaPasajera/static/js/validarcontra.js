
function validarPassword(pass1, pass2){
    if(pass1 === pass2){
        return true;
    }else{
        return false;
    }

}

function validarFormulario(){
    var contra = document.querySelector('#password1').value;
    var rcontra = document.querySelector('#password2').value;
    if(validarPassword(contra, rcontra) == false){
            alert("Las contraseñas no coinciden");
}}