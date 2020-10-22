function cifrar2(){
    var input_pass = document.getElementById("clave2");

    input_pass.value = SHA1(input_pass.value);		
}