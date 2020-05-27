$(document).ready(function(){
    var signUp = document.getElementById('sigup-btn');
    var stuId = document.getElementById('stuId');
    var baseUrl = 'http://127.0.0.1:5000';
    var stuName = document.getElementById('stuName');

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

    var stuNameInfo = document.getElementById('stuName_info'),
        stuIdInfo = document.getElementById('stuId_info');

    var wcPic = document.getElementById('wcPic');
    function checkStuId (){

        var idValue = stuId.value;
        // console.log(idValue);
        //验证输入学号有效
        var userReg = /^201[6-9]21[0-6]\d{3}$/;
        // console.log(idValue);
        if(checkStuName()){
            if( !userReg.test(idValue)){
                stuIdInfo.innerHTML = '请输入有效学号哦！';
            }else{
                stuIdInfo.innerHTML = '';
                signUp.addEventListener('click', getData,false);
            } 
        }

        
    }
    function checkStuName(){
        var stuNameValue = stuName.value;
        if(!stuNameValue){
            stuNameInfo.innerHTML = '请输入有效姓名哦！';
            return false;  
        }else{
            stuNameInfo.innerHTML = '';
            return true;
        }
    }

    //请求相关数据
    
    function getData(){
        var idValue = stuId.value;
        
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
        name.innerHTML = stuName.value;
        wcPic.src = baseUrl + '/wc/' + idValue + '.png';
        contentShow.style.display = 'block';
    }




    stuName.addEventListener('blur',checkStuName,false);
    stuId.addEventListener('blur',checkStuId,false);
  
})