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
    var name = document.getElementById('name'),
        costSum = document.getElementById('costSum'),
        resLove = document.getElementById('resLove'),
        placeLove = document.getElementById('placeLove'),
        timeFirst = document.getElementById('timeFirst'),
        resFirst = document.getElementById('resFirst'),
        placeFirst = document.getElementById('placeFirst'),
        timeLast = document.getElementById('timeLast'),
        resLast = document.getElementById('resLast'),
        placeLast = document.getElementById('placeLast'),
        contentShow = document.getElementById('contentShow');

    function getData(){
        var idValue = stuId[0].value;
        $.ajax({
            url:baseUrl+'/api/record/first/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                timeFirst.innerText = data.time;
                resFirst.innerText = data.restaurant;
                placeFirst.innerText = data.place;                  
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
                timeLast.innerText = data.time;
                resLast.innerText = data.restaurant;
                placeLast.innerText = data.place;   
            }
        })
        
        $.ajax({
            url:baseUrl+'/api/cost/sum/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){               
                costSum.innerText = data['sum(cost)'];
            }
        })
        
        $.ajax({
            url:baseUrl+'/api/place/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                resLove.innerText = data.restaurant;
                placeLove.innerText = data.place;
            }
        })
        contentShow.style.display = 'block';
    }
    



    signUp[0].addEventListener('click', getData,false);
    
})