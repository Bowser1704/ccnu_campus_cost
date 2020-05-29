
$(document).ready(function(){
    var btnChange = document.getElementById('pic_change');
    var pic = document.getElementById('pic');


    
    function changeUserHead(){
        var str = window.getComputedStyle(pic).backgroundImage;
        
        var tmp=str.split("(")[1].split(")")[0];
        tmp = tmp.slice(-6,-5);
        if(tmp == 1){
            $('#pic').removeClass("pic1").addClass("pic2");
        }else{
            $('#pic').removeClass('pic2').addClass('pic1');   
        }
    }
    
   

    
    var readMore = document.getElementById('read_more');
    function getMoreInf(){
        var idValue = stuId.value;
        var left = echarts.init(document.getElementById('left'));
        $.ajax({
            url:baseUrl+'/api/rank/restaurant/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                var restaurant = [];
                var count = [];
                for(let i = 0;i <data.length;i++){
                    restaurant.push(data[i].restaurant);
                    count.push(data[i]['count(*)']);
                    left.setOption(Option);
                }
                console.log(count);

            }
        })
        $.ajax({
            url:baseUrl+'/api/rank/restaurant/'+idValue,
            type:'get',
            dataType:'json',
            success:function(){
                
            }
        })
        var Option = {
            backgroundColor: '#2c343c',
        
            title: {
                text: 'Customized Pie',
                left: 'center',
                top: 20,
                textStyle: {
                    color: '#ccc'
                }
            },
        
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },
        
            visualMap: {
                show: false,
                min: 80,
                max: 600,
                inRange: {
                    colorLightness: [0, 1]
                }
            },
            series: [
                {
                    name: '访问来源',
                    type: 'pie',
                    radius: '55%',
                    center: ['50%', '50%'],
                    data: [
                        {value: 335, name: '直接访问'},
                        {value: 310, name: '邮件营销'},
                        {value: 274, name: '联盟广告'},
                        {value: 235, name: '视频广告'},
                        {value: 400, name: '搜索引擎'}
                    ].sort(function (a, b) { return a.value - b.value; }),
                    roseType: 'radius',
                    label: {
                        color: 'rgba(255, 255, 255, 0.3)'
                    },
                    labelLine: {
                        lineStyle: {
                            color: 'rgba(255, 255, 255, 0.3)'
                        },
                        smooth: 0.2,
                        length: 10,
                        length2: 20
                    },
                    itemStyle: {
                        color: '#c23531',
                        shadowBlur: 200,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    },
        
                    animationType: 'scale',
                    animationEasing: 'elasticOut',
                    animationDelay: function (idx) {
                        return Math.random() * 200;
                    }
                }
            ]
        };
        
    }


    readMore.addEventListener('click',getMoreInf,false);
    
    



    btnChange.addEventListener('click',changeUserHead,false);

})