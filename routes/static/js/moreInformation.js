
$(document).ready(function(){
    var btnChange = document.getElementById('pic_change');
    var pic = document.getElementById('pic');


    
    function changeUserHead(){
        var str = window.getComputedStyle(pic).backgroundImage;
        console.log(str);
        
        var tmp=str.split("(")[1].split(")")[0];
        tmp = tmp.slice(-6,-5);
        if(tmp == 1){
            $('#pic').removeClass("pic1").addClass("pic2");
        }else{
            $('#pic').removeClass('pic2').addClass('pic1');   
        }
    }
    
    btnChange.addEventListener('click',changeUserHead,false);
})