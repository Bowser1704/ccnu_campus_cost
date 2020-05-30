
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
        var right = echarts.init(document.getElementById('right'));
        $.ajax({
            url:baseUrl+'/api/rank/restaurant/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){
                var showData = []
                //处理json数据
                for(let i = 0;i <data.length;i++){
                    // restaurant.push(data[i].restaurant);
                    // count.push(data[i]['count(*)']);
                    var item = new Object();
                    item.value = data[i]['count(*)'];
                    item.name = data[i].restaurant;
                    showData.push(item);  
                }
                
                left.setOption(Option = {
                
                    title: {
                        text: '食堂次数排行榜',
                        left: 'right',
                        top: 20,
                        right:20,
                        textStyle: {
                            color: '#2f83e4'
                        }
                    },
                
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b} : {c} ({d}%)'
                    },
                    series: [
                        {
                            
                            type: 'pie',
                            radius: '65%',
                            center: ['50%', '50%'],
                            data: showData,
                            // labelLine: {
                            //     lineStyle: {
                            //         color: 'rgba(255, 255, 255, 0.3)'
                            //     },
                            //     smooth: 0.2,
                            //     length: 10,
                            //     length2: 20
                            // },
                            // itemStyle: {
                            //     color: '#c23531',
                            //     shadowBlur: 200,
                            //     shadowColor: 'rgba(0, 0, 0, 0.5)'
                            // },
                
                            animationType: 'scale',
                            animationEasing: 'elasticOut',
                            animationDelay: function (idx) {
                                return Math.random() * 200;
                            }
                        }
                    ]
                });
                

            }
        })
        $.ajax({
            url:baseUrl+'/api/cost/list/week/'+idValue,
            type:'get',
            dataType:'json',
            success:function(data){  
                var preWeekCost = [];
                var showX = [];
                for(var i = 0; i < data.length;i++){
                    preWeekCost.push(data[i]['sum(cost)']);
                    showX.push(i+1);
                }
                
                // console.log(preWeekCost);
                right.setOption(Option = {
                    title: {
                        text: '每周消费总金额统计',
                        left: 'center',
                        top: 20,
                        textStyle: {
                            color: '#2f83e4'
                        }
                    },
                    xAxis: {
                        
                        data: showX,
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: preWeekCost,
                        type: 'line'
                    }]
                });
                
            }
        })
    }


    readMore.addEventListener('click',getMoreInf,false);
    
    



    btnChange.addEventListener('click',changeUserHead,false);

})