$(document).ready(function(){
    var activeMenu = false,
        opacity = 0.6;

    // MENU RESPONSIVE
    $('#xresponsive-menu').on('click',function(){
        if(!activeMenu){
            $('#xbar').animate({
                left: "0px"
            }, 500);
            activeMenu = true;
        }else{
            $('#xbar').animate({
                left: "-120%"
            }, 500);
            activeMenu = false;
        }
    });


});