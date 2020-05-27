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
            },
            error:function(){
                console.log("这部分的服务器罢工了，试试重新请求吧！");
                
            },
        })
        $.ajax({
            url:baseUrl+'/api/record/last/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                console.log(data);
                
            }
        })
        
        $.ajax({
            url:baseUrl+'/api/cost/sum/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                console.log(data);
                
            }
        })
        
        $.ajax({
            url:baseUrl+'/api/place/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                console.log(data);
                
            }
        })
    }
    



    signUp[0].addEventListener('click', getData,false);
    
})