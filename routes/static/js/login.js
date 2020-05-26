$(document).ready(function(){
    var signUp = $('#sigup-btn');
    var stuId = $('#stuId');
    var baseUrl = 'http://127.0.0.1:5000';
    function checkId(){
        
        // console.log(idValue);
        //验证输入学号有效
        var userReg = /^\d{10}$/;
        if(!userReg.test(idValue)){
            
        }
        //发送学号数据
        // $.ajax({
        //     url:
        // })

        
        
        
    }
    //请求相关数据
    function getData(){
        var idValue = stuId[0].value;
        $.ajax({
            url:baseUrl+'/api/record/first/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                console.log(data);                   
            }
        })
        
        
        console.log(baseUrl+'/api/record/first/'+idValue);

        // $.get(baseUrl+'/api/record/first/'+idValue,
        // function(data,status){
        //     console.log(data);
            
        // })
    }
    



    signUp[0].addEventListener('click', getData,false);
    
})