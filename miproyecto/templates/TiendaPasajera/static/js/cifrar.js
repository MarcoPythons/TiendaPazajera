function cifrar(){
        var input_pass = document.getElementById("clave");

        input_pass.value = SHA1(input_pass.value);		
    }
    
